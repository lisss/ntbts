const {
  Interval,
  Job,
  merge,
  insert,
  intersect,
  canAttendAllAppointments,
  minMeetingRooms,
  findMaxCpuLoad,
  findEmployeeFreeTime,
} = require(".");

const testMerge = () => {
  merged_intervals = merge([
    new Interval(1, 4),
    new Interval(2, 5),
    new Interval(7, 9),
  ]);
  result = "";
  for (i = 0; i < merged_intervals.length; i++) {
    result += merged_intervals[i].get_interval() + " ";
  }
  console.log(`Merged intervals: ${result}`);

  merged_intervals = merge([
    new Interval(6, 7),
    new Interval(2, 4),
    new Interval(5, 9),
  ]);
  result = "";
  for (i = 0; i < merged_intervals.length; i++) {
    result += merged_intervals[i].get_interval() + " ";
  }
  console.log(`Merged intervals: ${result}`);

  merged_intervals = merge([
    new Interval(1, 4),
    new Interval(2, 6),
    new Interval(3, 5),
  ]);
  result = "";
  for (i = 0; i < merged_intervals.length; i++) {
    result += merged_intervals[i].get_interval() + " ";
  }
  console.log(`Merged intervals: ${result}`);
};

const testInsert = () => {
  process.stdout.write("Intervals after inserting the new interval: ");
  let result = insert(
    [new Interval(1, 3), new Interval(5, 7), new Interval(8, 12)],
    new Interval(4, 6)
  );
  for (i = 0; i < result.length; i++) {
    result[i].printInterval();
  }
  console.log();

  process.stdout.write("Intervals after inserting the new interval: ");
  result = insert(
    [new Interval(1, 3), new Interval(5, 7), new Interval(8, 12)],
    new Interval(4, 10)
  );
  for (i = 0; i < result.length; i++) {
    result[i].printInterval();
  }
  console.log();

  process.stdout.write("Intervals after inserting the new interval: ");
  result = insert([new Interval(2, 3), new Interval(5, 7)], new Interval(1, 4));
  for (i = 0; i < result.length; i++) {
    result[i].printInterval();
  }
  console.log();
};

const testIntersection = () => {
  process.stdout.write("Intervals Intersection: ");
  let result = intersect(
    [new Interval(1, 3), new Interval(5, 6), new Interval(7, 9)],
    [new Interval(2, 3), new Interval(5, 7)]
  );
  for (i = 0; i < result.length; i++) {
    result[i].printInterval();
  }
  console.log();

  process.stdout.write("Intervals Intersection: ");
  result = intersect(
    [new Interval(1, 3), new Interval(5, 7), new Interval(9, 12)],
    [new Interval(5, 10)]
  );
  for (i = 0; i < result.length; i++) {
    result[i].printInterval();
  }
  console.log();
};

const testCanAttendAllAppointments = () => {
  console.log(
    `Can attend all appointments: ${canAttendAllAppointments([
      new Interval(1, 4),
      new Interval(2, 5),
      new Interval(7, 9),
    ])}`
  );

  console.log(
    `Can attend all appointments: ${canAttendAllAppointments([
      new Interval(6, 7),
      new Interval(2, 4),
      new Interval(8, 12),
    ])}`
  );

  console.log(
    `Can attend all appointments: ${canAttendAllAppointments([
      new Interval(4, 5),
      new Interval(2, 3),
      new Interval(3, 6),
    ])}`
  );
};

const testMeetingRooms = () => {
  console.log(
    `Minimum Interval rooms required: ${minMeetingRooms([
      new Interval(4, 5),
      new Interval(2, 3),
      new Interval(2, 4),
      new Interval(3, 5),
    ])}`
  );
  console.log(
    `Minimum Interval rooms required: ${minMeetingRooms([
      new Interval(1, 4),
      new Interval(2, 5),
      new Interval(7, 9),
    ])}`
  );
  console.log(
    `Minimum Interval rooms required: ${minMeetingRooms([
      new Interval(6, 7),
      new Interval(2, 4),
      new Interval(8, 12),
    ])}`
  );
  console.log(
    `Minimum Interval rooms required: ${minMeetingRooms([
      new Interval(1, 4),
      new Interval(2, 3),
      new Interval(3, 6),
    ])}`
  );
};

const testFindMaxCpuLoad = () => {
  console.log(
    `Maximum CPU load at any time: ${findMaxCpuLoad([
      new Job(1, 4, 3),
      new Job(2, 5, 4),
      new Job(7, 9, 6),
    ])}`
  );
  console.log(
    `Maximum CPU load at any time: ${findMaxCpuLoad([
      new Job(6, 7, 10),
      new Job(2, 4, 11),
      new Job(8, 12, 15),
    ])}`
  );
  console.log(
    `"Maximum CPU load at any time: ${findMaxCpuLoad([
      new Job(1, 4, 2),
      new Job(2, 4, 1),
      new Job(3, 6, 5),
    ])}`
  );
};

const testFindEmployeeFreeTime = () => {
  input = [
    [new Interval(1, 3), new Interval(5, 6)],
    [new Interval(2, 3), new Interval(6, 8)],
  ];
  intervals = findEmployeeFreeTime(input);
  result = "Free intervals: ";
  for (i = 0; i < intervals.length; i++) result += intervals[i].getInterval();
  console.log(result);

  input = [
    [new Interval(1, 3), new Interval(9, 12)],
    [new Interval(2, 4)],
    [new Interval(6, 8)],
  ];
  intervals = findEmployeeFreeTime(input);
  result = "Free intervals: ";
  for (i = 0; i < intervals.length; i++) result += intervals[i].getInterval();
  console.log(result);

  input = [
    [new Interval(1, 3)],
    [new Interval(2, 4)],
    [new Interval(3, 5), new Interval(7, 9)],
  ];
  intervals = findEmployeeFreeTime(input);
  result = "Free intervals: ";
  for (i = 0; i < intervals.length; i++) result += intervals[i].getInterval();
  console.log(result);
};

testFindEmployeeFreeTime();
