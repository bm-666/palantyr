export function IconButton({
  children,
  title,
  onClick,
  disabled,
}: {
  children: React.ReactNode;
  title?: string;
  onClick?: () => void;
  disabled?: boolean;
}) {
  return (
    <button
      type="button"
      title={title}
      onClick={disabled ? undefined : onClick}
      disabled={disabled}
      className={`
        w-8 h-8
        flex items-center justify-center
        rounded
        hover:bg-gray-100
        active:bg-gray-200
        active:scale-95
        transition
        ${disabled
          ? "opacity-30 cursor-not-allowed"
          : "hover:bg-gray-100 active:bg-gray-200 active:scale-95"}
      `}
    >
      {children}
    </button>
  );
}
