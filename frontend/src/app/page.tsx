"use client"
import { ContainerCard } from "@/components/ContainerCard";
import { useContainers } from "@/features/containers/hooks";

export default function ContainersPage() {
  const { data: containers, isLoading } = useContainers();

  if (isLoading) return <p>Loading containers...</p>;

  return (
    <div className="p-6 space-y-4">
      <h1 className="text-2xl font-bold">Docker Containers</h1>
      {containers?.map((c) => (
        <ContainerCard key={c.containerId} container={c} />
      ))}
    </div>
  );
}