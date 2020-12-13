const Heap = require("collections/heap");

class Interval {
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }

  getInterval = () => {
    return "[" + this.start + ", " + this.end + "]";
  };

  printInterval = () => {
    process.stdout.write(`[${this.start}, ${this.end}]`);
  };
}

class Job {
  constructor(start, end, cpuLoad) {
    this.start = start;
    this.end = end;
    this.cpuLoad = cpuLoad;
  }
}

const merge = (intervals) => {
  const merged = [];
  intervals.sort((a, b) => a.start - b.start);

  let start = intervals[0].start;
  end = intervals[0].end;

  for (let i = 1; i < intervals.length; i++) {
    const curr = intervals[i];

    if (curr.start <= end) {
      end = Math.max(end, curr.end);
    } else {
      merged.push(new Interval(start, end));
      start = curr.start;
      end = curr.end;
    }
  }

  merged.push(new Interval(start, end));

  return merged;
};

const insert = (intervals, newInterval) => {
  const merged = [];
  let i = 0;

  while (i < intervals.length && intervals[i].end < newInterval.start) {
    merged.push(intervals[i]);
    i++;
  }

  while (i < intervals.length && intervals[i].start <= newInterval.end) {
    newInterval.start = Math.min(intervals[i].start, newInterval.start);
    newInterval.end = Math.max(intervals[i].end, newInterval.end);
    i++;
  }

  merged.push(newInterval);

  while (i < intervals.length) {
    merged.push(intervals[i]);
    i++;
  }

  return merged;
};

const intersect = (intervalsA, intervalsB) => {
  const result = [];
  let i = 0;
  j = 0;

  while (i < intervalsA.length && j < intervalsB.length) {
    const a = intervalsA[i];
    const b = intervalsB[j];

    let start, end;

    if (b.start >= a.start && b.start <= a.end) {
      start = b.start;
    } else if (a.start >= b.start && a.start <= b.end) {
      start = a.start;
    }

    if (start) {
      end = Math.min(a.end, b.end);
      result.push(new Interval(start, end));
    }

    if (a.end < b.end) {
      i++;
    } else {
      j++;
    }
  }
  return result;
};

const canAttendAllAppointments = (intervals) => {
  intervals.sort((a, b) => a.start - b.start);

  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i].start < intervals[i - 1].end) {
      return false;
    }
  }
  return true;
};

const minMeetingRooms = (meetings) => {
  meetings.sort((a, b) => a.start - b.start);

  const minHeap = new Heap([], null, (a, b) => b - a);
  let minRooms = 0;

  for (let i = 0; i < meetings.length; i++) {
    while (minHeap.length && meetings[i].start >= minHeap.peek()) {
      minHeap.pop();
    }
    minHeap.push(meetings[i].end);
    minRooms = Math.max(minRooms, minHeap.length);
  }
  return minRooms;
};

const findMaxCpuLoad = (jobs) => {
  jobs.sort((a, b) => a.start - b.start);

  const minHeap = new Heap([], null, (a, b) => b.end - a.end);
  let maxLoad = 0;
  let currLoad = 0;

  for (i = 0; i < jobs.length; i++) {
    while (minHeap.length && jobs[i].start >= minHeap.peek().end) {
      currLoad -= minHeap.pop().cpuLoad;
    }
    minHeap.push(jobs[i]);
    currLoad += jobs[i].cpuLoad;
    maxLoad = Math.max(maxLoad, currLoad);
  }
  return maxLoad;
};

/**
 * @TODO: try to understand how does this magic work
 */
class EmployeeInterval {
  constructor(interval, employeeIndex, intervalIndex) {
    this.interval = interval; // interval representing employee's working hours
    // index of the list containing working hours of this employee
    this.employeeIndex = employeeIndex;
    this.intervalIndex = intervalIndex; // index of the interval in the employee list
  }
}

const findEmployeeFreeTime = (schedule) => {
  const result = [];
  if (!schedule) return result;

  const n = schedule.length;
  if (!n) return result;

  const minHeap = new Heap(
    [],
    null,
    (a, b) => b.interval.start - a.interval.start
  );
  // insert the first interval of each employee to the queue
  for (i = 0; i < n; i++) {
    minHeap.push(new EmployeeInterval(schedule[i][0], i, 0));
  }
  let previousInterval = minHeap.peek().interval;
  while (minHeap.length > 0) {
    const queueTop = minHeap.pop();
    // if previousInterval is not overlapping with the next interval, insert a free interval
    if (previousInterval.end < queueTop.interval.start) {
      result.push(new Interval(previousInterval.end, queueTop.interval.start));
      previousInterval = queueTop.interval;
    } else {
      // overlapping intervals, update the previousInterval if needed
      if (previousInterval.end < queueTop.interval.end) {
        previousInterval = queueTop.interval;
      }
    }
    // if there are more intervals available for(the same employee, add their next interval
    const employeeSchedule = schedule[queueTop.employeeIndex];
    if (employeeSchedule.length > queueTop.intervalIndex + 1) {
      minHeap.push(
        new EmployeeInterval(
          employeeSchedule[queueTop.intervalIndex + 1],
          queueTop.employeeIndex,
          queueTop.intervalIndex + 1
        )
      );
    }
  }
  return result;
};

module.exports = {
  Interval,
  Job,
  merge,
  insert,
  intersect,
  canAttendAllAppointments,
  minMeetingRooms,
  findMaxCpuLoad,
  findEmployeeFreeTime,
};
