from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3403   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
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
        '鲁迪',                                 # 9
        '',                                     # 10
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
        'ED6_DT07/CH01500 ._CH',             # 00
        'ED6_DT07/CH01760 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01500P._CP',             # 00
        'ED6_DT07/CH01760P._CP',             # 01
    )

    DeclNpc(
        X                   = 609110,
        Z                   = 0,
        Y                   = -64290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )


    ScpFunction(
        "Function_0_DA",           # 00, 0
        "Function_1_EC",           # 01, 1
        "Function_2_110",          # 02, 2
        "Function_3_24E",          # 03, 3
    )


    def Function_0_DA(): pass

    label("Function_0_DA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB")
    ClearChrFlags(0x10, 0x80)

    label("loc_EB")

    Return()

    # Function_0_DA end

    def Function_1_EC(): pass

    label("Function_1_EC")

    OP_16(0x2, 0xFA0, 0x76E58, 0xFFFD40E0, 0x23003A)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F")
    OP_1B(0x0, 0x0, 0x3)

    label("loc_10F")

    Return()

    # Function_1_EC end

    def Function_2_110(): pass

    label("Function_2_110")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_24A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A2")
    OP_8C(0xFE, 90, 0)

    ChrTalk(    #0
        0xFE,
        (
            "既、既然如此，哪怕只有一句话\x01",
            "我也要传达我的心情……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "唉，怎么说好呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "（嘀嘀咕咕、嘀嘀咕咕……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_24A")

    label("loc_1A2")


    ChrTalk(    #3
        0xFE,
        "这、这位兄弟……你听我说啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "菲前辈，\x01",
            "好像当上埃尔赛尤号\x01",
            "随舰的维修员了！\x02",
        )
    )

    Jump("loc_205")

    label("loc_205")

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "………………真是深受打击……！！\x01",
            "这下再也见不了面了啊！！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_24A")

    TalkEnd(0xFE)
    Return()

    # Function_2_110 end

    def Function_3_24E(): pass

    label("Function_3_24E")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_289")

    ChrTalk(    #6
        0x106,
        (
            "#552F他们应该\x01",
            "还在中央工房里面……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E5")

    label("loc_289")


    ChrTalk(    #7
        0x106,
        (
            "#050F这前面就是卡鲁迪亚隧道了……\x02\x03",

            "#552F他们应该\x01",
            "还在中央工房里面……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2E5")

    OP_90(0x106, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    EventEnd(0x2)
    Return()

    # Function_3_24E end

    SaveToFile()

Try(main)
