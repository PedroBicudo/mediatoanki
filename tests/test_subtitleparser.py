from datetime import timedelta
from re import sub
from src.model.subtitle_formats.Vtt import Vtt
from src.model.subtitle_formats.Srt import Srt
from src.SubtitleParser import SubtitleParser
import unittest

class SubtitleParserTestCase(unittest.TestCase):
    
    def test_get_file_format(self):
        srt = SubtitleParser._get_file_format("subtitle.vtt.srt")
        vtt = SubtitleParser._get_file_format("subtitle.srt.vtt")
        vtt_blank = SubtitleParser._get_file_format("subtitle.vtt.")
        srt_blank = SubtitleParser._get_file_format("subtitle.srt.")

        self.assertEqual(
            srt,
            "srt", 
            "Teste: format(subtitle.vtt.srt) =="
        )

        self.assertNotEqual(
            srt_blank, 
            "srt",
            "Teste: subtitle.srt. != srt"
        )
        
        self.assertEqual(
            vtt, 
            "vtt",
            "Teste: format(subtitle.srt.vtt) == vtt"
        )
        
        self.assertNotEqual(
            vtt_blank, 
            "vtt",
            "Teste: subtitle.vtt. != vtt"
        )

    def test_has_hour_field(self):
        time_minute: str = "00:00"
        time_minute_milliseconds: str = "00:00.000"
        time_hour: str = "00:00:00"
        time_hour_milliseconds: str = "00:00:00.000"

        self.assertEqual(
            SubtitleParser._has_hour_field(time_minute),
            False,
            "Teste: 00:00 has hour field? False"
        )

        self.assertEqual(
            SubtitleParser._has_hour_field(time_minute_milliseconds),
            False,
            "Teste: 00:00.000 has hour field? False"
        )

        self.assertEqual(
            SubtitleParser._has_hour_field(time_hour),
            True,
            "Teste: 00:00:00 has hour field? True"
        )

        self.assertEqual(
            SubtitleParser._has_hour_field(time_hour_milliseconds),
            True,
            "Teste: 00:00:00.000 has hour field? True"
        )
    
    def test_get_regex_based_on_file_format(self):
        sub_parser = SubtitleParser()
        non_existent = "abcdefgh"
        srt = "srt"
        vtt = "vtt"

        self.assertEqual(
            sub_parser._get_regex_based_on_file_format(srt),
            Srt,
            "Teste: regex class of srt == Srt"
        )

        self.assertEqual(
            sub_parser._get_regex_based_on_file_format(vtt),
            Vtt,
            "Teste: regex class of vtt == Vtt"
        )

        with self.assertRaises(NotImplementedError, msg="Teste: formato non_existent raises NotImplementedError"):
            sub_parser._get_regex_based_on_file_format(non_existent),

    def test_is_not_blank_line(self):
        content_list_empty = []
        content_list_not_empty = ["a"]
        content_str_empty = ""
        content_str_not_empty = "a"

        self.assertEqual(
            SubtitleParser._is_not_empty(content_list_empty),
            False,
            "Teste: empty_list = [] == False"
        )

        self.assertEqual(
            SubtitleParser._is_not_empty(content_list_not_empty),
            True,
            "Teste: not_empty_list = [\" a \"] == False"
        )

        self.assertEqual(
            SubtitleParser._is_not_empty(content_str_empty),
            False,
            "Teste: \"\" is empty."
        )

        self.assertEqual(
            SubtitleParser._is_not_empty(content_str_not_empty),
            True,
            "Teste: \"a\" is not empty"
        )

    def test_convert_time_text_to_timedelta_with_vtt_format(self):
        vtt = Vtt

        time_vtt_timedelta = timedelta(hours=0.0, minutes=3.0, seconds=33.0, milliseconds=123)
        time_vtt_test = "00:03:33.123"
        timedelta_time_vtt_test = SubtitleParser.convert_time_text_to_timedelta(
            time_vtt_test, vtt
        )
        self.assertEqual(
            time_vtt_timedelta, timedelta_time_vtt_test,
            msg=f"Vtt: {time_vtt_timedelta} == {time_vtt_test}"
        )


        time_vtt_nohour__timedelta = timedelta(hours=0.0, minutes=1.0, seconds=59.)
        time_vtt_nohour_format = "01:59.000"
        timedelta_time_vtt_nohour_format = SubtitleParser.convert_time_text_to_timedelta(
            time_vtt_nohour_format, vtt
        )
        self.assertEqual(
            time_vtt_nohour__timedelta, timedelta_time_vtt_nohour_format,
            msg=f"Vtt: {time_vtt_nohour__timedelta} == {timedelta_time_vtt_nohour_format}"
        )


        time_vtt_nohour_nomilliseconds_timedelta = timedelta(hours=0.0, minutes=3.0, seconds=3.0)
        time_vtt_nohour_nomilliseconds_format = "03:03"
        timedelta_time_vtt_nomilliseconds_format = SubtitleParser.convert_time_text_to_timedelta(
            time_vtt_nohour_nomilliseconds_format, vtt
        )
        self.assertEqual(
            time_vtt_nohour_nomilliseconds_timedelta, timedelta_time_vtt_nomilliseconds_format,
            msg=f"Vtt: {time_vtt_nohour__timedelta} == {timedelta_time_vtt_nohour_format}"
        )

    def test_convert_time_text_to_timedelta_with_srt_format(self):
        srt = Srt

        time_srt_timedelta = timedelta(hours=0.0, minutes=3.0, seconds=33.0, milliseconds=123)
        time_srt_test = "00:03:33,123"
        timedelta_time_srt_test = SubtitleParser.convert_time_text_to_timedelta(
            time_srt_test, srt
        )
        self.assertEqual(
            time_srt_timedelta, timedelta_time_srt_test,
            msg=f"Srt: {time_srt_timedelta} == {time_srt_test}"
        )


        time_srt_nohour__timedelta = timedelta(hours=0.0, minutes=1.0, seconds=59.0)
        time_srt_nohour_format = "01:59,000"
        timedelta_time_srt_nohour_format = SubtitleParser.convert_time_text_to_timedelta(
            time_srt_nohour_format, srt
        )
        self.assertEqual(
            time_srt_nohour__timedelta, timedelta_time_srt_nohour_format,
            msg=f"Srt: {time_srt_nohour__timedelta} == {timedelta_time_srt_nohour_format}"
        )


        time_srt_nohour_nomilliseconds_timedelta = timedelta(hours=0.0, minutes=3.0, seconds=3.0)
        time_srt_nohour_nomilliseconds_format = "03:03"
        timedelta_time_srt_nomilliseconds_format = SubtitleParser.convert_time_text_to_timedelta(
            time_srt_nohour_nomilliseconds_format, srt
        )
        self.assertEqual(
            time_srt_nohour_nomilliseconds_timedelta, timedelta_time_srt_nomilliseconds_format,
            msg=f"Srt: {time_srt_nohour__timedelta} == {timedelta_time_srt_nomilliseconds_format}"
        )

    def test_get_text_from_scene(self):
        """ Teste de obtencao de texto da cena.

            Para extrair o texto de uma cena especifica,
            o algoritmo vai ler as linhas ate encontrar uma 
            linha em branco ou chegar no final do arquivo.

            Exemplo:

                Valido:

                    00:00:00.000 -> 00:00:00.000
                    text
                    [space]

                Invalido:
                    00:00:00.000 -> 00:00:00.000
                    text
                    00:00:00.000 -> 00:00:00.000
                    text
                
                Invalido:

                    00:00:00.000 -> 00:00:00.000
                    [space]
                    text
                    00:00:00.000 -> 00:00:00.000
                    [space]
                    text

                Invalido:

                    00:00:00.000 -> 00:00:00.000
                    text
                    [space]
                    text
                    00:00:00.000 -> 00:00:00.000
                    text
                    [space]
                    text

        """
        sub_parser = SubtitleParser()

        # Teste 0 linhas: ()
        file_lines_empty = []
        correct_empty_text = ""
        result_empty_text = sub_parser._get_text_from_scene(file_lines_empty)
        self.assertEqual(
            result_empty_text,
            correct_empty_text,
            msg="text from scene: [] should return \"\" "
        )

        # Teste 1 linha: (space)
        file_lines_one_space = [""]
        correct_one_space = ""
        result_one_space = sub_parser._get_text_from_scene(file_lines_one_space)
        self.assertEqual(
            result_one_space,
            correct_one_space,
            msg="text from scene: [\"\"] should return \"\""
        )

        # Teste 1 linha: (text)
        file_lines_one_text = ["text"]
        correct_one_text = "text"
        result_one_text = sub_parser._get_text_from_scene(file_lines_one_text)
        self.assertEqual(
            result_one_text,
            correct_one_text,
            msg="text from scene: [\"text\"] should return \"text\""
        )

        # Teste 2 linhas: (text, space)
        file_lines_two_text_space = ["text", ""]
        correct_two_text_space = "text"
        result_two_text_space = sub_parser._get_text_from_scene(file_lines_two_text_space)
        self.assertEqual(
            result_two_text_space,
            correct_two_text_space,
            msg="text from scene: [\"text\", \"\"] should return \"text\""
        )

        # Teste 2 linhas: (space, text)
        file_lines_two_space_text = ["", "text"]
        correct_two_space_text = ""
        result_two_space_text = sub_parser._get_text_from_scene(file_lines_two_space_text)
        self.assertEqual(
            result_two_space_text,
            correct_two_space_text,
            msg="text from scene: [\"\", \"text\"] should return \"\""
        )        

        # Teste 3 linhas: (text, space, text)
        file_lines_three_text_space_text = ["text", "", "text"]
        correct_three_text_space_text = "text"
        result_three_text_space_text = sub_parser._get_text_from_scene(file_lines_three_text_space_text)
        self.assertEqual(
            result_three_text_space_text,
            correct_three_text_space_text,
            msg="text from scene: [\"\", \"text\"] should return \"\""
        )

if __name__ == '__main__':
    unittest.main()
