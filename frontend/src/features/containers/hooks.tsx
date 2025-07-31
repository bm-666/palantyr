"use client"
import { fetchContainers } from "@/services/api/containers";
import { useQuery } from "@tanstack/react-query";

export function useContainers() {
    return useQuery(
        {
            queryKey: ["containers"],
            queryFn: fetchContainers,
            refetchInterval: 5000
        }
    );
}