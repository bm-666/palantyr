import { ContainerStatusEnum } from "@/modules/containers/model";

/**export function StatusBadge({status}: {status: ContainerStatusEnum}){
    const colorMap: Record<ContainerStatusEnum, string> = {
        running: "bg-green-500",
        exited: "bg-red-500",
        paused: "bg-yellow-500",
        restarting: "bg-orange-500",
        dead: "bg-gray-500",
  };
  return (
    <span className={`px-3 py-1 rounded text-white ${colorMap[status]}`}>
        {status}
    </span>
  );
} **/
// StatusBadge.tsx
// StatusBadge.tsx
export function StatusBadge({ status }: { status: string }) {
  const color = {
    running: "bg-green-500",
    stopped: "bg-red-500",
    restarting: "bg-yellow-400",
    unhealthy: "bg-orange-500",
  }[status] || "bg-gray-400";

  return (
    <span
      className={`w-3 h-3 rounded-full ${color}`}
      title={status}   // текст только при ховере
    />
  );
}

