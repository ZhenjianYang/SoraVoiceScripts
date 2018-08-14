from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2501   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2501.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        '艾福托老师',                           # 9
        '杰尼丝王立学院',                       # 10
        '王立学院·旧校舍',                     # 11
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
        'ED6_DT07/CH01460 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01460P._CP',             # 00
    )

    DeclNpc(
        X                   = 127010,
        Z                   = 0,
        Y                   = 27720,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 101330,
        Z                   = 0,
        Y                   = 28090,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 154530,
        Z                   = 0,
        Y                   = 28060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_112",          # 00, 0
        "Function_1_166",          # 01, 1
        "Function_2_182",          # 02, 2
        "Function_3_1A6",          # 03, 3
    )


    def Function_0_112(): pass

    label("Function_0_112")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_165")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_128")
    Jump("loc_165")

    label("loc_128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_132")
    Jump("loc_165")

    label("loc_132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_141")
    ClearChrFlags(0x10, 0x80)
    Jump("loc_165")

    label("loc_141")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_14B")
    Jump("loc_165")

    label("loc_14B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_165")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_165")

    label("loc_165")

    Return()

    # Function_0_112 end

    def Function_1_166(): pass

    label("Function_1_166")

    OP_16(0x2, 0xFA0, 0x0, 0xFFFE7960, 0x23004D)
    OP_B1("t2501_n")
    Return()

    # Function_1_166 end

    def Function_2_182(): pass

    label("Function_2_182")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A5")
    OP_8D(0xFE, 129120, 25960, 125080, 29610, 2000)
    Jump("Function_2_182")

    label("loc_1A5")

    Return()

    # Function_2_182 end

    def Function_3_1A6(): pass

    label("Function_3_1A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_2CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_215")

    ChrTalk(    #0
        0xFE,
        (
            "雷克特那家伙，\x01",
            "难道去了旧校舍……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "不不，\x01",
            "那里的钥匙是我在保管的……\x02",
        )
    )

    Jump("loc_211")

    label("loc_211")

    CloseMessageWindow()
    Jump("loc_2CA")

    label("loc_215")


    ChrTalk(    #2
        0xFE,
        (
            "我正在追\x01",
            "雷克特那家伙……\x02",
        )
    )

    Jump("loc_241")

    label("loc_241")

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "但是在这附近跟丢了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "真是的，\x01",
            "那家伙简直让人毫无办法……！！\x02",
        )
    )

    Jump("loc_29A")

    label("loc_29A")

    CloseMessageWindow()

    ChrTalk(    #5
        0x105,
        (
            "#045F（哈、哈哈……\x01",
            "  实在抱歉……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2CA")

    TalkEnd(0xFE)
    Return()

    # Function_3_1A6 end

    SaveToFile()

Try(main)
