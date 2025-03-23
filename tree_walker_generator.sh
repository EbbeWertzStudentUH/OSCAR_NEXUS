grammarinator-process QueryLanguageLexer.g4 QueryLanguageParser.g4 -o grammarinator/fuzzer/
grammarinator-generate QueryLanguageGenerator.QueryLanguageGenerator -r query -d 20 -o grammarinator/tests/test_%d.nql -n 100 -s grammarinator.runtime.simple_space_serializer --sys-path grammarinator/fuzzer/
echo "done"
read -p "Press enter to continue"