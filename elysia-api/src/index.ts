import { Elysia, t } from "elysia";

function calculateBMI(weight: number, tall: number): number {
  // tall is in cm, so divide by 100 to convert to meters
  return weight / Math.pow(tall / 100.0, 2);
}

const app = new Elysia()
  .model({
    BmiData: t.Object({
      weight: t.Number(),
      tall: t.Number(),
    }),
    BmiResponse: t.Object({
      username: t.String(),
      bmi: t.Number(),
    }),
  })
  .post("/bmi/:username", ({ body, params }) => {
    const bmi = calculateBMI(body.weight, body.tall);

    return {
      username: params.username,
      bmi,
    };
  }, {
    body: "BmiData",
    response: "BmiResponse",
  })
  .listen(3000);

console.log(
  `Elysia is running at http://${app.server?.hostname}:${app.server?.port}`
);
