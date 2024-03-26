import prisma from "../../utils/connect"
import { NextResponse } from "next/server";


export const POST = async (req) => {
  const { slug, title, img } = JSON.parse(req.body);

  try {
    const newCategory = await prisma.category.create({
      data: {
        slug,
        title,
        img,
      },
    });

    return new NextResponse(JSON.stringify(newCategory, { status: 201 }));
  } catch (err) {
    console.log(err);
    return new NextResponse(
      JSON.stringify({ message: "Something went wrong!" }, { status: 500 })
    );
  }
};


export const GET = async () => {
  try {
    const categories = await prisma.category.findMany();

    return new NextResponse(JSON.stringify(categories, { status: 200 }));
  } catch (err) {
    console.log(err);
    return new NextResponse(
      JSON.stringify({ message: "Something went wrong!" }, { status: 500 })
    );
  }
};