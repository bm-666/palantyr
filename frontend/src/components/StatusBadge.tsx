import { ContainerStatusEnum } from "@/modules/containers/model";

export function StatusBadge({status}: {status: ContainerStatusEnum}){
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
}