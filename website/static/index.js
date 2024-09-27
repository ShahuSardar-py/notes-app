function deleteNote(noteID) {
    fetch('/delete-note', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ noteID: noteID }),  // Ensure this matches the parameter name
    }).then((_res) => {
        window.location.href = "/";  // Redirect after deletion
    });
}