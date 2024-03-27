# Blogging System

The Blogging System is a web-based application that allows users to create, update, and delete blog posts. Users can sign up or authenticate using Google or GitHub credentials. Authenticated users can also add comments to blog posts. The system provides pagination to display a set of posts per page.

## Features

- User Authentication: Users can sign up or authenticate through Google or GitHub.
- Post Creation: Authenticated users can create new blog posts.
- Post Update and Deletion: Users can edit or delete their own blog posts.
- Commenting System: Authenticated users can add comments to blog posts.
- Pagination: Blog posts are displayed in a paginated manner.

## Technology Stack

- Backend:

  - NEXT.js: React framework for building server-rendered React applications.
  - MongoDB: NoSQL database to store user-related data.
  - Firebase: Cloud storage for storing media content.
  - Prisma: Object Relational Mapper for database management.

- Frontend:
  - NEXT.js: React framework for building server-rendered React applications.
  - React.js: JavaScript library for building user interfaces.
  - CSS: Cascading Style Sheets for styling the components.

## Prerequisites

- Node.js: Make sure you have Node.js installed. You can download it from [https://nodejs.org](https://nodejs.org).

## Getting Started

1. Clone the repository:

```shell
git clone <repository-url>

cd blogging_system

create an env from the .env.sample

npm install

npm run dev

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

enjoy

```
