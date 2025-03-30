grammarinator-process NexQLLexer.g4 NexQLParser.g4 -o grammarinator
grammarinator-generate NexQLGenerator.NexQLGenerator -r discovery_clause -d 50 -o grammarinator/tests/test_%d.nql -n 100 -s grammarinator.runtime.simple_space_serializer --sys-path grammarinator/
echo "done"
read -p "Press enter to continue"