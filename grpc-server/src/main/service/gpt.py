import os
import openai
from proto import server_pb2_grpc
from proto import server_pb2
from google.protobuf import wrappers_pb2


class GPTService(server_pb2_grpc.NlpServerServicer):
    def __init__(self) -> None:
        openai.api_key = os.getenv("GPT_KEY")

    def CorrectGrammar(self, request, context) -> server_pb2.CorrectGrammarResponse:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Correct this to standard English:\n{request.transcript}",
            temperature=0,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        choices = response.get("choices")
        if choices is not None and len(choices) > 0:
            recommend_corrected = choices[0].text
        else:
            recommend_corrected = ""
        res = server_pb2.CorrectGrammarResponse(
            correctTranscript=recommend_corrected,
            type="1",
            message=wrappers_pb2.StringValue(value="success"),
        )
        return res
