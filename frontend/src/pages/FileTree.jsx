export default function FileTree({ files, setFiles, activeFile, setActiveFile }) {
  const handleNewFile = () => {
    const newFile = {
      id: Date.now(),
      name: `new_file_${files.length + 1}.py`,
      content: "",
    };
    setFiles([...files, newFile]);
    setActiveFile(newFile); // immediately make it active
  };

  return (
    <div className="file-tree">
      <button onClick={handleNewFile}>+ New File</button>
      <ul>
        {files.map(file => (
          <li
            key={file.id}
            className={activeFile?.id === file.id ? "active-file" : ""}
            onClick={() => setActiveFile(file)}
          >
            {file.name}
          </li>
        ))}
      </ul>
    </div>
  );
}
