from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3117   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3117.x',
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
        '雷伊',                                 # 9
        '蒂亚利',                               # 10
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH01660 ._CH',             # 01
        'ED6_DT07/CH01050 ._CH',             # 02
        'ED6_DT07/CH01700 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH01660P._CP',             # 01
        'ED6_DT07/CH01050P._CP',             # 02
        'ED6_DT07/CH01700P._CP',             # 03
    )

    DeclNpc(
        X                   = 1730,
        Z                   = 0,
        Y                   = 15000,
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
        X                   = 1050,
        Z                   = 0,
        Y                   = 7470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_10A",          # 00, 0
        "Function_1_121",          # 01, 1
        "Function_2_122",          # 02, 2
        "Function_3_146",          # 03, 3
        "Function_4_2A5",          # 04, 4
    )


    def Function_0_10A(): pass

    label("Function_0_10A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_120")

    Return()

    # Function_0_10A end

    def Function_1_121(): pass

    label("Function_1_121")

    Return()

    # Function_1_121 end

    def Function_2_122(): pass

    label("Function_2_122")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_145")
    OP_8D(0xFE, 4670, 5810, -4590, 550, 1000)
    Jump("Function_2_122")

    label("loc_145")

    Return()

    # Function_2_122 end

    def Function_3_146(): pass

    label("Function_3_146")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_2A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1BE")

    ChrTalk(    #0
        0xFE,
        (
            "不过，导力人偶之类的，\x01",
            "不是我的专业呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "呵呵，先从收集资料开始\x01",
            "做一下基础设计试试吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A1")

    label("loc_1BE")


    ChrTalk(    #2
        0xFE,
        (
            "温室的实验，\x01",
            "应该也告一段落了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "差不多该着手开发\x01",
            "以提妲为模型的导力人偶了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "呵呵，首先从基础设计开始……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x106,
        (
            "#053F（提妲的母亲\x01",
            "  眼神也很恐怖的……）\x02\x03",

            "#057F（…………这个还是\x01",
            "  放弃比较好吧……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2A1")

    TalkEnd(0xFE)
    Return()

    # Function_3_146 end

    def Function_4_2A5(): pass

    label("Function_4_2A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_3E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_34E")

    ChrTalk(    #6
        0xFE,
        (
            "从下次开始，\x01",
            "温室的管理就由我来负责了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "这样应该能够\x01",
            "尽情进行自己的研究了…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "但是，要研究什么才好呢。\x01",
            "没有任何点子啊……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E6")

    label("loc_34E")


    ChrTalk(    #9
        0xFE,
        (
            "雷伊前辈\x01",
            "只用三个月就种出了\x01",
            "有『治愈』效果的植物。\x02",
        )
    )

    Jump("loc_393")

    label("loc_393")

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "呜呜，真难以置信……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "也没进行什么品种改良\x01",
            "就能种出这种东西来……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3E6")

    TalkEnd(0xFE)
    Return()

    # Function_4_2A5 end

    SaveToFile()

Try(main)
