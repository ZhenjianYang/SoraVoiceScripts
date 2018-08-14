from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3118   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3118.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        '米妮亚姆医生',                         # 9
        '安东尼',                               # 10
        '',                                     # 11
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
        'ED6_DT07/CH01430 ._CH',             # 00
        'ED6_DT07/CH01700 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01430P._CP',             # 00
        'ED6_DT07/CH01700P._CP',             # 01
    )

    DeclNpc(
        X                   = -1410,
        Z                   = 0,
        Y                   = 6690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -5510,
        Z                   = 0,
        Y                   = -3140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_FA",           # 00, 0
        "Function_1_111",          # 01, 1
        "Function_2_112",          # 02, 2
        "Function_3_136",          # 03, 3
        "Function_4_24D",          # 04, 4
    )


    def Function_0_FA(): pass

    label("Function_0_FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_110")

    Return()

    # Function_0_FA end

    def Function_1_111(): pass

    label("Function_1_111")

    Return()

    # Function_1_111 end

    def Function_2_112(): pass

    label("Function_2_112")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_135")
    OP_8D(0xFE, -6290, -6030, -3150, 520, 1000)
    Jump("Function_2_112")

    label("loc_135")

    Return()

    # Function_2_112 end

    def Function_3_136(): pass

    label("Function_3_136")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_249")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C1")

    ChrTalk(    #0
        0xFE,
        (
            "唔，\x01",
            "玛多克先生今天还没来啊……\x02",
        )
    )

    Jump("loc_173")

    label("loc_173")

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "难道\x01",
            "是去教会了吗。\x02",
        )
    )

    Jump("loc_194")

    label("loc_194")

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "在那边也能祈祷，\x01",
            "真是一举两得啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_249")

    label("loc_1C1")


    ChrTalk(    #3
        0xFE,
        (
            "…………艾莉卡\x01",
            "好像回来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "那孩子也有一些地方\x01",
            "很像拉赛尔博士……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "一定又让\x01",
            "玛多克先生感到胃痛了。\x02",
        )
    )

    Jump("loc_245")

    label("loc_245")

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_249")

    TalkEnd(0xFE)
    Return()

    # Function_3_136 end

    def Function_4_24D(): pass

    label("Function_4_24D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_273")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #6
        0xFE,
        "喵呜？\x02",
    )

    Jump("loc_272")

    label("loc_272")

    CloseMessageWindow()

    label("loc_273")

    TalkEnd(0xFE)
    Return()

    # Function_4_24D end

    SaveToFile()

Try(main)
