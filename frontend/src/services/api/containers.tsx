import { ContainerSchema } from "@/modules/containers/model";
import { apiClient } from "./client";

export async function fetchContainers(): Promise<ContainerSchema[]> {
    const res = await apiClient.get("/containers/");
    console.log("Reeees", res)
    return res.data.containers;
  }
