from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2513   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2513.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '克拉拉',                               # 9
        '罗迪',                                 # 10
        '雷克特',                               # 11
        '书',                                   # 12
        '乔儿',                                 # 13
        '米克',                                 # 14
        '米克',                                 # 15
        '利戈尔',                               # 16
        '安敦',                                 # 17
        '目标用照相机',                         # 18
        '',                                     # 19
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
        'ED6_DT07/CH01090 ._CH',             # 00
        'ED6_DT07/CH01360 ._CH',             # 01
        'ED6_DT07/CH02670 ._CH',             # 02
        'ED6_DT06/CH20021 ._CH',             # 03
        'ED6_DT07/CH02390 ._CH',             # 04
        'ED6_DT07/CH01080 ._CH',             # 05
        'ED6_DT07/CH02910 ._CH',             # 06
        'ED6_DT07/CH02910 ._CH',             # 07
        'ED6_DT07/CH02900 ._CH',             # 08
        'ED6_DT26/CH20778 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01090P._CP',             # 00
        'ED6_DT07/CH01360P._CP',             # 01
        'ED6_DT07/CH02670P._CP',             # 02
        'ED6_DT06/CH20021P._CP',             # 03
        'ED6_DT07/CH02390P._CP',             # 04
        'ED6_DT07/CH01080P._CP',             # 05
        'ED6_DT07/CH02910P._CP',             # 06
        'ED6_DT07/CH02910P._CP',             # 07
        'ED6_DT07/CH02900P._CP',             # 08
        'ED6_DT26/CH20778P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C7,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0xFC,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2330,
        Z                   = 0,
        Y                   = 4680,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 56700,
        Z                   = 1000,
        Y                   = 19000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 6330,
        Y                   = 4000,
        Z                   = -1250,
        Range               = 9800,
        Unknown_10          = 0x1B58,
        Unknown_14          = 0xA0,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )


    ScpFunction(
        "Function_0_25A",          # 00, 0
        "Function_1_3A2",          # 01, 1
        "Function_2_3E6",          # 02, 2
        "Function_3_563",          # 03, 3
        "Function_4_735",          # 04, 4
        "Function_5_81F",          # 05, 5
        "Function_6_866",          # 06, 6
        "Function_7_91A",          # 07, 7
        "Function_8_BDD",          # 08, 8
        "Function_9_C91",          # 09, 9
        "Function_10_CB2",         # 0A, 10
        "Function_11_157F",        # 0B, 11
        "Function_12_1E86",        # 0C, 12
        "Function_13_23DB",        # 0D, 13
        "Function_14_246E",        # 0E, 14
    )


    def Function_0_25A(): pass

    label("Function_0_25A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_346")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_2A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 1)), scpexpr(EXPR_END)), "loc_2A0")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -37060, 1000, 7700, 90)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -35280, 1000, 7780, 270)

    label("loc_2A0")

    Jump("loc_346")

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_2B2")
    ClearChrFlags(0x18, 0x80)
    Jump("loc_346")

    label("loc_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_30E")
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrChipByIndex(0x12, 9)
    SetChrSubChip(0x12, 0)
    SetChrPos(0x12, 8600, 4200, 9370, 90)
    OP_62(0x12, 0x64, 1600, 0x18, 0x1B, 0x12C, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8160, 4400, 9200, 0)
    SetChrSubChip(0x13, 29)
    Jump("loc_346")

    label("loc_30E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_346")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -66600, 1000, 9600, 90)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -65140, 1000, 9600, 270)
    ClearChrFlags(0x17, 0x80)

    label("loc_346")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_37B")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_369"),
        (107, "loc_369"),
        (SWITCH_DEFAULT, "loc_378"),
    )


    label("loc_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_375")
    Event(0, 14)

    label("loc_375")

    Jump("loc_378")

    label("loc_378")

    Jump("loc_3A1")

    label("loc_37B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_3A1")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_392"),
        (106, "loc_392"),
        (SWITCH_DEFAULT, "loc_3A1"),
    )


    label("loc_392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39E")
    Event(0, 9)

    label("loc_39E")

    Jump("loc_3A1")

    label("loc_3A1")

    Return()

    # Function_0_25A end

    def Function_1_3A2(): pass

    label("Function_1_3A2")

    OP_B1("t2513_n")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E5")
    OP_B2(0x1, 0x0, 0x80)
    OP_62(0x12, 0x64, 1600, 0x18, 0x1B, 0x12C, 0x0)

    label("loc_3E5")

    Return()

    # Function_1_3A2 end

    def Function_2_3E6(): pass

    label("Function_2_3E6")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40B")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_54D")

    label("loc_40B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_424")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_54D")

    label("loc_424")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43D")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_54D")

    label("loc_43D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_456")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_54D")

    label("loc_456")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46F")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_54D")

    label("loc_46F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_488")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_54D")

    label("loc_488")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A1")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_54D")

    label("loc_4A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BA")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_54D")

    label("loc_4BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D3")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_54D")

    label("loc_4D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EC")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_54D")

    label("loc_4EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_505")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_54D")

    label("loc_505")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51E")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_54D")

    label("loc_51E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_537")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_54D")

    label("loc_537")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54D")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_54D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_562")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_54D")

    label("loc_562")

    Return()

    # Function_2_3E6 end

    def Function_3_563(): pass

    label("Function_3_563")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_570")
    Jump("loc_731")

    label("loc_570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_57A")
    Jump("loc_731")

    label("loc_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_584")
    Jump("loc_731")

    label("loc_584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_58E")
    Jump("loc_731")

    label("loc_58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_731")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 6)), scpexpr(EXPR_END)), "loc_5ED")

    ChrTalk(    #0
        0x17,
        (
            "其他的社团成员\x01",
            "差不多也该来了吧。\x02\x03",

            "对击剑有兴趣的话\x01",
            "就请参观一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_731")

    label("loc_5ED")


    ChrTalk(    #1
        0x17,
        "哦，记得你是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x17,
        (
            "插班来的一年级生\x01",
            "科洛丝·琳希同学吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x105,
        "#044F啊，是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x17,
        (
            "我是人文学系三年级的利戈尔。\x01",
            "担任击剑部的部长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x17,
        (
            "你有兴趣的话\x01",
            "就请参观一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x105,
        (
            "#542F……不好意思。\x01",
            "现在有些事要办……\x02\x03",

            "#543F（……击剑啊………）\x02\x03",

            "#048F（呵呵，让我想起了\x01",
            "　和尤莉亚小姐一起练习的事呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F7E)

    label("loc_731")

    TalkEnd(0xFE)
    Return()

    # Function_3_563 end

    def Function_4_735(): pass

    label("Function_4_735")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_7F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_793")

    ChrTalk(    #7
        0xFE,
        (
            "那么半吊子的家伙\x01",
            "居然是学生会长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "难道我不比\x01",
            "他更适合吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F3")

    label("loc_793")


    ChrTalk(    #9
        0xFE,
        "……难以置信。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "那么吊儿郎当的家伙\x01",
            "居然是学生会长。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "现在的世道已经变了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_7F3")

    Jump("loc_81B")

    label("loc_7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_800")
    Jump("loc_81B")

    label("loc_800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_80A")
    Jump("loc_81B")

    label("loc_80A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_814")
    Jump("loc_81B")

    label("loc_814")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_81B")

    label("loc_81B")

    TalkEnd(0xFE)
    Return()

    # Function_4_735 end

    def Function_5_81F(): pass

    label("Function_5_81F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_862")

    ChrTalk(    #12
        0xFE,
        (
            "我要重生成为他那个样子。\x01",
            "…………（嘀嘀咕咕）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_862")

    TalkEnd(0xFE)
    Return()

    # Function_5_81F end

    def Function_6_866(): pass

    label("Function_6_866")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_916")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_8AC")

    ChrTalk(    #13
        0xFE,
        "莫妮卡好慢啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "还没换好衣服吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_916")

    label("loc_8AC")


    ChrTalk(    #15
        0xFE,
        "啊，还是去社团参观一下吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "嗯，热烈欢迎哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "稍微等一下。\x01",
            "应该还有一个人要来的……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_916")

    TalkEnd(0xFE)
    Return()

    # Function_6_866 end

    def Function_7_91A(): pass

    label("Function_7_91A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_BD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 2)), scpexpr(EXPR_END)), "loc_A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_992")
    OP_8C(0xFE, 90, 0)

    ChrTalk(    #18
        0x14,
        (
            "#646F米克，\x01",
            "你好好听着哦。\x02\x03",

            "你这样\x01",
            "偷懒的行为简直是……！\x02",
        )
    )

    Jump("loc_98E")

    label("loc_98E")

    CloseMessageWindow()
    Jump("loc_A19")

    label("loc_992")


    ChrTalk(    #19
        0x14,
        (
            "#644F我再教训一会儿\x01",
            "这个家伙。\x02\x03",

            "#646F这家伙偷懒的样子，\x01",
            "跟雷克特一样真令人火大！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x105,
        "#045F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_A19")

    Jump("loc_BD9")

    label("loc_A1C")

    OP_8C(0xFE, 90, 0)

    ChrTalk(    #21
        0x14,
        (
            "#646F米克，\x01",
            "你好好听着哦。\x02\x03",

            "趁此机会\x01",
            "话先说在前头……！\x02",
        )
    )

    Jump("loc_A79")

    label("loc_A79")

    CloseMessageWindow()

    ChrTalk(    #22
        0x105,
        "#044F那个，乔儿……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #23
        0x14,
        (
            "#643F啊，科洛丝。\x02\x03",

            "#1890F抱歉，\x01",
            "我正打算教训这家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x105,
        (
            "#040F嗯，没关系。\x01",
            "找学长的事就交给我吧。\x02\x03",

            "我稍微\x01",
            "有点线索。\x02",
        )
    )

    Jump("loc_B44")

    label("loc_B44")

    CloseMessageWindow()

    ChrTalk(    #25
        0x14,
        (
            "#643F是、是吗……\x02\x03",

            "#644F嗯～\x01",
            "寻找雷克特的手段\x01",
            "已经无人能出科洛丝其右了呢……\x02",
        )
    )

    Jump("loc_BAA")

    label("loc_BAA")

    CloseMessageWindow()

    ChrTalk(    #26
        0x105,
        (
            "#045F这、这倒是\x01",
            "太夸张了点……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F82)

    label("loc_BD9")

    TalkEnd(0xFE)
    Return()

    # Function_7_91A end

    def Function_8_BDD(): pass

    label("Function_8_BDD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_C8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_C36")

    ChrTalk(    #27
        0xFE,
        (
            "等莫妮卡来了\x01",
            "就要开始今天的碰头会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "要参观就趁现在吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C8D")

    label("loc_C36")


    ChrTalk(    #29
        0xFE,
        (
            "科洛丝同学\x01",
            "好像还没加入社团吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "一会儿要开碰头会，\x01",
            "要参观就趁现在吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_C8D")

    TalkEnd(0xFE)
    Return()

    # Function_8_BDD end

    def Function_9_C91(): pass

    label("Function_9_C91")

    EventBegin(0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (105, "loc_CA3"),
        (106, "loc_CAA"),
        (SWITCH_DEFAULT, "loc_CB1"),
    )


    label("loc_CA3")

    Call(0, 10)
    Jump("loc_CB1")

    label("loc_CAA")

    Call(0, 11)
    Jump("loc_CB1")

    label("loc_CB1")

    Return()

    # Function_9_C91 end

    def Function_10_CB2(): pass

    label("Function_10_CB2")

    OP_6D(-65500, 1000, 7440, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, -66100, 0, 1500, 0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_D11():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D11)

    def lambda_D23():
        OP_8E(0xFE, 0xFFFEFDCC, 0x0, 0xF28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D23)
    WaitChrThread(0x105, 0x1)

    def lambda_D43():
        OP_8E(0xFE, 0xFFFEF5FC, 0x0, 0xF28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D43)
    WaitChrThread(0x105, 0x1)

    def lambda_D63():
        OP_8E(0xFE, 0xFFFEF5FC, 0x3E8, 0x1D10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D63)
    WaitChrThread(0x105, 0x1)
    TurnDirection(0x105, 0x10, 500)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_4A(0x10, 255)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_4A(0x11, 255)
    Sleep(500)

    ChrTalk(    #31
        0x10,
        "啊，莫妮卡？\x02",
    )

    CloseMessageWindow()

    def lambda_DD9():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_DD9)
    Sleep(100)

    def lambda_DEC():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_DEC)
    Sleep(300)

    ChrTalk(    #32
        0x10,
        "太迟啦～…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #33
        0x105,
        (
            "#044F#6P咦！？　那、那个……\x02\x03",

            "#043F对不起。\x01",
            "我搞错了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        "咦？　不……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        "搞错的是我吧？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x105,
        (
            "#045F#6P啊，是吗……\x02\x03",

            "#540F对、对不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "都说啦，\x01",
            "搞错的是我嘛……\x02",
        )
    )

    Jump("loc_F53")

    label("loc_F53")

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        (
            "#11P好了，\x01",
            "给我打住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x11,
        (
            "#11P对不起啊，科洛丝同学。\x01",
            "我们部长就是不太机灵～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        (
            "#11P……嗯，那么，有什么事吗？\x01",
            "我们之后要开会呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x105,
        (
            "#044F#6P啊，是这样吗……\x02\x03",

            "#047F（嗯……记得克拉拉学长\x01",
            "　就是社会学系的吧……）\x02\x03",

            "#049F（……不过，\x01",
            "　现在还是不太方便。）\x02\x03",

            "（会议之后\x01",
            "　再来一趟吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #42
        0x10,
        "我说…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "……啊，明白了。\x01",
            "你是来参观社团的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10,
        "好，有新社员啦！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 500)

    ChrTalk(    #45
        0x11,
        "#11P克拉拉学长，你结论也下得太快了吧……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x105, 500)

    ChrTalk(    #46
        0x11,
        "#11P啊，请别介意这家伙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        (
            "#11P……那么，\x01",
            "要是有事请快点说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x105,
        (
            "#044F#6P啊……\x02\x03",

            "#045F嗯，那、那我这就……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1207():
        OP_8E(0xFE, 0xFFFEF7F0, 0x3E8, 0x2148, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1207)
    WaitChrThread(0x105, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #49
        "\x07\x05将资料交给克拉拉。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #50
        0x10,
        "怎么，是学分表啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        "看你那个样子亏我还满怀期待呢～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        "…………好失望。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x105,
        (
            "#540F#6P对、对不起。\x02\x03",

            "#543F那么我\x01",
            "这就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        "啊，嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 180, 400)

    def lambda_1327():

        label("loc_1327")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_1327")

    QueueWorkItem2(0x10, 2, lambda_1327)

    def lambda_1338():

        label("loc_1338")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_1338")

    QueueWorkItem2(0x11, 2, lambda_1338)

    def lambda_1349():
        OP_8E(0xFE, 0xFFFEF5FC, 0x3E8, 0x1EF0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1349)
    WaitChrThread(0x105, 0x1)

    def lambda_1369():
        OP_8E(0xFE, 0xFFFEF5FC, 0x0, 0xF28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1369)
    WaitChrThread(0x105, 0x1)

    def lambda_1389():
        OP_8E(0xFE, 0xFFFEFDCC, 0x0, 0xF28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1389)
    WaitChrThread(0x105, 0x1)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8C(0x105, 180, 500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_13DE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_13DE)

    def lambda_13F0():
        OP_8E(0xFE, 0xFFFEFDCC, 0x3E8, 0x5DC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_13F0)
    WaitChrThread(0x105, 0x1)
    OP_22(0x7, 0x0, 0x64)
    Sleep(2000)
    OP_63(0x10)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #55
        0x10,
        "真是个奇怪的女孩子啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x11,
        (
            "#5P是一年级的插班生呢。\x01",
            "喏，就是那个传说中的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        "啊～就是她啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #58
        0x10,
        (
            "那顺便来参观一下\x01",
            "也没什么不好嘛～……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x2)
    OP_44(0x11, 0x2)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x5F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-7000, 0, 11400, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, -7000, 0, 11400, 180)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_69(0x105, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2F69)
    EventEnd(0x0)
    Return()

    # Function_10_CB2 end

    def Function_11_157F(): pass

    label("Function_11_157F")

    OP_6D(-64239, 1000, 8800, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, -59740, 1000, 7660, 270)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_4A(0x10, 255)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_4A(0x11, 255)
    Sleep(500)

    ChrTalk(    #59
        0x10,
        "#6P啊，莫妮卡？\x02",
    )

    CloseMessageWindow()

    def lambda_1635():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1635)
    Sleep(100)

    def lambda_1648():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1648)
    Sleep(300)

    ChrTalk(    #60
        0x10,
        "#6P太迟啦～…………\x02",
    )

    CloseMessageWindow()

    def lambda_167B():

        label("loc_167B")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_167B")

    QueueWorkItem2(0x10, 2, lambda_167B)

    def lambda_168C():

        label("loc_168C")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_168C")

    QueueWorkItem2(0x11, 2, lambda_168C)

    def lambda_169D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_169D)

    def lambda_16AF():
        OP_8E(0xFE, 0xFFFF07CC, 0x3E8, 0x1DEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16AF)
    WaitChrThread(0x105, 0x1)
    TurnDirection(0x105, 0x10, 500)
    OP_44(0x10, 0x2)
    OP_44(0x11, 0x2)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #61
        0x105,
        (
            "#044F咦！？　那、那个……\x02\x03",

            "#043F对不起。\x01",
            "我搞错了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        "#1P咦？　不……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        "#1P搞错的是我吧？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x105,
        (
            "#045F啊，是吗……\x02\x03",

            "#540F对、对不起。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "#1P都说啦，\x01",
            "搞错的是我嘛～……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x11,
        (
            "#5P好了，\x01",
            "你们俩都给我打住。\x02",
        )
    )

    Jump("loc_1840")

    label("loc_1840")

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        (
            "#5P对不起啊，科洛丝同学。\x01",
            "我们部长就是不太机灵～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x11,
        (
            "#5P……嗯，那么，有什么事吗？\x01",
            "我们之后要开会呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x105,
        (
            "#044F啊，是这样吗……\x02\x03",

            "#047F（嗯……记得克拉拉学长\x01",
            "　就是社会系的吧……）\x02\x03",

            "#049F（……不过，\x01",
            "　现在还是不太方便。）\x02\x03",

            "（会议之后\x01",
            "　再来一趟吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #70
        0x10,
        "#1P我说…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10,
        (
            "#1P……啊，明白了。\x01",
            "你是来参观社团的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        "#1P好，有新社员啦！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x10, 500)

    ChrTalk(    #73
        0x11,
        "#11P克拉拉学长，你结论也下得太快了吧……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x105, 500)

    ChrTalk(    #74
        0x11,
        "#5P啊，请别介意这家伙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x11,
        (
            "#5P……那么，\x01",
            "要是有事请快点说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x105,
        (
            "#044F啊……\x02\x03",

            "#045F嗯，那、那我这就……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1ACF():

        label("loc_1ACF")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_1ACF")

    QueueWorkItem2(0x10, 2, lambda_1ACF)

    def lambda_1AE0():

        label("loc_1AE0")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_1AE0")

    QueueWorkItem2(0x11, 2, lambda_1AE0)

    def lambda_1AF1():
        OP_8E(0xFE, 0xFFFEFBD8, 0x3E8, 0x20D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1AF1)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 0, 400)
    OP_44(0x10, 0x2)
    OP_44(0x11, 0x2)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #77
        "\x07\x05将资料交给克拉拉。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #78
        0x10,
        "#1P怎么，是学分表啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10,
        "#1P看你那个样子亏我还满怀期待呢～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10,
        "#1P…………好失望。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x105,
        (
            "#540F#6P对、对不起。\x02\x03",

            "#543F那么我\x01",
            "这就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10,
        "#1P啊，嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 250, 400)

    def lambda_1C2C():

        label("loc_1C2C")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_1C2C")

    QueueWorkItem2(0x10, 2, lambda_1C2C)

    def lambda_1C3D():

        label("loc_1C3D")

        TurnDirection(0xFE, 0x105, 400)
        OP_48()
        Jump("loc_1C3D")

    QueueWorkItem2(0x11, 2, lambda_1C3D)

    def lambda_1C4E():
        OP_8E(0xFE, 0xFFFEF5FC, 0x3E8, 0x1EF0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1C4E)
    WaitChrThread(0x105, 0x1)

    def lambda_1C6E():
        OP_8E(0xFE, 0xFFFEF5FC, 0x0, 0xF28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1C6E)
    WaitChrThread(0x105, 0x1)

    def lambda_1C8E():
        OP_8E(0xFE, 0xFFFEFDCC, 0x0, 0xF28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1C8E)
    WaitChrThread(0x105, 0x1)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8C(0x105, 180, 500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_1CE3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1CE3)

    def lambda_1CF5():
        OP_8E(0xFE, 0xFFFEFDCC, 0x3E8, 0x5DC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1CF5)
    WaitChrThread(0x105, 0x1)
    OP_22(0x7, 0x0, 0x64)
    Sleep(2000)
    OP_63(0x10)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #83
        0x10,
        "#1P真是个奇怪的女孩子啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x11,
        (
            "#5P是一年级的插班生呢。\x01",
            "喏，就是那个传说中的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x10,
        "#1P啊～就是她啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #86
        0x10,
        (
            "#1P那顺便来参观一下\x01",
            "也没什么不好嘛～……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x10, 0x2)
    OP_44(0x11, 0x2)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x5F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x0, (scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-7000, 0, 11400, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x105, -7000, 0, 11400, 180)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2F69)
    EventEnd(0x0)
    Return()

    # Function_11_157F end

    def Function_12_1E86(): pass

    label("Function_12_1E86")

    EventBegin(0x0)
    OP_8C(0x105, 0, 0)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1EB1():
        OP_6D(9440, 4000, 9740, 2000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1EB1)

    def lambda_1EC9():
        OP_67(0, 4640, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1EC9)

    def lambda_1EE1():
        OP_6B(3160, 2000)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_1EE1)
    WaitChrThread(0x19, 0x0)
    SetChrPos(0x105, 8000, 4000, -3540, 0)
    SetChrPos(0x13B, 8500, 4000, -2140, 0)
    SetChrPos(0x152, 7700, 4000, -2500, 0)

    def lambda_1F29():
        OP_8E(0xFE, 0x1E14, 0xFA0, 0x1D4C, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x152, 1, lambda_1F29)
    Sleep(300)

    def lambda_1F49():
        OP_8E(0xFE, 0x2134, 0xFA0, 0x1BE4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_1F49)
    Sleep(100)
    SetChrFlags(0x105, 0x1000)

    def lambda_1F6E():
        OP_8E(0xFE, 0x1F40, 0xFA0, 0x1554, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1F6E)
    WaitChrThread(0x13B, 0x1)
    Sleep(500)

    ChrTalk(    #87
        0x13B,
        "#649F#60W#12P找～到～你～了～……\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #88
        0x13B,
        "#1891F#3S#12P快，乖乖束手就擒吧！！#2S\x02",
    )

    OP_7C(0x32, 0x64, 0xBB8, 0x12C)
    CloseMessageWindow()

    ChrTalk(    #89
        0x152,
        (
            "#732F#6P会长，\x01",
            "拜托别太给人添麻烦吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #90
        0x12,
        (
            "#1774F#5P唔唔、唔唔……\x02\x03",

            "唔唔、唔唔……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x64, 1500, 0x18, 0x1B, 0x12C, 0x0)
    Sleep(2000)
    OP_62(0x13B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x152, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #91
        0x105,
        (
            "#542F#12P那个…………\x01",
            "这，这本书是……？？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #92
        0x12,
        (
            "#1772F#5P《猫语日常会话辞典》。\x02\x03",

            "#1771F喵－呵。\x02\x03",

            "嗯喵☆\x02\x03",

            "呜喵喵～⊙\x02",
        )
    )

    Jump("loc_2186")

    label("loc_2186")

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x152, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x13B, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #93
        0x152,
        (
            "#734F#6P你、你一整天\x01",
            "就在干这个啊……？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x12, 0x64, 1500, 0x8, 0x9, 0xC8, 0x0)
    Sleep(1000)
    OP_62(0x13B, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x13B, 0x3, 0x0, 0xD)
    Sleep(2000)
    FadeToDark(2000, 0, -96)
    OP_A2(0x5)
    OP_0D()
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #94
        (
            "\x18\x07\x0C拼命生活的我闭上双眼，\x01",
            "在广阔空虚的世界中不停奔走。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #95
        (
            "\x18\x07\x0C不是为了做出什么成就。\x01",
            "也不是为了在天空中翱翔。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #96
        (
            "\x18\x07\x0C只是在我踌躇之时，\x01",
            "这小小的箱庭世界已宽广得令人吃惊。 \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(3000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_44(0x13B, 0xFF)
    SetChrName("")

    AnonymousTalk(    #97
        "\x18\x07\x0C#40W―――没错。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #98
        "\x18\x07\x0C#40W我究竟是为何，而来到此处……？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    RemoveParty(0x3A, 0x0)
    RemoveParty(0x51, 0x0)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1E86 end

    def Function_13_23DB(): pass

    label("Function_13_23DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_246D")

    def lambda_23EA():
        OP_8F(0xFE, 0x2134, 0xFA0, 0x21C0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_23EA)
    WaitChrThread(0x13B, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2411")
    OP_22(0x8E, 0x0, 0x32)

    label("loc_2411")


    def lambda_2417():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_2417)

    def lambda_2431():
        OP_9E(0xFE, 0xF, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_2431)

    def lambda_244B():
        OP_8F(0xFE, 0x2134, 0xFA0, 0x1BE4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13B, 1, lambda_244B)
    WaitChrThread(0x13B, 0x1)
    Sleep(500)
    Jump("Function_13_23DB")

    label("loc_246D")

    Return()

    # Function_13_23DB end

    def Function_14_246E(): pass

    label("Function_14_246E")

    EventBegin(0x0)
    OP_6D(-34930, 0, 5630, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    SetChrPos(0x14, -36120, 0, 3440, 0)
    SetChrFlags(0x14, 0x40)
    SetChrPos(0x15, -35750, 0, 5500, 0)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x20)
    ClearChrFlags(0x15, 0x1)
    ClearChrFlags(0x15, 0x100)
    OP_51(0x15, 0x2A, (scpexpr(EXPR_PUSH_LONG, 0xAFC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x2B, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x2C, (scpexpr(EXPR_PUSH_LONG, 0x15F90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x47E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x91), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -36120, -800, 4800, 0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_2593"),
        (107, "loc_25A7"),
        (SWITCH_DEFAULT, "loc_25BB"),
    )


    label("loc_2593")

    SetChrPos(0x105, -36140, 0, 1500, 0)
    Jump("loc_25BB")

    label("loc_25A7")

    SetChrPos(0x105, -40500, 1000, 6540, 90)
    Jump("loc_25BB")

    label("loc_25BB")

    OP_0D()
    Sleep(1000)

    ChrTalk(    #99
        0x14,
        (
            "#649F#12P呼呼呼……可算找到了。\x01",
            "你个呆瓜学生会长……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_260A():
        OP_8E(0xFE, 0xFFFF72E8, 0x0, 0xF00, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_260A)
    WaitChrThread(0x14, 0x1)
    Sleep(300)

    ChrTalk(    #100
        0x14,
        "#1891F#12P#3S来，觉悟吧！！#2S\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x14, 0x4)

    def lambda_265F():
        OP_8E(0xFE, 0xFFFF72E8, 0x0, 0x11F8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_265F)
    WaitChrThread(0x14, 0x1)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(300)

    def lambda_2689():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2689)
    Sleep(1000)

    def lambda_26A8():
        OP_8F(0xFE, 0xFFFF72E8, 0x0, 0xD70, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_26A8)

    def lambda_26C3():
        OP_8F(0xFE, 0xFFFF745A, 0x0, 0x10CC, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_26C3)
    WaitChrThread(0x14, 0x1)
    Sleep(1000)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #101
        0x14,
        (
            "#642F米克，你……\x02\x03",

            "#645F…………在干什么啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x16, -36120, -1000, 4800, 0)
    SetChrPos(0x15, -35750, 0, 4300, 225)
    SetChrFlags(0x15, 0x800)
    OP_0D()
    Sleep(300)
    OP_62(0x16, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #102
        0x16,
        "#1P放、放开我！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x16,
        "#1P我没干什么……！\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (104, "loc_27F4"),
        (107, "loc_2854"),
        (SWITCH_DEFAULT, "loc_28D4"),
    )


    label("loc_27F4")

    OP_22(0x6, 0x0, 0x64)

    def lambda_27FF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_27FF)
    WaitChrThread(0x105, 0x2)
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1300)

    ChrTalk(    #104
        0x105,
        "#044F…………咦？？\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D4")

    label("loc_2854")


    def lambda_285A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_285A)

    def lambda_286C():
        OP_8E(0xFE, 0xFFFF6870, 0x3E8, 0x198C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_286C)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 135, 400)
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1300)

    ChrTalk(    #105
        0x105,
        "#044F#5P…………咦？？\x02",
    )

    CloseMessageWindow()
    Jump("loc_28D4")

    label("loc_28D4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-34850, 1000, 10060, 0)
    OP_67(0, 4400, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x15, -35330, 1000, 8510, 270)
    SetChrFlags(0x15, 0x40)
    ClearChrFlags(0x15, 0x800)
    ClearChrFlags(0x15, 0x4)
    ClearChrFlags(0x15, 0x20)
    SetChrFlags(0x15, 0x1)
    SetChrFlags(0x15, 0x100)
    SetChrFlags(0x16, 0x80)
    OP_51(0x15, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x105, -37090, 1000, 7760, 90)
    SetChrPos(0x14, -37220, 1000, 8900, 90)
    ClearChrFlags(0x14, 0x4)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #106
        0x15,
        (
            "#11P都说了，\x01",
            "我没干什么坏事啦～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x14,
        (
            "#646F#6P那你干嘛\x01",
            "躲在这种地方啊。\x02\x03",

            "怎么看都很可疑啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x15,
        (
            "#11P不、不是，我也是这么想着\x01",
            "所以要确认一下……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #109
        0x14,
        "#643F#6P确认一下…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x105,
        (
            "#044F#6P嗯，\x01",
            "要确认什么呢……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x15,
        "#11P啊啊，其实刚才……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x15,
        (
            "#11P我看到校舍后面，\x01",
            "有个很不正经的家伙\x01",
            "走了过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x15,
        (
            "#11P而且至今为止\x01",
            "从来没见过那么\x01",
            "不正经的家伙。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #114
        0x105,
        "#045F#6P（为、为什么……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x14,
        (
            "#645F#6P（我一下子\x01",
            "　就知道是谁了……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x15,
        (
            "#11P那个邋遢样子\x01",
            "实在是太夸张了，\x01",
            "连我都起了疑心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x15,
        "#11P所以就尾随着他。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x15,
        (
            "#11P然后那家伙，\x01",
            "四下里望望\x01",
            "就进了礼堂……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x15,
        "#11P怎么看都很可疑吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x14,
        "#647F#6P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x15,
        (
            "#11P我也悄悄追了上来，\x01",
            "但是在这里打了个照面……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x15,
        (
            "#11P他看到我的脸\x01",
            "就慌忙跑到这下面去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x15,
        (
            "#11P我也正打算进去，\x01",
            "可是中途被抓住……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x15,
        "#11P可恶，就差一点点了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x14,
        "#645F#6P…………唉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x105,
        (
            "#045F#6P唔，这个……\x02\x03",

            "应该是被雷克特学长\x01",
            "耍弄了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x15,
        "#11P哎…………？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x14,
        (
            "#647F#6P米克，\x01",
            "都怪你总是想着偷懒。\x02\x03",

            "#649F所以他才故意做出\x01",
            "引人注意的样子来骗你。\x02\x03",

            "这算是那个学生会长的\x01",
            "特长之一吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #129
        0x15,
        "#11P怎、怎么会……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x15,
        "#11P那家伙，居然是学生会长吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x15,
        (
            "#11P难以置信，\x01",
            "那么邋遢的样子……！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x105,
        (
            "#045F#6P啊、啊哈哈……\x02\x03",

            "（事到如今你说这话也……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-37200, 1000, 6860, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_4B(0x14, 255)
    OP_4B(0x15, 255)
    ClearChrFlags(0x14, 0x40)
    ClearChrFlags(0x15, 0x40)
    SetChrPos(0x105, -37090, 1000, 7760, 90)
    SetChrPos(0x14, -37220, 1000, 8900, 90)
    SetChrPos(0x15, -35330, 1000, 8510, 270)
    OP_69(0x0, 0x0)
    OP_A2(0x2F71)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_14_246E end

    SaveToFile()

Try(main)
