from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4211   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4211.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '妮舒',                                 # 9
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
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01350 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01350P._CP',             # 00
    )

    DeclNpc(
        X                   = -5940,
        Z                   = 0,
        Y                   = 68560,
        Direction           = 268,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_DF",           # 01, 1
        "Function_2_105",          # 02, 2
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_DE")
    SetChrFlags(0x8, 0x80)

    label("loc_DE")

    Return()

    # Function_0_D2 end

    def Function_1_DF(): pass

    label("Function_1_DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FB")
    OP_B1("t4211_y")
    Jump("loc_104")

    label("loc_FB")

    OP_B1("t4211_n")

    label("loc_104")

    Return()

    # Function_1_DF end

    def Function_2_105(): pass

    label("Function_2_105")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_13F")

    ChrTalk(    #0
        0xFE,
        (
            "女王和科洛蒂娅殿下\x01",
            "究竟在谈些什么呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E1")

    label("loc_13F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1A1")

    ChrTalk(    #1
        0xFE,
        (
            "公爵对回城堡一事\x01",
            "好像感到很高兴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "肯定是因为会妨碍签字仪式\x01",
            "而被赶出了离宫。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E1")

    label("loc_1A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1E1")

    ChrTalk(    #3
        0xFE,
        "什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "十分抱歉，我正忙着\x01",
            "打扫这里的卫生呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1")

    TalkEnd(0xFE)
    Return()

    # Function_2_105 end

    SaveToFile()

Try(main)
