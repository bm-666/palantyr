import { ContainerSchema } from "@/modules/containers/model";
import { apiClient } from "./client";

export async function fetchContainers(): Promise<ContainerSchema[]> {
    const res = await apiClient.get("/containers");
    return res.data.containers;
  }
