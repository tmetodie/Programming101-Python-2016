# Education System

We already have a Course Management System with courses and lectures, then students and teachers for those courses.
Your task is to add new app `education` with logic for tasks and solutions.

The specification is as follows:

## Tasks

We are interested in the following attributes for one task:

* Name - should be unique
* Description
* Course - FK

For our tasks, we should have the following views:

* `GET /tasks` should display a nice table with all tasks, sorted by active course.

**Also, each lecture should have a link to a detailed course page.**

* `GET /tasks/<task_id>/` - this is the detailed information about tasks.
* `POST /tasks/<task_id>/` - for editing task
* `GET POST /tasks/new/` - for creating new tasks.

**Keep your mind that only teacher can create and edit tasks!**

* `GET /tasks/<course-id>` - this should display all tasks for course.
* After that, on the page with all courses, for each course add a link to tasks view.

## Solutions

This is the interesting part of our system.
Our solution should have:

* Task - FK
* Student - FK
* Date
* URL - link with solution in Github

We should have a set of URLs:

* `GET POST /solutions/course/<course_id>/new` - for creating new solution of task
* `GET POST /solutions/course/<course_id>/edit/<solution-id>` - the form for editing an existing solution

**Only student can create and edit solutions**

* `GET /solutions/course/<course-id>/` - display all solutions only for course with course_id. Teacher who teaches this course can see all solutions for it.
* On the page with all courses, for each course add a link to solutions view.
* `GET /solutions/course/<course-id>/<task_id>` - display all solutions for certain tasks. Teacher who teaches this course can see all solutions for it.

## TESTS, TESTS, TESTS!
