import { ContainerSchema } from "@/modules/containers/model";
import { apiClient } from "./client";
import { ContainerAction } from "@/types/container-actions";

export async function fetchContainers(): Promise<ContainerSchema[]> {
    const res = await apiClient.get("/containers/");
    console.log("Reeees", res)
    return res.data.containers;
  }

export async function containerAction(
  
  containerId: string,
  action: ContainerAction
) {
  console.log("Test --->>")
  const res = await fetch(
    `http://localhost:8001/containers/${containerId}/action`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({action})
    }

  );
  if (!res.ok) {
    throw new Error("Failed to perform container action ")
  }
}