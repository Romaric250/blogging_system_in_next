
import prisma from "@/utils/connect";
import { NextResponse } from "next/server";


export const PUT = async (req) => {
  const commentId = req.query.commentId;
  const body = JSON.parse(req.body);

  try {
    const updatedComment = await prisma.comment.update({
      where: {id: commentId},
      data: body,
    });

    return new NextResponse(JSON.stringify(updatedComment, { status: 200 }));
  } catch (err) {
    return new NextResponse(
      JSON.stringify({ message: "Something went wrong!" }, { status: 500 })
    );
  }
};


export const DELETE = async (req) => {
  const commentId = req.query.commentId;

  try {
    await prisma.comment.delete({
      where: { id: commentId },
    });

    return new NextResponse(JSON.stringify({ message: "Comment deleted successfully" }, { status: 200 }));
  } catch (err) {
    return new NextResponse(
      JSON.stringify({ message: "Something went wrong!" }, { status: 500 })
    );
  }
};