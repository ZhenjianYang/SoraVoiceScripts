from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 调试地图

    CreateScenaFile(
        FileName            = 'T0001_2 ._SN',
        MapName             = 'map',
        Location            = 'T0001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 1,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 2,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_16D",          # 01, 1
        "Function_2_2A3",          # 02, 2
        "Function_3_34B",          # 03, 3
        "Function_4_44E",          # 04, 4
        "Function_5_53D",          # 05, 5
        "Function_6_61F",          # 06, 6
        "Function_7_743",          # 07, 7
        "Function_8_825",          # 08, 8
        "Function_9_907",          # 09, 9
        "Function_10_AAC",         # 0A, 10
        "Function_11_B92",         # 0B, 11
        "Function_12_C74",         # 0C, 12
        "Function_13_D56",         # 0D, 13
        "Function_14_E38",         # 0E, 14
        "Function_15_F1A",         # 0F, 15
        "Function_16_FFC",         # 10, 16
        "Function_17_10DE",        # 11, 17
        "Function_18_11C0",        # 12, 18
        "Function_19_12A6",        # 13, 19
        "Function_20_1388",        # 14, 20
        "Function_21_151F",        # 15, 21
        "Function_22_1601",        # 16, 22
        "Function_23_1764",        # 17, 23
        "Function_24_1909",        # 18, 24
        "Function_25_19EB",        # 19, 25
        "Function_26_1ACD",        # 1A, 26
        "Function_27_1BC7",        # 1B, 27
        "Function_28_1CF8",        # 1C, 28
        "Function_29_1DDA",        # 1D, 29
        "Function_30_1F17",        # 1E, 30
        "Function_31_1FF9",        # 1F, 31
        "Function_32_216C",        # 20, 32
        "Function_33_224E",        # 21, 33
        "Function_34_2330",        # 22, 34
        "Function_35_2439",        # 23, 35
        "Function_36_2599",        # 24, 36
        "Function_37_267B",        # 25, 37
        "Function_38_27D1",        # 26, 38
        "Function_39_2944",        # 27, 39
        "Function_40_2A26",        # 28, 40
        "Function_41_2B08",        # 29, 41
        "Function_42_2BEA",        # 2A, 42
        "Function_43_2CCC",        # 2B, 43
        "Function_44_2DAE",        # 2C, 44
        "Function_45_2EAB",        # 2D, 45
        "Function_46_2F8B",        # 2E, 46
        "Function_47_306D",        # 2F, 47
        "Function_48_32F8",        # 30, 48
    )


    def Function_0_AA(): pass

    label("Function_0_AA")


    AnonymousTalk(    #0
        "\x06Select a section.\x02",
    )


    label("loc_BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Rolent\x01",       # 0
            "Bose\x01",         # 1
            "Ruan\x01",         # 2
            "Zeiss\x01",        # 3
            "Grancel\x01",      # 4
            "Others\x01",       # 5
            "Cancel\x01",       # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_126"),
        (1, "loc_12D"),
        (2, "loc_134"),
        (3, "loc_13B"),
        (4, "loc_142"),
        (5, "loc_149"),
        (SWITCH_DEFAULT, "loc_150"),
    )


    label("loc_126")

    Call(2, 1)
    Jump("loc_15A")

    label("loc_12D")

    Call(2, 9)
    Jump("loc_15A")

    label("loc_134")

    Call(2, 20)
    Jump("loc_15A")

    label("loc_13B")

    Call(2, 27)
    Jump("loc_15A")

    label("loc_142")

    Call(2, 35)
    Jump("loc_15A")

    label("loc_149")

    Call(2, 46)
    Jump("loc_15A")

    label("loc_150")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15A")

    Jump("loc_BF")

    label("loc_15D")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_AA end

    def Function_1_16D(): pass

    label("Function_1_16D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_295")

    AnonymousTalk(    #1
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "Malga Mine\x01",               # 0
            "Mistwald\x01",                 # 1
            "Tower\x01",                    # 2
            "Elize Highway\x01",            # 3
            "Milch Main Road\x01",          # 4
            "Malga Trail\x01",              # 5
            "Sewers\x01",                   # 6
            "Perzel Farm (Night)\x01",      # 7
            "Verte Bridge\x01",             # 8
            "Cancel\x01",                   # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_237"),
        (1, "loc_23E"),
        (2, "loc_245"),
        (3, "loc_24C"),
        (4, "loc_253"),
        (5, "loc_25A"),
        (6, "loc_261"),
        (7, "loc_268"),
        (8, "loc_278"),
        (SWITCH_DEFAULT, "loc_288"),
    )


    label("loc_237")

    Call(2, 2)
    Jump("loc_292")

    label("loc_23E")

    Call(2, 3)
    Jump("loc_292")

    label("loc_245")

    Call(2, 4)
    Jump("loc_292")

    label("loc_24C")

    Call(2, 5)
    Jump("loc_292")

    label("loc_253")

    Call(2, 6)
    Jump("loc_292")

    label("loc_25A")

    Call(2, 7)
    Jump("loc_292")

    label("loc_261")

    Call(2, 8)
    Jump("loc_292")

    label("loc_268")

    Battle(0x393, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_292")

    label("loc_278")

    Battle(0x3ED, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_292")

    label("loc_288")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_292")

    Jump("Function_1_16D")

    label("loc_295")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_16D end

    def Function_2_2A3(): pass

    label("Function_2_2A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33D")

    AnonymousTalk(    #2
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0100_01\x01",      # 0
            "C0100_02\x01",      # 1
            "C0100_03\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_300"),
        (1, "loc_310"),
        (2, "loc_320"),
        (SWITCH_DEFAULT, "loc_330"),
    )


    label("loc_300")

    Battle(0x56, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_33A")

    label("loc_310")

    Battle(0x57, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_33A")

    label("loc_320")

    Battle(0x58, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_33A")

    label("loc_330")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_33A")

    Jump("Function_2_2A3")

    label("loc_33D")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_2A3 end

    def Function_3_34B(): pass

    label("Function_3_34B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_440")

    AnonymousTalk(    #3
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0100_01\x01",          # 0
            "C0100_02\x01",          # 1
            "C0100_03\x01",          # 2
            "C0100_20\x01",          # 3
            "C0100_11\x01",          # 4
            "BTL_EVENT001\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3D3"),
        (1, "loc_3E3"),
        (2, "loc_3F3"),
        (3, "loc_403"),
        (4, "loc_413"),
        (5, "loc_423"),
        (SWITCH_DEFAULT, "loc_433"),
    )


    label("loc_3D3")

    Battle(0x3E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_43D")

    label("loc_3E3")

    Battle(0x3F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_43D")

    label("loc_3F3")

    Battle(0x40, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_43D")

    label("loc_403")

    Battle(0x51, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_43D")

    label("loc_413")

    Battle(0x48, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_43D")

    label("loc_423")

    Battle(0x385, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_43D")

    label("loc_433")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_43D")

    Jump("Function_3_34B")

    label("loc_440")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_34B end

    def Function_4_44E(): pass

    label("Function_4_44E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52F")

    AnonymousTalk(    #4
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0400_01\x01",          # 0
            "C0400_02\x01",          # 1
            "C0400_07\x01",          # 2
            "C0400_13\x01",          # 3
            "C0400_10\x01",          # 4
            "BTL_EVENT002\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4D2"),
        (1, "loc_4E2"),
        (2, "loc_4F2"),
        (3, "loc_502"),
        (4, "loc_512"),
        (SWITCH_DEFAULT, "loc_522"),
    )


    label("loc_4D2")

    Battle(0x31, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_52C")

    label("loc_4E2")

    Battle(0x32, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_52C")

    label("loc_4F2")

    Battle(0x37, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_52C")

    label("loc_502")

    Battle(0x3D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_52C")

    label("loc_512")

    Battle(0x3A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_52C")

    label("loc_522")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52C")

    Jump("Function_4_44E")

    label("loc_52F")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_44E end

    def Function_5_53D(): pass

    label("Function_5_53D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_611")

    AnonymousTalk(    #5
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R0100_02\x01",      # 0
            "R0100_05\x01",      # 1
            "R0100_09\x01",      # 2
            "R0100_11\x01",      # 3
            "R0100_14\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5B4"),
        (1, "loc_5C4"),
        (2, "loc_5D4"),
        (3, "loc_5E4"),
        (4, "loc_5F4"),
        (SWITCH_DEFAULT, "loc_604"),
    )


    label("loc_5B4")

    Battle(0x15, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_60E")

    label("loc_5C4")

    Battle(0x18, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_60E")

    label("loc_5D4")

    Battle(0x1C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_60E")

    label("loc_5E4")

    Battle(0x1E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_60E")

    label("loc_5F4")

    Battle(0x21, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_60E")

    label("loc_604")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_60E")

    Jump("Function_5_53D")

    label("loc_611")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_53D end

    def Function_6_61F(): pass

    label("Function_6_61F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_735")

    AnonymousTalk(    #6
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R0200_02\x01",          # 0
            "R0200_06\x01",          # 1
            "R0200_09\x01",          # 2
            "R0200_11\x01",          # 3
            "R0200_17\x01",          # 4
            "BTL_QUEST003\x01",      # 5
            "BTL_QUEST004\x01",      # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6B8"),
        (1, "loc_6C8"),
        (2, "loc_6D8"),
        (3, "loc_6E8"),
        (4, "loc_6F8"),
        (5, "loc_708"),
        (6, "loc_718"),
        (SWITCH_DEFAULT, "loc_728"),
    )


    label("loc_6B8")

    Battle(0x7A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_732")

    label("loc_6C8")

    Battle(0x7E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_732")

    label("loc_6D8")

    Battle(0x81, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_732")

    label("loc_6E8")

    Battle(0x83, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_732")

    label("loc_6F8")

    Battle(0x89, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_732")

    label("loc_708")

    Battle(0x3EB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_732")

    label("loc_718")

    Battle(0x3EC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_732")

    label("loc_728")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_732")

    Jump("Function_6_61F")

    label("loc_735")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_61F end

    def Function_7_743(): pass

    label("Function_7_743")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_817")

    AnonymousTalk(    #7
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R0300_02\x01",      # 0
            "R0300_06\x01",      # 1
            "R0300_09\x01",      # 2
            "R0300_12\x01",      # 3
            "R0300_17\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7BA"),
        (1, "loc_7CA"),
        (2, "loc_7DA"),
        (3, "loc_7EA"),
        (4, "loc_7FA"),
        (SWITCH_DEFAULT, "loc_80A"),
    )


    label("loc_7BA")

    Battle(0x65, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_7CA")

    Battle(0x69, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_7DA")

    Battle(0x6C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_7EA")

    Battle(0x6F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_7FA")

    Battle(0x74, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_814")

    label("loc_80A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_814")

    Jump("Function_7_743")

    label("loc_817")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_743 end

    def Function_8_825(): pass

    label("Function_8_825")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F9")

    AnonymousTalk(    #8
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C0500_01\x01",      # 0
            "C0500_02\x01",      # 1
            "C0500_03\x01",      # 2
            "C0500_04\x01",      # 3
            "C0500_07\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_89C"),
        (1, "loc_8AC"),
        (2, "loc_8BC"),
        (3, "loc_8CC"),
        (4, "loc_8DC"),
        (SWITCH_DEFAULT, "loc_8EC"),
    )


    label("loc_89C")

    Battle(0x2A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_8F6")

    label("loc_8AC")

    Battle(0x2B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_8F6")

    label("loc_8BC")

    Battle(0x2C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_8F6")

    label("loc_8CC")

    Battle(0x2D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_8F6")

    label("loc_8DC")

    Battle(0x30, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_8F6")

    label("loc_8EC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8F6")

    Jump("Function_8_825")

    label("loc_8F9")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_825 end

    def Function_9_907(): pass

    label("Function_9_907")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A9E")

    AnonymousTalk(    #9
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        60,
        1,
        (
            "Tower\x01",                  # 0
            "Fort\x01",                   # 1
            "Canyon\x01",                 # 2
            "Krone Pass\x01",             # 3
            "East Bose Highway\x01",      # 4
            "West Bose Highway\x01",      # 5
            "Eisen Road\x01",             # 6
            "New Ansel Path\x01",         # 7
            "Ravennue Trail\x01",         # 8
            "Ravennue Mine\x01",          # 9
            "Ravennue Square\x01",        # 10
            "Forbidden City\x01",         # 11
            "Krone Exterior\x01",         # 12
            "Cancel\x01",                 # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A1B"),
        (1, "loc_A22"),
        (2, "loc_A29"),
        (3, "loc_A30"),
        (4, "loc_A37"),
        (5, "loc_A3E"),
        (6, "loc_A45"),
        (7, "loc_A4C"),
        (8, "loc_A53"),
        (9, "loc_A5A"),
        (10, "loc_A61"),
        (11, "loc_A71"),
        (12, "loc_A81"),
        (SWITCH_DEFAULT, "loc_A91"),
    )


    label("loc_A1B")

    Call(2, 10)
    Jump("loc_A9B")

    label("loc_A22")

    Call(2, 11)
    Jump("loc_A9B")

    label("loc_A29")

    Call(2, 12)
    Jump("loc_A9B")

    label("loc_A30")

    Call(2, 13)
    Jump("loc_A9B")

    label("loc_A37")

    Call(2, 14)
    Jump("loc_A9B")

    label("loc_A3E")

    Call(2, 15)
    Jump("loc_A9B")

    label("loc_A45")

    Call(2, 16)
    Jump("loc_A9B")

    label("loc_A4C")

    Call(2, 17)
    Jump("loc_A9B")

    label("loc_A53")

    Call(2, 18)
    Jump("loc_A9B")

    label("loc_A5A")

    Call(2, 19)
    Jump("loc_A9B")

    label("loc_A61")

    Battle(0x387, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_A9B")

    label("loc_A71")

    Battle(0x389, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_A9B")

    label("loc_A81")

    Battle(0x396, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_A9B")

    label("loc_A91")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A9B")

    Jump("Function_9_907")

    label("loc_A9E")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_907 end

    def Function_10_AAC(): pass

    label("Function_10_AAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B84")

    AnonymousTalk(    #10
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1211_01\x01",          # 0
            "C1211_02\x01",          # 1
            "C1211_03\x01",          # 2
            "C1211_04\x01",          # 3
            "BTL_QUEST007\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B27"),
        (1, "loc_B37"),
        (2, "loc_B47"),
        (3, "loc_B57"),
        (4, "loc_B67"),
        (SWITCH_DEFAULT, "loc_B77"),
    )


    label("loc_B27")

    Battle(0x8E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B81")

    label("loc_B37")

    Battle(0x8F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B81")

    label("loc_B47")

    Battle(0x90, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B81")

    label("loc_B57")

    Battle(0x91, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B81")

    label("loc_B67")

    Battle(0x3EF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_B81")

    label("loc_B77")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B81")

    Jump("Function_10_AAC")

    label("loc_B84")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_10_AAC end

    def Function_11_B92(): pass

    label("Function_11_B92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C66")

    AnonymousTalk(    #11
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1300_01\x01",      # 0
            "C1300_02\x01",      # 1
            "C1300_03\x01",      # 2
            "C1300_04\x01",      # 3
            "C1300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C09"),
        (1, "loc_C19"),
        (2, "loc_C29"),
        (3, "loc_C39"),
        (4, "loc_C49"),
        (SWITCH_DEFAULT, "loc_C59"),
    )


    label("loc_C09")

    Battle(0xA1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_C63")

    label("loc_C19")

    Battle(0xA2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_C63")

    label("loc_C29")

    Battle(0xA3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_C63")

    label("loc_C39")

    Battle(0xA4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_C63")

    label("loc_C49")

    Battle(0xA5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_C63")

    label("loc_C59")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C63")

    Jump("Function_11_B92")

    label("loc_C66")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_11_B92 end

    def Function_12_C74(): pass

    label("Function_12_C74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D48")

    AnonymousTalk(    #12
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1400_01\x01",      # 0
            "C1400_02\x01",      # 1
            "C1400_03\x01",      # 2
            "C1400_04\x01",      # 3
            "C1400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CEB"),
        (1, "loc_CFB"),
        (2, "loc_D0B"),
        (3, "loc_D1B"),
        (4, "loc_D2B"),
        (SWITCH_DEFAULT, "loc_D3B"),
    )


    label("loc_CEB")

    Battle(0xB5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D45")

    label("loc_CFB")

    Battle(0xB6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D45")

    label("loc_D0B")

    Battle(0xB7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D45")

    label("loc_D1B")

    Battle(0xB8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D45")

    label("loc_D2B")

    Battle(0xB9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_D45")

    label("loc_D3B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D45")

    Jump("Function_12_C74")

    label("loc_D48")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_C74 end

    def Function_13_D56(): pass

    label("Function_13_D56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E2A")

    AnonymousTalk(    #13
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1500_01\x01",      # 0
            "C1500_02\x01",      # 1
            "C1500_03\x01",      # 2
            "C1500_04\x01",      # 3
            "C1500_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DCD"),
        (1, "loc_DDD"),
        (2, "loc_DED"),
        (3, "loc_DFD"),
        (4, "loc_E0D"),
        (SWITCH_DEFAULT, "loc_E1D"),
    )


    label("loc_DCD")

    Battle(0xC9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E27")

    label("loc_DDD")

    Battle(0xCA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E27")

    label("loc_DED")

    Battle(0xCB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E27")

    label("loc_DFD")

    Battle(0xCC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E27")

    label("loc_E0D")

    Battle(0xCD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_E27")

    label("loc_E1D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E27")

    Jump("Function_13_D56")

    label("loc_E2A")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_D56 end

    def Function_14_E38(): pass

    label("Function_14_E38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F0C")

    AnonymousTalk(    #14
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1100_01\x01",      # 0
            "R1100_02\x01",      # 1
            "R1100_20\x01",      # 2
            "R1100_04\x01",      # 3
            "R1100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EAF"),
        (1, "loc_EBF"),
        (2, "loc_ECF"),
        (3, "loc_EDF"),
        (4, "loc_EEF"),
        (SWITCH_DEFAULT, "loc_EFF"),
    )


    label("loc_EAF")

    Battle(0xDD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F09")

    label("loc_EBF")

    Battle(0xDE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F09")

    label("loc_ECF")

    Battle(0xF0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F09")

    label("loc_EDF")

    Battle(0xE0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F09")

    label("loc_EEF")

    Battle(0xE1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_F09")

    label("loc_EFF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F09")

    Jump("Function_14_E38")

    label("loc_F0C")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_14_E38 end

    def Function_15_F1A(): pass

    label("Function_15_F1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FEE")

    AnonymousTalk(    #15
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1200_01\x01",      # 0
            "R1200_02\x01",      # 1
            "R1200_03\x01",      # 2
            "R1200_04\x01",      # 3
            "R1200_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F91"),
        (1, "loc_FA1"),
        (2, "loc_FB1"),
        (3, "loc_FC1"),
        (4, "loc_FD1"),
        (SWITCH_DEFAULT, "loc_FE1"),
    )


    label("loc_F91")

    Battle(0xF1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_FEB")

    label("loc_FA1")

    Battle(0xF2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_FEB")

    label("loc_FB1")

    Battle(0xF3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_FEB")

    label("loc_FC1")

    Battle(0xF4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_FEB")

    label("loc_FD1")

    Battle(0xF5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_FEB")

    label("loc_FE1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FEB")

    Jump("Function_15_F1A")

    label("loc_FEE")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_15_F1A end

    def Function_16_FFC(): pass

    label("Function_16_FFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D0")

    AnonymousTalk(    #16
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1300_01\x01",      # 0
            "R1300_02\x01",      # 1
            "R1300_03\x01",      # 2
            "R1300_04\x01",      # 3
            "R1300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1073"),
        (1, "loc_1083"),
        (2, "loc_1093"),
        (3, "loc_10A3"),
        (4, "loc_10B3"),
        (SWITCH_DEFAULT, "loc_10C3"),
    )


    label("loc_1073")

    Battle(0x105, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10CD")

    label("loc_1083")

    Battle(0x106, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10CD")

    label("loc_1093")

    Battle(0x107, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10CD")

    label("loc_10A3")

    Battle(0x108, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10CD")

    label("loc_10B3")

    Battle(0x109, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_10CD")

    label("loc_10C3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10CD")

    Jump("Function_16_FFC")

    label("loc_10D0")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_16_FFC end

    def Function_17_10DE(): pass

    label("Function_17_10DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B2")

    AnonymousTalk(    #17
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1400_01\x01",      # 0
            "R1400_02\x01",      # 1
            "R1400_03\x01",      # 2
            "R1400_04\x01",      # 3
            "R1400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1155"),
        (1, "loc_1165"),
        (2, "loc_1175"),
        (3, "loc_1185"),
        (4, "loc_1195"),
        (SWITCH_DEFAULT, "loc_11A5"),
    )


    label("loc_1155")

    Battle(0x119, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11AF")

    label("loc_1165")

    Battle(0x11A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11AF")

    label("loc_1175")

    Battle(0x11B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11AF")

    label("loc_1185")

    Battle(0x11C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11AF")

    label("loc_1195")

    Battle(0x11D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_11AF")

    label("loc_11A5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11AF")

    Jump("Function_17_10DE")

    label("loc_11B2")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_10DE end

    def Function_18_11C0(): pass

    label("Function_18_11C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1298")

    AnonymousTalk(    #18
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R1500_01\x01",          # 0
            "R1500_02\x01",          # 1
            "R1500_03\x01",          # 2
            "R1500_04\x01",          # 3
            "BTL_QUEST006\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_123B"),
        (1, "loc_124B"),
        (2, "loc_125B"),
        (3, "loc_126B"),
        (4, "loc_127B"),
        (SWITCH_DEFAULT, "loc_128B"),
    )


    label("loc_123B")

    Battle(0x12D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1295")

    label("loc_124B")

    Battle(0x12E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1295")

    label("loc_125B")

    Battle(0x12F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1295")

    label("loc_126B")

    Battle(0x130, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1295")

    label("loc_127B")

    Battle(0x3EE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1295")

    label("loc_128B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1295")

    Jump("Function_18_11C0")

    label("loc_1298")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_18_11C0 end

    def Function_19_12A6(): pass

    label("Function_19_12A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_137A")

    AnonymousTalk(    #19
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C1100_01\x01",      # 0
            "C1100_02\x01",      # 1
            "C1100_03\x01",      # 2
            "C1100_04\x01",      # 3
            "C1100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_131D"),
        (1, "loc_132D"),
        (2, "loc_133D"),
        (3, "loc_134D"),
        (4, "loc_135D"),
        (SWITCH_DEFAULT, "loc_136D"),
    )


    label("loc_131D")

    Battle(0x141, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1377")

    label("loc_132D")

    Battle(0x142, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1377")

    label("loc_133D")

    Battle(0x143, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1377")

    label("loc_134D")

    Battle(0x144, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1377")

    label("loc_135D")

    Battle(0x145, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1377")

    label("loc_136D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1377")

    Jump("Function_19_12A6")

    label("loc_137A")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_19_12A6 end

    def Function_20_1388(): pass

    label("Function_20_1388")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1511")

    AnonymousTalk(    #20
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        60,
        1,
        (
            "Manoria Village\x01",                 # 0
            "Gull Seaside Way\x01",                # 1
            "Vista Forest Road\x01",               # 2
            "Aina Highway\x01",                    # 3
            "Tower\x01",                           # 4
            "Ruan Mayor's Residence\x01",          # 5
            "Varenne Lighthouse (Night)\x01",      # 6
            "Ruan Warehouse\x01",                  # 7
            "Old Schoolhouse\x01",                 # 8
            "Varenne Lighthouse (Day)\x01",        # 9
            "Cancel\x01",                          # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_149A"),
        (1, "loc_14A1"),
        (2, "loc_14A8"),
        (3, "loc_14AF"),
        (4, "loc_14B6"),
        (5, "loc_14BD"),
        (6, "loc_14CD"),
        (7, "loc_14D4"),
        (8, "loc_14E4"),
        (9, "loc_14F4"),
        (SWITCH_DEFAULT, "loc_1504"),
    )


    label("loc_149A")

    Call(2, 21)
    Jump("loc_150E")

    label("loc_14A1")

    Call(2, 22)
    Jump("loc_150E")

    label("loc_14A8")

    Call(2, 23)
    Jump("loc_150E")

    label("loc_14AF")

    Call(2, 24)
    Jump("loc_150E")

    label("loc_14B6")

    Call(2, 25)
    Jump("loc_150E")

    label("loc_14BD")

    Battle(0x394, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_150E")

    label("loc_14CD")

    Call(2, 26)
    Jump("loc_150E")

    label("loc_14D4")

    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_150E")

    label("loc_14E4")

    Battle(0x399, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_150E")

    label("loc_14F4")

    Battle(0x3F2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_150E")

    label("loc_1504")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_150E")

    Jump("Function_20_1388")

    label("loc_1511")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_20_1388 end

    def Function_21_151F(): pass

    label("Function_21_151F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F3")

    AnonymousTalk(    #21
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2100_01\x01",      # 0
            "R2100_02\x01",      # 1
            "R2100_03\x01",      # 2
            "R2100_04\x01",      # 3
            "R2100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1596"),
        (1, "loc_15A6"),
        (2, "loc_15B6"),
        (3, "loc_15C6"),
        (4, "loc_15D6"),
        (SWITCH_DEFAULT, "loc_15E6"),
    )


    label("loc_1596")

    Battle(0x169, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_15F0")

    label("loc_15A6")

    Battle(0x16A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_15F0")

    label("loc_15B6")

    Battle(0x16B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_15F0")

    label("loc_15C6")

    Battle(0x16C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_15F0")

    label("loc_15D6")

    Battle(0x16D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_15F0")

    label("loc_15E6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15F0")

    Jump("Function_21_151F")

    label("loc_15F3")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_21_151F end

    def Function_22_1601(): pass

    label("Function_22_1601")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1756")

    AnonymousTalk(    #22
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2200_01 Main\x01",                 # 0
            "R2200_02\x01",                      # 1
            "R2201_01 Beach\x01",                # 2
            "R2201_02\x01",                      # 3
            "R2202_01 Main (Evening)\x01",       # 4
            "R2202_02\x01",                      # 5
            "R2203_01 Beach (Evening)\x01",      # 6
            "R2203_02\x01",                      # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16C9"),
        (1, "loc_16D9"),
        (2, "loc_16E9"),
        (3, "loc_16F9"),
        (4, "loc_1709"),
        (5, "loc_1719"),
        (6, "loc_1729"),
        (7, "loc_1739"),
        (SWITCH_DEFAULT, "loc_1749"),
    )


    label("loc_16C9")

    Battle(0x17D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1753")

    label("loc_16D9")

    Battle(0x17E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1753")

    label("loc_16E9")

    Battle(0x187, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1753")

    label("loc_16F9")

    Battle(0x188, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1753")

    label("loc_1709")

    Battle(0x321, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1753")

    label("loc_1719")

    Battle(0x322, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1753")

    label("loc_1729")

    Battle(0x32B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1753")

    label("loc_1739")

    Battle(0x32C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1753")

    label("loc_1749")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1753")

    Jump("Function_22_1601")

    label("loc_1756")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_22_1601 end

    def Function_23_1764(): pass

    label("Function_23_1764")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18FB")

    AnonymousTalk(    #23
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2300_01\x01",                # 0
            "R2300_02\x01",                # 1
            "R2300_03\x01",                # 2
            "R2300_04\x01",                # 3
            "R2300_05\x01",                # 4
            "R2301_01 (Evening)\x01",      # 5
            "R2301_02 (Evening)\x01",      # 6
            "R2301_03 (Evening)\x01",      # 7
            "R2301_04 (Evening)\x01",      # 8
            "R2301_05 (Evening)\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_184E"),
        (1, "loc_185E"),
        (2, "loc_186E"),
        (3, "loc_187E"),
        (4, "loc_188E"),
        (5, "loc_189E"),
        (6, "loc_18AE"),
        (7, "loc_18BE"),
        (8, "loc_18CE"),
        (9, "loc_18DE"),
        (SWITCH_DEFAULT, "loc_18EE"),
    )


    label("loc_184E")

    Battle(0x191, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18F8")

    label("loc_185E")

    Battle(0x192, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18F8")

    label("loc_186E")

    Battle(0x193, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18F8")

    label("loc_187E")

    Battle(0x194, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18F8")

    label("loc_188E")

    Battle(0x195, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18F8")

    label("loc_189E")

    Battle(0x335, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18F8")

    label("loc_18AE")

    Battle(0x336, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18F8")

    label("loc_18BE")

    Battle(0x337, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18F8")

    label("loc_18CE")

    Battle(0x338, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18F8")

    label("loc_18DE")

    Battle(0x339, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_18F8")

    label("loc_18EE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18F8")

    Jump("Function_23_1764")

    label("loc_18FB")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_23_1764 end

    def Function_24_1909(): pass

    label("Function_24_1909")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19DD")

    AnonymousTalk(    #24
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R2400_01\x01",      # 0
            "R2400_02\x01",      # 1
            "R2400_03\x01",      # 2
            "R2400_04\x01",      # 3
            "R2400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1980"),
        (1, "loc_1990"),
        (2, "loc_19A0"),
        (3, "loc_19B0"),
        (4, "loc_19C0"),
        (SWITCH_DEFAULT, "loc_19D0"),
    )


    label("loc_1980")

    Battle(0x1A5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_19DA")

    label("loc_1990")

    Battle(0x1A6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_19DA")

    label("loc_19A0")

    Battle(0x1A7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_19DA")

    label("loc_19B0")

    Battle(0x1A8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_19DA")

    label("loc_19C0")

    Battle(0x1A9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_19DA")

    label("loc_19D0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19DA")

    Jump("Function_24_1909")

    label("loc_19DD")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_24_1909 end

    def Function_25_19EB(): pass

    label("Function_25_19EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ABF")

    AnonymousTalk(    #25
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C2111_01\x01",      # 0
            "C2111_02\x01",      # 1
            "C2111_03\x01",      # 2
            "C2111_04\x01",      # 3
            "C2111_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A62"),
        (1, "loc_1A72"),
        (2, "loc_1A82"),
        (3, "loc_1A92"),
        (4, "loc_1AA2"),
        (SWITCH_DEFAULT, "loc_1AB2"),
    )


    label("loc_1A62")

    Battle(0x1B9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1ABC")

    label("loc_1A72")

    Battle(0x1BA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1ABC")

    label("loc_1A82")

    Battle(0x1BB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1ABC")

    label("loc_1A92")

    Battle(0x1BC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1ABC")

    label("loc_1AA2")

    Battle(0x1BD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1ABC")

    label("loc_1AB2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1ABC")

    Jump("Function_25_19EB")

    label("loc_1ABF")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_25_19EB end

    def Function_26_1ACD(): pass

    label("Function_26_1ACD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB9")

    AnonymousTalk(    #26
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "BTL_EVENT011 (Deen)\x01",              # 0
            "BTL_EVENT012 (Rais)\x01",              # 1
            "BTL_EVENT013 (Rocco)\x01",             # 2
            "BTL_EVENT014 (Man in Black)\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B6C"),
        (1, "loc_1B7C"),
        (2, "loc_1B8C"),
        (3, "loc_1B9C"),
        (SWITCH_DEFAULT, "loc_1BAC"),
    )


    label("loc_1B6C")

    Battle(0x38F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BB6")

    label("loc_1B7C")

    Battle(0x390, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BB6")

    label("loc_1B8C")

    Battle(0x391, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BB6")

    label("loc_1B9C")

    Battle(0x392, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1BB6")

    label("loc_1BAC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BB6")

    Jump("Function_26_1ACD")

    label("loc_1BB9")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_26_1ACD end

    def Function_27_1BC7(): pass

    label("Function_27_1BC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CEA")

    AnonymousTalk(    #27
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "Kaldia Tunnel\x01",              # 0
            "Kaldia Limestone Cave\x01",      # 1
            "Tower\x01",                      # 2
            "Tratt Plains Road\x01",          # 3
            "Ritter Roadway\x01",             # 4
            "Soldat Army Road\x01",           # 5
            "Leiston Fortress\x01",           # 6
            "Tower (Event)\x01",              # 7
            "Cancel\x01",                     # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C9C"),
        (1, "loc_1CA3"),
        (2, "loc_1CAA"),
        (3, "loc_1CB1"),
        (4, "loc_1CB8"),
        (5, "loc_1CBF"),
        (6, "loc_1CC6"),
        (7, "loc_1CCD"),
        (SWITCH_DEFAULT, "loc_1CDD"),
    )


    label("loc_1C9C")

    Call(2, 28)
    Jump("loc_1CE7")

    label("loc_1CA3")

    Call(2, 29)
    Jump("loc_1CE7")

    label("loc_1CAA")

    Call(2, 30)
    Jump("loc_1CE7")

    label("loc_1CB1")

    Call(2, 31)
    Jump("loc_1CE7")

    label("loc_1CB8")

    Call(2, 32)
    Jump("loc_1CE7")

    label("loc_1CBF")

    Call(2, 33)
    Jump("loc_1CE7")

    label("loc_1CC6")

    Call(2, 34)
    Jump("loc_1CE7")

    label("loc_1CCD")

    Battle(0x3A0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1CE7")

    label("loc_1CDD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CE7")

    Jump("Function_27_1BC7")

    label("loc_1CEA")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_27_1BC7 end

    def Function_28_1CF8(): pass

    label("Function_28_1CF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DCC")

    AnonymousTalk(    #28
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3400_01\x01",      # 0
            "R3400_02\x01",      # 1
            "R3400_03\x01",      # 2
            "R3400_04\x01",      # 3
            "R3400_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1D6F"),
        (1, "loc_1D7F"),
        (2, "loc_1D8F"),
        (3, "loc_1D9F"),
        (4, "loc_1DAF"),
        (SWITCH_DEFAULT, "loc_1DBF"),
    )


    label("loc_1D6F")

    Battle(0x1CD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DC9")

    label("loc_1D7F")

    Battle(0x1CE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DC9")

    label("loc_1D8F")

    Battle(0x1CF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DC9")

    label("loc_1D9F")

    Battle(0x1D0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DC9")

    label("loc_1DAF")

    Battle(0x1D1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1DC9")

    label("loc_1DBF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DC9")

    Jump("Function_28_1CF8")

    label("loc_1DCC")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_28_1CF8 end

    def Function_29_1DDA(): pass

    label("Function_29_1DDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F09")

    AnonymousTalk(    #29
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3300_01\x01",          # 0
            "C3300_02\x01",          # 1
            "C3300_03\x01",          # 2
            "C3300_04\x01",          # 3
            "C3300_05\x01",          # 4
            "C3300_06\x01",          # 5
            "C3300_07\x01",          # 6
            "BTL_EVENT020\x01",      # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E7C"),
        (1, "loc_1E8C"),
        (2, "loc_1E9C"),
        (3, "loc_1EAC"),
        (4, "loc_1EBC"),
        (5, "loc_1ECC"),
        (6, "loc_1EDC"),
        (7, "loc_1EEC"),
        (SWITCH_DEFAULT, "loc_1EFC"),
    )


    label("loc_1E7C")

    Battle(0x1E1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F06")

    label("loc_1E8C")

    Battle(0x1E2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F06")

    label("loc_1E9C")

    Battle(0x1E3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F06")

    label("loc_1EAC")

    Battle(0x1E4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F06")

    label("loc_1EBC")

    Battle(0x1E5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F06")

    label("loc_1ECC")

    Battle(0x1E6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F06")

    label("loc_1EDC")

    Battle(0x1E7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F06")

    label("loc_1EEC")

    Battle(0x398, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1F06")

    label("loc_1EFC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F06")

    Jump("Function_29_1DDA")

    label("loc_1F09")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_29_1DDA end

    def Function_30_1F17(): pass

    label("Function_30_1F17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FEB")

    AnonymousTalk(    #30
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3511_01\x01",      # 0
            "C3511_02\x01",      # 1
            "C3511_03\x01",      # 2
            "C3511_04\x01",      # 3
            "C3511_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F8E"),
        (1, "loc_1F9E"),
        (2, "loc_1FAE"),
        (3, "loc_1FBE"),
        (4, "loc_1FCE"),
        (SWITCH_DEFAULT, "loc_1FDE"),
    )


    label("loc_1F8E")

    Battle(0x1F5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FE8")

    label("loc_1F9E")

    Battle(0x1F6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FE8")

    label("loc_1FAE")

    Battle(0x1F7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FE8")

    label("loc_1FBE")

    Battle(0x1F8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FE8")

    label("loc_1FCE")

    Battle(0x1F9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1FE8")

    label("loc_1FDE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FE8")

    Jump("Function_30_1F17")

    label("loc_1FEB")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_30_1F17 end

    def Function_31_1FF9(): pass

    label("Function_31_1FF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_215E")

    AnonymousTalk(    #31
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3100_01\x01",      # 0
            "R3100_02\x01",      # 1
            "R3100_03\x01",      # 2
            "R3100_04\x01",      # 3
            "R3101_05\x01",      # 4
            "R3101_01\x01",      # 5
            "R3101_02\x01",      # 6
            "R3101_03\x01",      # 7
            "R3101_04\x01",      # 8
            "R3101_05\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_20B1"),
        (1, "loc_20C1"),
        (2, "loc_20D1"),
        (3, "loc_20E1"),
        (4, "loc_20F1"),
        (5, "loc_2101"),
        (6, "loc_2111"),
        (7, "loc_2121"),
        (8, "loc_2131"),
        (9, "loc_2141"),
        (SWITCH_DEFAULT, "loc_2151"),
    )


    label("loc_20B1")

    Battle(0x209, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_215B")

    label("loc_20C1")

    Battle(0x20A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_215B")

    label("loc_20D1")

    Battle(0x20B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_215B")

    label("loc_20E1")

    Battle(0x20C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_215B")

    label("loc_20F1")

    Battle(0x20D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_215B")

    label("loc_2101")

    Battle(0x349, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_215B")

    label("loc_2111")

    Battle(0x34A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_215B")

    label("loc_2121")

    Battle(0x34B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_215B")

    label("loc_2131")

    Battle(0x34C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_215B")

    label("loc_2141")

    Battle(0x34D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_215B")

    label("loc_2151")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_215B")

    Jump("Function_31_1FF9")

    label("loc_215E")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_31_1FF9 end

    def Function_32_216C(): pass

    label("Function_32_216C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2240")

    AnonymousTalk(    #32
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3200_01\x01",      # 0
            "R3200_02\x01",      # 1
            "R3200_03\x01",      # 2
            "R3200_04\x01",      # 3
            "R3200_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21E3"),
        (1, "loc_21F3"),
        (2, "loc_2203"),
        (3, "loc_2213"),
        (4, "loc_2223"),
        (SWITCH_DEFAULT, "loc_2233"),
    )


    label("loc_21E3")

    Battle(0x21D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_223D")

    label("loc_21F3")

    Battle(0x21E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_223D")

    label("loc_2203")

    Battle(0x21F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_223D")

    label("loc_2213")

    Battle(0x220, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_223D")

    label("loc_2223")

    Battle(0x221, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_223D")

    label("loc_2233")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_223D")

    Jump("Function_32_216C")

    label("loc_2240")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_32_216C end

    def Function_33_224E(): pass

    label("Function_33_224E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2322")

    AnonymousTalk(    #33
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R3300_01\x01",      # 0
            "R3300_02\x01",      # 1
            "R3300_03\x01",      # 2
            "R3300_04\x01",      # 3
            "R3300_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_22C5"),
        (1, "loc_22D5"),
        (2, "loc_22E5"),
        (3, "loc_22F5"),
        (4, "loc_2305"),
        (SWITCH_DEFAULT, "loc_2315"),
    )


    label("loc_22C5")

    Battle(0x231, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_231F")

    label("loc_22D5")

    Battle(0x232, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_231F")

    label("loc_22E5")

    Battle(0x233, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_231F")

    label("loc_22F5")

    Battle(0x234, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_231F")

    label("loc_2305")

    Battle(0x235, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_231F")

    label("loc_2315")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_231F")

    Jump("Function_33_224E")

    label("loc_2322")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_33_224E end

    def Function_34_2330(): pass

    label("Function_34_2330")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_242B")

    AnonymousTalk(    #34
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C3107_01\x01",                # 0
            "C3107_02\x01",                # 1
            "C3107_10\x01",                # 2
            "C3107_11\x01",                # 3
            "C3107_12\x01",                # 4
            "C3107_14 (Agent C)\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_23BE"),
        (1, "loc_23CE"),
        (2, "loc_23DE"),
        (3, "loc_23EE"),
        (4, "loc_23FE"),
        (5, "loc_240E"),
        (SWITCH_DEFAULT, "loc_241E"),
    )


    label("loc_23BE")

    Battle(0x245, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2428")

    label("loc_23CE")

    Battle(0x246, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2428")

    label("loc_23DE")

    Battle(0x24E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2428")

    label("loc_23EE")

    Battle(0x24F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2428")

    label("loc_23FE")

    Battle(0x250, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2428")

    label("loc_240E")

    Battle(0x252, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2428")

    label("loc_241E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2428")

    Jump("Function_34_2330")

    label("loc_242B")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_34_2330 end

    def Function_35_2439(): pass

    label("Function_35_2439")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_258B")

    AnonymousTalk(    #35
        "\x06Select a map.\x02",
    )


    Menu(
        2,
        10,
        80,
        1,
        (
            "Erbe Scenic Route\x01",                  # 0
            "Sewers\x01",                             # 1
            "Sealed Area\x01",                        # 2
            "Royal Avenue\x01",                       # 3
            "Erbe Royal Villa (Night)\x01",           # 4
            "Erbe Royal Villa Room (Night)\x01",      # 5
            "Castle\x01",                             # 6
            "Castle Garden\x01",                      # 7
            "Sealed Area Bosses\x01",                 # 8
            "Grand Arena\x01",                        # 9
            "Cancel\x01",                             # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2538"),
        (1, "loc_253F"),
        (2, "loc_2546"),
        (3, "loc_254D"),
        (4, "loc_2554"),
        (5, "loc_255B"),
        (6, "loc_2562"),
        (7, "loc_2569"),
        (8, "loc_2570"),
        (9, "loc_2577"),
        (SWITCH_DEFAULT, "loc_257E"),
    )


    label("loc_2538")

    Call(2, 36)
    Jump("loc_2588")

    label("loc_253F")

    Call(2, 37)
    Jump("loc_2588")

    label("loc_2546")

    Call(2, 38)
    Jump("loc_2588")

    label("loc_254D")

    Call(2, 39)
    Jump("loc_2588")

    label("loc_2554")

    Call(2, 40)
    Jump("loc_2588")

    label("loc_255B")

    Call(2, 41)
    Jump("loc_2588")

    label("loc_2562")

    Call(2, 42)
    Jump("loc_2588")

    label("loc_2569")

    Call(2, 43)
    Jump("loc_2588")

    label("loc_2570")

    Call(2, 44)
    Jump("loc_2588")

    label("loc_2577")

    Call(2, 45)
    Jump("loc_2588")

    label("loc_257E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2588")

    Jump("Function_35_2439")

    label("loc_258B")

    OP_5F(0x2)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_35_2439 end

    def Function_36_2599(): pass

    label("Function_36_2599")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_266D")

    AnonymousTalk(    #36
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4100_01\x01",      # 0
            "C4100_02\x01",      # 1
            "C4100_03\x01",      # 2
            "C4100_04\x01",      # 3
            "C4100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2610"),
        (1, "loc_2620"),
        (2, "loc_2630"),
        (3, "loc_2640"),
        (4, "loc_2650"),
        (SWITCH_DEFAULT, "loc_2660"),
    )


    label("loc_2610")

    Battle(0x259, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_266A")

    label("loc_2620")

    Battle(0x25A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_266A")

    label("loc_2630")

    Battle(0x25B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_266A")

    label("loc_2640")

    Battle(0x25C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_266A")

    label("loc_2650")

    Battle(0x25D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_266A")

    label("loc_2660")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_266A")

    Jump("Function_36_2599")

    label("loc_266D")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_36_2599 end

    def Function_37_267B(): pass

    label("Function_37_267B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C3")

    AnonymousTalk(    #37
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4200_01\x01",      # 0
            "C4200_02\x01",      # 1
            "C4200_03\x01",      # 2
            "C4200_04\x01",      # 3
            "C4200_05\x01",      # 4
            "C4200_06\x01",      # 5
            "C4200_07\x01",      # 6
            "C4200_08\x01",      # 7
            "C4200_09\x01",      # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2726"),
        (1, "loc_2736"),
        (2, "loc_2746"),
        (3, "loc_2756"),
        (4, "loc_2766"),
        (5, "loc_2776"),
        (6, "loc_2786"),
        (7, "loc_2796"),
        (8, "loc_27A6"),
        (SWITCH_DEFAULT, "loc_27B6"),
    )


    label("loc_2726")

    Battle(0x26D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27C0")

    label("loc_2736")

    Battle(0x26E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27C0")

    label("loc_2746")

    Battle(0x26F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27C0")

    label("loc_2756")

    Battle(0x270, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27C0")

    label("loc_2766")

    Battle(0x271, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27C0")

    label("loc_2776")

    Battle(0x272, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27C0")

    label("loc_2786")

    Battle(0x273, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27C0")

    label("loc_2796")

    Battle(0x274, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27C0")

    label("loc_27A6")

    Battle(0x275, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_27C0")

    label("loc_27B6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27C0")

    Jump("Function_37_267B")

    label("loc_27C3")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_37_267B end

    def Function_38_27D1(): pass

    label("Function_38_27D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2936")

    AnonymousTalk(    #38
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "C4300_01\x01",      # 0
            "C4300_02\x01",      # 1
            "C4300_03\x01",      # 2
            "C4300_04\x01",      # 3
            "C4300_05\x01",      # 4
            "C4300_06\x01",      # 5
            "C4300_07\x01",      # 6
            "C4300_08\x01",      # 7
            "C4300_09\x01",      # 8
            "C4300_10\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2889"),
        (1, "loc_2899"),
        (2, "loc_28A9"),
        (3, "loc_28B9"),
        (4, "loc_28C9"),
        (5, "loc_28D9"),
        (6, "loc_28E9"),
        (7, "loc_28F9"),
        (8, "loc_2909"),
        (9, "loc_2919"),
        (SWITCH_DEFAULT, "loc_2929"),
    )


    label("loc_2889")

    Battle(0x281, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2933")

    label("loc_2899")

    Battle(0x282, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2933")

    label("loc_28A9")

    Battle(0x283, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2933")

    label("loc_28B9")

    Battle(0x284, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2933")

    label("loc_28C9")

    Battle(0x285, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2933")

    label("loc_28D9")

    Battle(0x286, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2933")

    label("loc_28E9")

    Battle(0x287, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2933")

    label("loc_28F9")

    Battle(0x288, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2933")

    label("loc_2909")

    Battle(0x289, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2933")

    label("loc_2919")

    Battle(0x28A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2933")

    label("loc_2929")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2933")

    Jump("Function_38_27D1")

    label("loc_2936")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_38_27D1 end

    def Function_39_2944(): pass

    label("Function_39_2944")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A18")

    AnonymousTalk(    #39
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R4100_01\x01",      # 0
            "R4100_02\x01",      # 1
            "R4100_03\x01",      # 2
            "R4100_04\x01",      # 3
            "R4100_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_29BB"),
        (1, "loc_29CB"),
        (2, "loc_29DB"),
        (3, "loc_29EB"),
        (4, "loc_29FB"),
        (SWITCH_DEFAULT, "loc_2A0B"),
    )


    label("loc_29BB")

    Battle(0x295, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A15")

    label("loc_29CB")

    Battle(0x296, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A15")

    label("loc_29DB")

    Battle(0x297, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A15")

    label("loc_29EB")

    Battle(0x298, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A15")

    label("loc_29FB")

    Battle(0x299, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2A15")

    label("loc_2A0B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A15")

    Jump("Function_39_2944")

    label("loc_2A18")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_39_2944 end

    def Function_40_2A26(): pass

    label("Function_40_2A26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AFA")

    AnonymousTalk(    #40
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4301_01\x01",      # 0
            "T4301_02\x01",      # 1
            "T4301_03\x01",      # 2
            "T4301_04\x01",      # 3
            "T4301_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A9D"),
        (1, "loc_2AAD"),
        (2, "loc_2ABD"),
        (3, "loc_2ACD"),
        (4, "loc_2ADD"),
        (SWITCH_DEFAULT, "loc_2AED"),
    )


    label("loc_2A9D")

    Battle(0x2BD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2AF7")

    label("loc_2AAD")

    Battle(0x2BE, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2AF7")

    label("loc_2ABD")

    Battle(0x2BF, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2AF7")

    label("loc_2ACD")

    Battle(0x2C0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2AF7")

    label("loc_2ADD")

    Battle(0x2C1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2AF7")

    label("loc_2AED")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AF7")

    Jump("Function_40_2A26")

    label("loc_2AFA")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_40_2A26 end

    def Function_41_2B08(): pass

    label("Function_41_2B08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BDC")

    AnonymousTalk(    #41
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4310_01\x01",      # 0
            "T4310_02\x01",      # 1
            "T4310_03\x01",      # 2
            "T4310_04\x01",      # 3
            "T4310_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B7F"),
        (1, "loc_2B8F"),
        (2, "loc_2B9F"),
        (3, "loc_2BAF"),
        (4, "loc_2BBF"),
        (SWITCH_DEFAULT, "loc_2BCF"),
    )


    label("loc_2B7F")

    Battle(0x2D1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BD9")

    label("loc_2B8F")

    Battle(0x2D2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BD9")

    label("loc_2B9F")

    Battle(0x2D3, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BD9")

    label("loc_2BAF")

    Battle(0x2D4, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BD9")

    label("loc_2BBF")

    Battle(0x2D5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2BD9")

    label("loc_2BCF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BD9")

    Jump("Function_41_2B08")

    label("loc_2BDC")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_41_2B08 end

    def Function_42_2BEA(): pass

    label("Function_42_2BEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CBE")

    AnonymousTalk(    #42
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4210_01\x01",      # 0
            "T4210_02\x01",      # 1
            "T4210_03\x01",      # 2
            "T4210_04\x01",      # 3
            "T4210_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C61"),
        (1, "loc_2C71"),
        (2, "loc_2C81"),
        (3, "loc_2C91"),
        (4, "loc_2CA1"),
        (SWITCH_DEFAULT, "loc_2CB1"),
    )


    label("loc_2C61")

    Battle(0x2E5, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CBB")

    label("loc_2C71")

    Battle(0x2E6, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CBB")

    label("loc_2C81")

    Battle(0x2E7, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CBB")

    label("loc_2C91")

    Battle(0x2E8, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CBB")

    label("loc_2CA1")

    Battle(0x2E9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2CBB")

    label("loc_2CB1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2CBB")

    Jump("Function_42_2BEA")

    label("loc_2CBE")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_42_2BEA end

    def Function_43_2CCC(): pass

    label("Function_43_2CCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DA0")

    AnonymousTalk(    #43
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "T4201_01\x01",      # 0
            "T4201_02\x01",      # 1
            "T4201_03\x01",      # 2
            "T4201_04\x01",      # 3
            "T4201_05\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D43"),
        (1, "loc_2D53"),
        (2, "loc_2D63"),
        (3, "loc_2D73"),
        (4, "loc_2D83"),
        (SWITCH_DEFAULT, "loc_2D93"),
    )


    label("loc_2D43")

    Battle(0x2F9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D9D")

    label("loc_2D53")

    Battle(0x2FA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D9D")

    label("loc_2D63")

    Battle(0x2FB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D9D")

    label("loc_2D73")

    Battle(0x2FC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D9D")

    label("loc_2D83")

    Battle(0x2FD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2D9D")

    label("loc_2D93")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D9D")

    Jump("Function_43_2CCC")

    label("loc_2DA0")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_43_2CCC end

    def Function_44_2DAE(): pass

    label("Function_44_2DAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E9D")

    AnonymousTalk(    #44
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "Lorence\x01",               # 0
            "Kanone\x01",                # 1
            "Richard\x01",               # 2
            "Last Boss Form 1\x01",      # 3
            "Last Boss Form 2\x01",      # 4
            "Cancel\x01",                # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2E38"),
        (1, "loc_2E48"),
        (2, "loc_2E58"),
        (3, "loc_2E68"),
        (4, "loc_2E7C"),
        (SWITCH_DEFAULT, "loc_2E90"),
    )


    label("loc_2E38")

    Battle(0x39A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E9A")

    label("loc_2E48")

    Battle(0x39B, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E9A")

    label("loc_2E58")

    Battle(0x39C, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E9A")

    label("loc_2E68")

    Call(2, 48)
    Battle(0x3A1, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E9A")

    label("loc_2E7C")

    Call(2, 48)
    Battle(0x3A2, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2E9A")

    label("loc_2E90")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E9A")

    Jump("Function_44_2DAE")

    label("loc_2E9D")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_44_2DAE end

    def Function_45_2EAB(): pass

    label("Function_45_2EAB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F7D")

    AnonymousTalk(    #45
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "Deen, Rais, Rocco\x01",                  # 0
            "Kurt, Grant, Carna, Anelace\x01",        # 1
            "Lorence, Special Ops Soldiers\x01",      # 2
            "Cancel\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F40"),
        (1, "loc_2F50"),
        (2, "loc_2F60"),
        (SWITCH_DEFAULT, "loc_2F70"),
    )


    label("loc_2F40")

    Battle(0x39D, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F7A")

    label("loc_2F50")

    Battle(0x39E, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F7A")

    label("loc_2F60")

    Battle(0x39F, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_2F7A")

    label("loc_2F70")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F7A")

    Jump("Function_45_2EAB")

    label("loc_2F7D")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_45_2EAB end

    def Function_46_2F8B(): pass

    label("Function_46_2F8B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_305F")

    AnonymousTalk(    #46
        "\x06Select a battle.\x02",
    )


    Menu(
        3,
        10,
        100,
        1,
        (
            "R4100_21\x01",      # 0
            "R4100_22\x01",      # 1
            "R4100_23\x01",      # 2
            "R4100_24\x01",      # 3
            "R4100_25\x01",      # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3002"),
        (1, "loc_3012"),
        (2, "loc_3022"),
        (3, "loc_3032"),
        (4, "loc_3042"),
        (SWITCH_DEFAULT, "loc_3052"),
    )


    label("loc_3002")

    Battle(0x2A9, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_305C")

    label("loc_3012")

    Battle(0x2AA, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_305C")

    label("loc_3022")

    Battle(0x2AB, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_305C")

    label("loc_3032")

    Battle(0x2AC, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_305C")

    label("loc_3042")

    Battle(0x2AD, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_305C")

    label("loc_3052")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_305C")

    Jump("Function_46_2F8B")

    label("loc_305F")

    OP_5F(0x3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_46_2F8B end

    def Function_47_306D(): pass

    label("Function_47_306D")

    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x0, 0x5, 0x0)
    OP_31(0x1, 0x5, 0x0)

    AnonymousTalk(    #47
        "\x06Select a battle.\x02",
    )


    label("loc_3095")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32E8")

    Menu(
        1,
        10,
        100,
        1,
        (
            "Small Fishies\x01",                  # 0
            "Lily Mover\x01",                     # 1
            "Event Battle, Rough Field\x01",      # 2
            "Pom + Killer Smoke\x01",             # 3
            "NPC Battle\x01",                     # 4
            "Sky Battle\x01",                     # 5
            "Auto-Battle 1\x01",                  # 6
            "Arena 1\x01",                        # 7
            "Arena 2\x01",                        # 8
            "Arena 3\x01",                        # 9
            "Arena 4\x01",                        # 10
            "Arena 5\x01",                        # 11
            "Arena 6\x01",                        # 12
            "Cancel\x01",                         # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_318C"),
        (1, "loc_319C"),
        (2, "loc_31AC"),
        (3, "loc_31EC"),
        (4, "loc_31FC"),
        (5, "loc_3212"),
        (6, "loc_3222"),
        (7, "loc_323B"),
        (8, "loc_3254"),
        (9, "loc_326D"),
        (10, "loc_3286"),
        (11, "loc_329F"),
        (12, "loc_32B8"),
        (SWITCH_DEFAULT, "loc_32D1"),
    )


    label("loc_318C")

    Battle(0x7A, 0x0, 0x0, 0x2, 0xFF)
    Jump("loc_32DB")

    label("loc_319C")

    Battle(0x18, 0x0, 0x0, 0x2, 0xFF)
    Jump("loc_32DB")

    label("loc_31AC")


    AnonymousTalk(    #48
        "This is an event battle. Defeat all enemies.\x02",
    )

    CloseMessageWindow()
    Battle(0x393, 0x0, 0x0, 0x2, 0xFF)
    Jump("loc_32DB")

    label("loc_31EC")

    Battle(0x38, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_32DB")

    label("loc_31FC")

    AddParty(0xE, 0xFF)
    AddParty(0xF, 0xFF)
    Battle(0x7A, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_32DB")

    label("loc_3212")

    Battle(0x387, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_32DB")

    label("loc_3222")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBB8, 0x100001, 0x0, 0x200, 0xFF)
    Jump("loc_32DB")

    label("loc_323B")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBB9, 0x100002, 0x0, 0x200, 0xFF)
    Jump("loc_32DB")

    label("loc_3254")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBA, 0x100003, 0x0, 0x200, 0xFF)
    Jump("loc_32DB")

    label("loc_326D")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBB, 0x100004, 0x0, 0x200, 0xFF)
    Jump("loc_32DB")

    label("loc_3286")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBC, 0x100005, 0x0, 0x200, 0xFF)
    Jump("loc_32DB")

    label("loc_329F")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBD, 0x100006, 0x0, 0x200, 0xFF)
    Jump("loc_32DB")

    label("loc_32B8")

    OP_4F(0x30, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Battle(0xBBE, 0x100007, 0x0, 0x200, 0xFF)
    Jump("loc_32DB")

    label("loc_32D1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32DB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3095")

    label("loc_32E8")

    OP_5F(0x1)
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_47_306D end

    def Function_48_32F8(): pass

    label("Function_48_32F8")

    OP_31(0x0, 0x0, 0x27)
    OP_31(0x1, 0x0, 0x27)
    OP_31(0x2, 0x0, 0x27)
    OP_31(0x3, 0x0, 0x27)
    OP_31(0x6, 0x0, 0x27)
    OP_31(0x4, 0x0, 0x27)
    OP_31(0x5, 0x0, 0x27)
    OP_31(0x7, 0x0, 0x27)
    OP_31(0x0, 0x5, 0x64)
    OP_31(0x1, 0x5, 0x64)
    OP_31(0x2, 0x5, 0x64)
    OP_31(0x3, 0x5, 0x64)
    OP_31(0x6, 0x5, 0x64)
    OP_31(0x4, 0x5, 0x64)
    OP_31(0x5, 0x5, 0x64)
    OP_31(0x7, 0x5, 0x64)
    OP_3E(0x1F5, 99)
    OP_3E(0x1F6, 99)
    OP_3E(0x1F7, 99)
    OP_3E(0x1FB, 99)
    OP_3E(0x1FC, 99)
    OP_3E(0x1FD, 10)
    OP_3E(0x1FF, 99)
    OP_3E(0x1FF, 99)
    OP_34(0x1, 0x3C)
    OP_34(0x1, 0x3E)
    OP_34(0x1, 0x41)
    OP_34(0x1, 0x3F)
    OP_34(0x1, 0x5F)
    OP_34(0x1, 0x60)
    OP_34(0x1, 0x69)
    OP_34(0x1, 0x6A)
    OP_34(0x0, 0x1E)
    OP_34(0x0, 0x1F)
    OP_34(0x0, 0x20)
    OP_34(0x0, 0x23)
    OP_34(0x0, 0x25)
    OP_34(0x0, 0x6E)
    OP_34(0x0, 0x6F)
    OP_34(0x0, 0x70)
    OP_34(0x0, 0x76)
    OP_34(0x0, 0x77)
    OP_34(0x0, 0x78)
    OP_34(0x2, 0x32)
    OP_34(0x2, 0x33)
    OP_34(0x2, 0x34)
    OP_34(0x2, 0x36)
    OP_34(0x2, 0x37)
    OP_34(0x3, 0x64)
    OP_34(0x3, 0x69)
    OP_34(0x3, 0x69)
    OP_34(0x3, 0x4B)
    OP_34(0x3, 0x4C)
    OP_34(0x4, 0x6E)
    OP_34(0x4, 0x6F)
    OP_34(0x4, 0x70)
    OP_34(0x4, 0x72)
    OP_34(0x4, 0x73)
    OP_34(0x4, 0x76)
    OP_34(0x4, 0x77)
    OP_34(0x4, 0x78)
    OP_34(0x5, 0x1E)
    OP_34(0x5, 0x1F)
    OP_34(0x5, 0x20)
    OP_34(0x6, 0x56)
    OP_34(0x6, 0x57)
    OP_34(0x6, 0x58)
    OP_34(0x6, 0x6E)
    OP_34(0x6, 0x6F)
    OP_34(0x6, 0x76)
    OP_34(0x7, 0xB)
    OP_34(0x7, 0xD)
    OP_34(0x7, 0x10)
    OP_34(0x7, 0x4B)
    OP_34(0x7, 0x4C)
    OP_41(0x0, 0xA)
    OP_41(0x0, 0xFE)
    OP_41(0x0, 0x119)
    OP_41(0x1, 0x29)
    OP_41(0x1, 0xFD)
    OP_41(0x1, 0x11A)
    OP_41(0x2, 0x41)
    OP_41(0x2, 0xFE)
    OP_41(0x2, 0x119)
    OP_41(0x3, 0x62)
    OP_41(0x3, 0xFD)
    OP_41(0x3, 0x11A)
    OP_41(0x4, 0x80)
    OP_41(0x4, 0xFE)
    OP_41(0x4, 0x119)
    OP_41(0x5, 0x9D)
    OP_41(0x5, 0xFD)
    OP_41(0x5, 0x11A)
    OP_41(0x6, 0xBB)
    OP_41(0x6, 0xFE)
    OP_41(0x6, 0x119)
    OP_41(0x7, 0xD9)
    OP_41(0x7, 0xFD)
    OP_41(0x7, 0x11A)
    Return()

    # Function_48_32F8 end

    SaveToFile()

Try(main)
