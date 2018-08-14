from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0110   ._SN',
        MapName             = 'event',
        Location            = 'E0110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        '乔丝特',                               # 9
        '吉尔',                                 # 10
        '多伦',                                 # 11
        '乘务员雷古',                           # 12
        '乘务员阿伦',                           # 13
        '乘务员洛西',                           # 14
        '乘务员罗尔',                           # 15
        '乘务员雷古',                           # 16
        '乘务员雷古',                           # 17
        '乘务员的声音',                         # 18
        '目标用照相机',                         # 19
        '封印石④',                             # 20
        '',                                     # 21
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03100 ._CH',             # 00
        'ED6_DT26/CH20416 ._CH',             # 01
        'ED6_DT27/CH03760 ._CH',             # 02
        'ED6_DT07/CH01380 ._CH',             # 03
        'ED6_DT27/CH03761 ._CH',             # 04
        'ED6_DT27/CH03101 ._CH',             # 05
        'ED6_DT27/CH03771 ._CH',             # 06
        'ED6_DT26/CH20621 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT27/CH03100P._CP',             # 00
        'ED6_DT26/CH20416P._CP',             # 01
        'ED6_DT27/CH03760P._CP',             # 02
        'ED6_DT07/CH01380P._CP',             # 03
        'ED6_DT27/CH03761P._CP',             # 04
        'ED6_DT27/CH03101P._CP',             # 05
        'ED6_DT27/CH03771P._CP',             # 06
        'ED6_DT26/CH20621P._CP',             # 07
    )

    DeclNpc(
        X                   = 45640,
        Z                   = 0,
        Y                   = 6930,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -21870,
        Z                   = 850,
        Y                   = 4940,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 47460,
        Z                   = 0,
        Y                   = 76210,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -24300,
        Z                   = -1000,
        Y                   = 4970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 45780,
        Z                   = 0,
        Y                   = 6950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 51430,
        Z                   = 0,
        Y                   = 2760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -24200,
        Z                   = -250,
        Y                   = 4300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -24370,
        Z                   = -250,
        Y                   = 5510,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        NpcIndex            = 0xCC,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -17680,
        TriggerZ            = 0,
        TriggerY            = 3110,
        TriggerRange        = 1500,
        ActorX              = -17800,
        ActorZ              = 4300,
        ActorY              = 4950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -22380,
        TriggerZ            = 650,
        TriggerY            = 5380,
        TriggerRange        = 1000,
        ActorX              = -22380,
        ActorZ              = 1650,
        ActorY              = 5380,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B2",          # 00, 0
        "Function_1_34A",          # 01, 1
        "Function_2_558",          # 02, 2
        "Function_3_56E",          # 03, 3
        "Function_4_5C8",          # 04, 4
        "Function_5_5CF",          # 05, 5
        "Function_6_636",          # 06, 6
        "Function_7_742",          # 07, 7
        "Function_8_84C",          # 08, 8
        "Function_9_27F6",         # 09, 9
        "Function_10_2842",        # 0A, 10
        "Function_11_2887",        # 0B, 11
        "Function_12_2B91",        # 0C, 12
        "Function_13_2E2A",        # 0D, 13
        "Function_14_309D",        # 0E, 14
        "Function_15_4203",        # 0F, 15
        "Function_16_4827",        # 10, 16
    )


    def Function_0_2B2(): pass

    label("Function_0_2B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE")

    label("loc_2BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_349")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_2E4")
    OP_A3(0x2508)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_349")

    label("loc_2E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_2FE")
    OP_A3(0x2507)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)
    Jump("loc_349")

    label("loc_2FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_318")
    OP_A3(0x2506)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 12)
    Jump("loc_349")

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_332")
    OP_A3(0x2505)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x52), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)
    Jump("loc_349")

    label("loc_332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_349")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_349")

    Return()

    # Function_0_2B2 end

    def Function_1_34A(): pass

    label("Function_1_34A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_362")
    OP_B1("E0110_n")
    Jump("loc_37E")

    label("loc_362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_375")
    OP_B1("E0110_n")
    Jump("loc_37E")

    label("loc_375")

    OP_B1("E0110_y")

    label("loc_37E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_455")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_446")
    ClearChrFlags(0x1B, 0x80)
    OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1B, -17800, 4300, 4950, 0)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    PlayEffect(0x7, 0x7, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_44A")

    label("loc_446")

    OP_64(0x0, 0x1)

    label("loc_44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_455")
    OP_64(0x1, 0x1)

    label("loc_455")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B4")
    OP_10(0x0, 0x0)
    OP_10(0x6, 0x1)
    OP_22(0x7A, 0x1, 0x50)
    OP_76(0x7, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x7, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x7, 0x2, 0x1, 0xFFFFFFFE, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_4D9")

    label("loc_4B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_4D3")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x1)
    OP_10(0x6, 0x0)
    Jump("loc_4D9")

    label("loc_4D3")

    OP_10(0x0, 0x1)
    OP_10(0x6, 0x0)

    label("loc_4D9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_529")
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_76(0x4, 0x5, 0x2, 0x4, 0x8, 0x0, 0x0, 0x0)
    Jump("loc_557")

    label("loc_529")

    OP_71(0x40E, 0x0)
    ExitThread()
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_64(0x0, 0x1)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()

    label("loc_557")

    Return()

    # Function_1_34A end

    def Function_2_558(): pass

    label("Function_2_558")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_558")

    label("loc_56D")

    Return()

    # Function_2_558 end

    def Function_3_56E(): pass

    label("Function_3_56E")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0x11,
        (
            "#200F不好意思，\x01",
            "能帮我找下大哥吗？\x02\x03",

            "我想再确认一下\x01",
            "送货的地址。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_56E end

    def Function_4_5C8(): pass

    label("Function_4_5C8")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_4_5C8 end

    def Function_5_5CF(): pass

    label("Function_5_5CF")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        (
            "老大……啊，不，\x01",
            "老板从今天早上起也一直忙着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "现在一定是累坏了，\x01",
            "还在睡午觉吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_5CF end

    def Function_6_636(): pass

    label("Function_6_636")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C8")
    OP_A2(0x3)

    ChrTalk(    #3
        0xFE,
        "真是辛苦了!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "如果告诉母亲说当上了货运员，\x01",
            "母亲一定会十分高兴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "呵呵，看来今年总算可以\x01",
            "回久违的家乡看看了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73E")

    label("loc_6C8")


    ChrTalk(    #6
        0xFE,
        (
            "如果告诉母亲说当上了货运员，\x01",
            "母亲一定会十分高兴的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "一直让父母操心到现在，\x01",
            "我可要好好赚钱，孝顺父母啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73E")

    TalkEnd(0xFE)
    Return()

    # Function_6_636 end

    def Function_7_742(): pass

    label("Function_7_742")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DC")
    OP_A2(0x4)

    ChrTalk(    #8
        0xFE,
        "啊，小、小姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "竟然能让我这个\x01",
            "曾经从空贼团逃出来的人\x01",
            "成为公司的员工……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "我、我一辈子都报答不完\x01",
            "大哥们对我的恩情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_848")

    label("loc_7DC")


    ChrTalk(    #11
        0xFE,
        (
            "既然已经改邪归正了，\x01",
            "就一定要洗心革面，好好加油。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "要抱着若犯错就断指的觉悟\x01",
            "十二分地努力工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_848")

    TalkEnd(0xFE)
    Return()

    # Function_7_742 end

    def Function_8_84C(): pass

    label("Function_8_84C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-23640, 0, 7960, 0)
    OP_67(0, 5200, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(330000, 0)
    OP_6E(280, 0)
    OP_22(0x7A, 0x1, 0x50)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x10B, 0x40)
    SetChrPos(0x11, -24260, -1000, 4970, 270)
    SetChrPos(0x12, -21870, 650, 4940, 315)
    SetChrPos(0x10B, -18620, 3000, 4800, 270)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    OP_76(0xB, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x1, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x2, 0x1, 0xFFFFFFFC, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(2000, 0)
    OP_6B(3000, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #13
        0x10B,
        (
            "#210F在起伏的群山对面\x01",
            "可以看到瓦雷利亚湖了――\x02\x03",

            "嗯，\x01",
            "看来国境线就近在眼前了。\x02",
        )
    )

    Jump("loc_9CA")

    label("loc_9CA")

    CloseMessageWindow()

    ChrTalk(    #14
        0x12,
        (
            "#190F#0CＯＫ，就按原定计划进行。\x02\x03",

            "吉尔，推力６０％――\x01",
            "方向和高度维持原样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x11,
        (
            "#200F明白，推力降低到６０％――\x02\x03",

            "……方向和高度设定完毕。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(200)

    ChrTalk(    #16
        0x12,
        (
            "#490F好的……\x01",
            "已进入规定的航路。\x02\x03",

            "然后就保持现状，\x01",
            "直接朝目的地飞行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x11,
        "#203F呼，总算可以松一口气了。\x02",
    )

    CloseMessageWindow()

    def lambda_B1F():
        OP_8F(0xFE, 0xFFFFB8D4, 0xBB8, 0x12C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_B1F)
    WaitChrThread(0x10B, 0x1)
    Sleep(500)

    ChrTalk(    #18
        0x10B,
        (
            "#211F你们两个，都辛苦了。\x02\x03",

            "哈哈，今天也按时顺利赶到了，\x01",
            "这比什么都好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x12,
        (
            "#191F嗯，确实如此。\x02\x03",

            "我们卡普亚特急便\x01",
            "是以客人的笑脸、信赖、安心\x01",
            "为宗旨的货运公司嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#202F嘿嘿，这可是以前当空贼时\x01",
            "完全无法想象的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10B,
        (
            "#210F嗯，这都是多亏了\x01",
            "艾莉茜雅女王的恩赦，\x01",
            "我们才会有今天。\x02\x03",

            "当听到无罪释放的时候，\x01",
            "我真是大吃了一惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "#200F嗯，\x01",
            "而且还用她自己的钱\x01",
            "偿还了我们的借款。\x02\x03",

            "托她的福，\x01",
            "山猫号也没有被没收。\x02\x03",

            "对女王的敬意，\x01",
            "这一辈子都无法改变啊。\x02",
        )
    )

    Jump("loc_D51")

    label("loc_D51")

    CloseMessageWindow()

    ChrTalk(    #23
        0x12,
        (
            "#490F嗯，确实如此。\x02\x03",

            "为了回报女王的恩情，\x01",
            "还是要尽快把钱\x01",
            "还给女王才是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10B,
        (
            "#211F嗯，按照现在的收入情况，\x01",
            "用不了多久就一定能还清了。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    LoadEffect(0x1, "map\\\\mp001_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -22580, 1700, 5540, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x0)
    OP_8C(0x12, 240, 500)
    Sleep(300)

    ChrTalk(    #25
        0x10B,
        (
            "#415F嘿嘿，正说着呢，\x01",
            "就来了新的工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x12,
        "#198F啊、啊～……咳咳。\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x83, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x12,
        (
            "#190F喂，这里是卡普亚特急便！\x02\x03",

            "是……\x01",
            "哎，是的……\x02\x03",

            "……明天上午？\x01",
            "好，没问题。\x02\x03",

            "#198F知道了。\x01",
            "那就当天前去拜访您了。\x02",
        )
    )

    Jump("loc_F62")

    label("loc_F62")

    CloseMessageWindow()
    OP_59()
    OP_22(0x83, 0x0, 0x64)
    Sleep(300)
    OP_8C(0x12, 315, 400)
    Sleep(300)

    ChrTalk(    #28
        0x10B,
        "#415F哪里来的工作？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x12,
        (
            "#490F啊，\x01",
            "这次也是来自共和国的委托哦。\x02\x03",

            "有个包裹\x01",
            "需要送到格兰赛尔。\x02",
        )
    )

    Jump("loc_1002")

    label("loc_1002")

    CloseMessageWindow()

    ChrTalk(    #30
        0x11,
        (
            "#200F去王都的话……\x01",
            "明后天正好有航行安排。\x02\x03",

            "哈哈，生意真是兴隆啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10B,
        (
            "#211F呵呵，比这更灵活方便的运输方法，\x01",
            "业界应该是找不到第二家了。\x02\x03",

            "#213F这么说来，多伦哥。\x01",
            "说到王都我才想起来……\x02\x03",

            "#210F今天早上，\x01",
            "你去了王都的游击士协会吧。\x02\x03",

            "到底什么事啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #32
        0x12,
        (
            "#192F……哎呀，是这样。\x02\x03",

            "我都忘了说了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10B,
        "#213F什么啊，多伦哥？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 100, 500)
    Sleep(300)

    ChrTalk(    #34
        0x12,
        (
            "#490F事实上，\x01",
            "从帝国来了封给我们的信，\x02\x03",

            "听了别太惊讶哦……\x02\x03",

            "#191F寄信的是约修亚那小子。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #35
        0x10B,
        "#414F真、真的！？\x02",
    )

    CloseMessageWindow()

    def lambda_127A():
        OP_67(-23640, 0, 8150, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_127A)

    def lambda_1292():
        OP_67(0, 5050, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1292)

    def lambda_12AA():
        OP_8E(0xFE, 0xFFFFB9B0, 0xBB8, 0x10CC, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_12AA)
    WaitChrThread(0x10B, 0x1)
    OP_22(0xA3, 0x0, 0x50)

    def lambda_12CF():
        OP_96(0xFE, 0xFFFFBBA4, 0x0, 0xA50, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_12CF)
    WaitChrThread(0x10B, 0x1)
    OP_23(0xA3)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_12FA():
        OP_8E(0xFE, 0xFFFFB758, 0x0, 0xA50, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_12FA)
    WaitChrThread(0x10B, 0x1)

    def lambda_131A():
        OP_8E(0xFE, 0xFFFFB758, 0x0, 0x12C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_131A)
    WaitChrThread(0x10B, 0x1)

    def lambda_133A():
        OP_8E(0xFE, 0xFFFFAF24, 0x0, 0x12C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_133A)
    WaitChrThread(0x10B, 0x1)
    Sleep(300)

    ChrTalk(    #36
        0x11,
        "#202F嘿～那可真是少有啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10B,
        (
            "#212F就是说嘛，\x01",
            "为什么不早些告诉我呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x12,
        (
            "#490F#5P啊哈哈，抱歉抱歉～\x01",
            "因为早上慌慌忙忙的。\x02\x03",

            "对了，乔丝特。\x01",
            "你能念给我听听吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10B,
        "#415F嘿嘿，当然可以啦。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x10B, 0x4)

    def lambda_1447():
        OP_8E(0xFE, 0xFFFFAD6C, 0x28A, 0x1360, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_1447)
    WaitChrThread(0x10B, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        "\x07\x05从多伦那里接过信封。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    def lambda_14AA():
        OP_8F(0xFE, 0xFFFFAF24, 0x28A, 0x12C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_14AA)
    WaitChrThread(0x10B, 0x1)
    ClearChrFlags(0x10B, 0x4)
    Sleep(300)

    ChrTalk(    #41
        0x10B,
        "#415F稍等一下……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_8C(0x10B, 100, 500)
    Sleep(300)
    OP_62(0x10B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #42
        0x11,
        (
            "#200F我记得他应该是在周游帝国吧。\x02\x03",

            "现在有没有什么进展呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x12, 270, 400)
    Sleep(300)

    ChrTalk(    #43
        0x12,
        (
            "#490F#5P确实，不知他现在到了什么地方呢。\x02\x03",

            "帝国之中\x01",
            "也有各种各样的地方啊。\x02",
        )
    )

    Jump("loc_15D5")

    label("loc_15D5")

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        "#202F啊，只要过得好就行了……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 1)
    Sleep(500)

    ChrTalk(    #45
        0x11,
        (
            "#200F嗯？怎么了，乔丝特？\x01",
            "快点念给我听啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10B)
    Sleep(500)

    ChrTalk(    #46
        0x10B,
        "#416F#5P……０７：００，古代艺术品……\x02",
    )

    CloseMessageWindow()
    Sleep(800)
    OP_8C(0x12, 100, 500)
    Sleep(300)

    ChrTalk(    #47
        0x12,
        "#490F#5P啊？那是什么啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x11,
        (
            "#206F……乔丝特？\x01",
            "到底写了些什么啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x10B, 270, 500)
    Sleep(300)

    ChrTalk(    #49
        0x10B,
        (
            "#212F你还问写了些什么的……\x02\x03",

            "这个……\x01",
            "不正是今早投递的发票吗？\x02",
        )
    )

    Jump("loc_1757")

    label("loc_1757")

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #50
        0x12,
        "#192F#5P#3S什么！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #51
        0x11,
        "#206F……哎？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10B,
        (
            "#212F这个……\x01",
            "明明应该已经交给\x01",
            "收货人的才对啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x12,
        "#192F#5P难、难道是……！？\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 0)
    Sleep(500)

    ChrTalk(    #54
        0x11,
        "#203F啊……不好的预感。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10B,
        "#416F……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x12,
        (
            "#190F#5P那小子寄来的信\x01",
            "是装在帝国发行的信封中的。\x02\x03",

            "同样的，今天早上的发票也是\x01",
            "装在帝国发行的信封中的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x11,
        "#204F也就是说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x12,
        (
            "#197F#5P对不起……\x02\x03",

            "看起来，\x01",
            "是把信错贴在货物上了。\x02",
        )
    )

    Jump("loc_197E")

    label("loc_197E")

    CloseMessageWindow()

    ChrTalk(    #59
        0x10B,
        "#417F………………\x02",
    )

    CloseMessageWindow()

    def lambda_19A3():
        OP_9E(0xFE, 0x7, 0x0, 0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_19A3)
    Sleep(500)

    ChrTalk(    #60
        0x11,
        "#203F唉，这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x12,
        (
            "#192F#5P总，总之，\x01",
            "赶快先联络投递处！\x02\x03",

            "肯定和货物夹在一起呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x10B, 0x2)
    Sleep(500)

    ChrTalk(    #62
        0x10B,
        "#418F#5S多伦哥大笨蛋！！！#2S\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x12C)
    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        "#205F哇！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x12,
        "#192F#5P哇～～！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10B,
        (
            "#418F怎么会犯这样的错误啊！\x02\x03",

            "真是不可想像！\x02\x03",

            "#417F本来听到从约修亚那里来了信，\x01",
            "还挺高兴的…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x11,
        "#207F乔丝特……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x12,
        (
            "#197F#5P对不起，乔丝特。\x02\x03",

            "这全是我的责任。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10B)
    Sleep(500)

    ChrTalk(    #68
        0x10B,
        (
            "#416F大哥总是这样。\x02\x03",

            "从以前开始就一直这么粗枝大叶……\x02\x03",

            "#214F总是给大家带来那么多麻烦，\x01",
            "知道吗？\x02",
        )
    )

    Jump("loc_1C22")

    label("loc_1C22")

    CloseMessageWindow()

    ChrTalk(    #69
        0x12,
        "#198F#5P啊，嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        (
            "#206F喂～我说乔丝特。\x01",
            "现在还不能肯定\x01",
            "信已经丢掉了呢。\x02\x03",

            "你也不应该说到这种地步……\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    ChrTalk(    #71
        0x10B,
        "#214F#4S吉尔哥给我闭嘴！#2S\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0xC8)
    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #72
        0x11,
        "#201F什……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10B,
        (
            "#212F对了，从以前开始就是这样。\x02\x03",

            "#215F那个时候也是……\x01",
            "随便就跟人签约，结果被骗得好惨……\x02\x03",

            "我们那么……\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    ChrTalk(    #74
        0x11,
        "#201F#4S乔丝特！！#2S\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0xC8)
    CloseMessageWindow()
    OP_59()
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1DF0():
        OP_8C(0xFE, 240, 500)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_1DF0)

    ChrTalk(    #75
        0x10B,
        "#216F哇！？\x02",
    )

    Sleep(1000)
    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 1)
    Sleep(500)

    ChrTalk(    #76
        0x11,
        (
            "#204F……你说得太过分了。\x02\x03",

            "大哥已经反省过了。\x02\x03",

            "#207F而且……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10B,
        "#213F……哎？\x02",
    )

    CloseMessageWindow()
    OP_20(0xFA0)
    OP_8C(0x10B, 280, 400)
    Sleep(500)

    ChrTalk(    #78
        0x12,
        (
            "#198F#5P#40W……没错，说起来都是我的错。\x02\x03",

            "当初，如果我能干得好点……\x01",
            "现在也不至于被迫流落他乡啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10B,
        "#215F……啊……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 0)
    Sleep(500)

    ChrTalk(    #80
        0x11,
        (
            "#203F哎，你啊……\x02\x03",

            "怎么也不至于\x01",
            "扯到那个话题上吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x10B, 0x1, 0x0, 0x9)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(500)
    OP_1D(0x53)
    OP_AD(0x240066, 0x0, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(250, 20, -1, -1)
    SetChrName("多伦")

    AnonymousTalk(    #81
        (
            "\x07\x0C#40W本来，现在我们应该是\x01",
            "在祖传的土地上过着优雅的生活……\x02",
        )
    )

    Jump("loc_2016")

    label("loc_2016")

    CloseMessageWindow()

    AnonymousTalk(    #82
        "\x07\x0C#40W弹着乐器，喝着红茶……\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #83
        (
            "\x07\x0C#40W偶尔，\x01",
            "也会去参加一下宴会之类的活动。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 250, -1, -1)
    SetChrName("吉尔")

    AnonymousTalk(    #84
        "\x07\x0C喂喂，我说大哥……\x02",
    )

    Jump("loc_20A9")

    label("loc_20A9")

    CloseMessageWindow()

    AnonymousTalk(    #85
        (
            "\x07\x0C事到如今，\x01",
            "谁也没有再留恋那时候的生活了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("乔丝特")

    AnonymousTalk(    #86
        "\x07\x0C#40W……………\x02",
    )

    Jump("loc_2116")

    label("loc_2116")

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_AD(0x240067, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(120, 20, -1, -1)
    SetChrName("多伦")

    AnonymousTalk(    #87
        (
            "\x07\x0C#40W被眼前的欲望所蒙蔽，\x01",
            "让花言巧语乘虚而入……\x02",
        )
    )

    Jump("loc_2185")

    label("loc_2185")

    CloseMessageWindow()

    AnonymousTalk(    #88
        (
            "\x07\x0C#40W恍然大悟的时候，\x01",
            "剩下的仅仅是难以偿还的债务。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #89
        "\x07\x0C#40W明明是老爸留下的财产……\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #90
        "\x07\x0C#40W就算再笨也该有个限度啊。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 300, -1, -1)
    SetChrName("吉尔")

    AnonymousTalk(    #91
        (
            "\x07\x0C那个……\x01",
            "也不是大哥一个人的错。\x02",
        )
    )

    Jump("loc_2264")

    label("loc_2264")

    CloseMessageWindow()

    AnonymousTalk(    #92
        (
            "\x07\x0C只是因为我们几个……\x01",
            "几个小孩子不懂世事而已。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0xC8)
    Sleep(2000)
    OP_43(0x10B, 0x1, 0x0, 0xA)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #93
        0x12,
        "#198F#5P#40W就算是那样，我也……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 1)
    Sleep(500)

    ChrTalk(    #94
        0x11,
        "#206F乔丝特，你也说点什么吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x10B,
        "#215F#40W…………………………\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 0)
    Sleep(500)

    ChrTalk(    #96
        0x11,
        "#203F……呼……唉。\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_20(0x0)
    PlayEffect(0x1, 0x0, 0xFF, -22600, 1700, 5520, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(300)
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(300)
    OP_1D(0x52)
    Sleep(500)
    OP_82(0x0, 0x0)

    ChrTalk(    #97
        0x11,
        "#201F怎、怎么了……！?\x02",
    )

    CloseMessageWindow()

    def lambda_2464():
        OP_8C(0xFE, 240, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2464)
    Sleep(100)
    OP_8C(0x10B, 240, 500)
    Sleep(300)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -23300, 650, 4780, 0)

    ChrTalk(    #98
        0x19,
        (
            "#5C#5P不、不好了！\x01",
            "老大……不对，老板！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x12,
        "#192F#0C#6P怎、怎么回事！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x19,
        (
            "#5C#5P那、那个……\x01",
            "后方出现了红色飞艇的身影。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x19,
        "#5C#5P那个……好像是结社的飞艇。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x10B,
        "#216F#0C……哎！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10B, 100, 600)

    def lambda_2584():
        OP_67(0, 4300, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2584)

    def lambda_259C():
        OP_6D(-23640, -300, 7960, 1000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_259C)

    def lambda_25B4():
        OP_6C(325000, 1000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_25B4)

    def lambda_25C4():
        OP_8E(0xFE, 0xFFFFB758, 0x0, 0x12C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_25C4)
    WaitChrThread(0x10B, 0x1)

    def lambda_25E4():
        OP_8E(0xFE, 0xFFFFB758, 0x0, 0xA50, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_25E4)
    WaitChrThread(0x10B, 0x1)

    def lambda_2604():
        OP_8E(0xFE, 0xFFFFBBA4, 0x0, 0xA50, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_2604)
    WaitChrThread(0x10B, 0x1)
    OP_8C(0x10B, 330, 600)

    def lambda_262B():
        OP_67(0, 5100, -10000, 500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_262B)

    def lambda_2643():
        OP_6D(-23640, 0, 7960, 500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2643)

    def lambda_265B():
        OP_6C(330000, 500)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_265B)
    Fade(500)
    SetChrPos(0x10B, -18100, 3000, 4140, 330)
    OP_0D()
    OP_22(0xA4, 0x0, 0x64)

    def lambda_2687():
        OP_8E(0xFE, 0xFFFFB744, 0xBB8, 0x12C0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_2687)
    WaitChrThread(0x10B, 0x1)
    OP_8C(0x10B, 270, 600)
    Sleep(300)

    ChrTalk(    #103
        0x12,
        "#197F#0C#5P嘁，这下可麻烦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x11,
        "#206F#0C大哥……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x12,
        (
            "#198F#5P啊啊，没有时间准备迎战了。\x02\x03",

            "#196F优先确保货物的安全！\x01",
            "全速甩开他们！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x11,
        "#201F明白！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x12,
        (
            "#196F#5P小子们，都听得见吧！\x01",
            "紧急事态发生了！\x02\x03",

            "以防卷入战斗，\x01",
            "大家给我各自盯紧点！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_84C end

    def Function_9_27F6(): pass

    label("Function_9_27F6")

    OP_24(0x7A, 0x50)
    Sleep(100)
    OP_24(0x7A, 0x46)
    Sleep(100)
    OP_24(0x7A, 0x3C)
    Sleep(100)
    OP_24(0x7A, 0x32)
    Sleep(100)
    OP_24(0x7A, 0x28)
    Sleep(100)
    OP_24(0x7A, 0x1E)
    Sleep(100)
    OP_24(0x7A, 0x14)
    Sleep(100)
    OP_24(0x7A, 0xA)
    Sleep(100)
    OP_23(0x7A)
    Return()

    # Function_9_27F6 end

    def Function_10_2842(): pass

    label("Function_10_2842")

    OP_22(0x7A, 0x1, 0xA)
    Sleep(200)
    OP_24(0x7A, 0x14)
    Sleep(200)
    OP_24(0x7A, 0x1E)
    Sleep(200)
    OP_24(0x7A, 0x28)
    Sleep(200)
    OP_24(0x7A, 0x32)
    Sleep(200)
    OP_24(0x7A, 0x3C)
    Sleep(200)
    OP_24(0x7A, 0x46)
    Sleep(200)
    OP_24(0x7A, 0x50)
    Return()

    # Function_10_2842 end

    def Function_11_2887(): pass

    label("Function_11_2887")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(-23640, 0, 7960, 0)
    OP_67(0, 5100, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(330000, 0)
    OP_6E(280, 0)
    OP_22(0x7A, 0x1, 0x64)
    OP_76(0xB, 0x0, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x10B, 0x40)
    SetChrPos(0x11, -24260, -1000, 4970, 270)
    SetChrPos(0x12, -21870, 650, 4940, 315)
    SetChrPos(0x10B, -18620, 3000, 4800, 270)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #108
        0x12,
        "#199F乔丝特，看到了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x10B,
        (
            "#212F嗯、嗯……\x01",
            "和后方结社飞艇一起的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x12,
        "#192F什么，怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x10B,
        (
            "#214F还有几台从未见过的兵器……\x01",
            "全部朝这边过来了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x12,
        (
            "#197F哎呀～\x01",
            "完全被他们盯上了……\x02\x03",

            "#199F乔丝特，你就待在那里\x01",
            "用后方的机枪迎击！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x10B,
        "#212F……嗯，知道了！\x02",
    )

    CloseMessageWindow()
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #114
        0x12,
        (
            "#190F现在切换到机枪模式。\x02\x03",

            "怎样，可以正常运作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10B,
        (
            "#212F嗯，没问题！\x02\x03",

            "那就开始迎击吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_6B(3500, 3000)
    OP_0D()
    OP_C0(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_11_2887 end

    def Function_12_2B91(): pass

    label("Function_12_2B91")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-23640, 0, 7960, 0)
    OP_67(0, 5100, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(330000, 0)
    OP_6E(280, 0)
    OP_22(0x7A, 0x1, 0x5A)
    OP_76(0xB, 0x0, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x10B, 0x40)
    SetChrPos(0x11, -24260, -1000, 4970, 270)
    SetChrPos(0x12, -21870, 650, 4940, 315)
    SetChrPos(0x10B, -18620, 3000, 4800, 270)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #116
        0x10B,
        "#212F呼，已经赶走他们了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x12,
        (
            "#190F不知道……\x01",
            "总之，现在还不能放松警惕。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #118
        0x12,
        (
            "#192F乔丝特！\x01",
            "右后方传来了热能反应。\x02\x03",

            "你能确认一下吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x10B,
        (
            "#213F嗯，好的……\x02\x03",

            "是什么呢……?\x01",
            "好像有人乘在上面……\x02\x03",

            "#216F朝、朝这边来了……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2DD3():
        OP_6D(-38560, -2440, 14200, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_2DD3)

    def lambda_2DEB():
        OP_67(0, 3500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2DEB)

    def lambda_2E03():
        OP_6C(304000, 3000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_2E03)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_2B91 end

    def Function_13_2E2A(): pass

    label("Function_13_2E2A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(-23640, 0, 7960, 0)
    OP_67(0, 5100, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(330000, 0)
    OP_6E(280, 0)
    OP_22(0x7A, 0x1, 0x5A)
    OP_76(0xB, 0x0, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x1, 0x1, 0xFFFFFFFD, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x10B, 0x40)
    SetChrPos(0x11, -24260, -1000, 4970, 270)
    SetChrPos(0x12, -21870, 650, 4940, 315)
    SetChrPos(0x10B, -18620, 3000, 4800, 270)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)

    def lambda_2F1C():

        label("loc_2F1C")

        OP_7C(0xF, 0xF, 0xBB8, 0x64)
        OP_48()
        Jump("loc_2F1C")

    QueueWorkItem2(0x11, 3, lambda_2F1C)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #120
        0x11,
        "#206F……不行啊，甩不掉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x12,
        (
            "#197F到底是个什么鬼东西啊。\x02\x03",

            "#196F吉尔，不能减速啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x11,
        "#201F哎呀，我知道！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x12,
        (
            "#199F乔丝特……就算是一瞬间也好，\x01",
            "能帮忙制造出突围的空当来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x10B,
        (
            "#212F嗯，交给我吧……\x02\x03",

            "#214F我会努力试试看的！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C0(0x11, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_13_2E2A end

    def Function_14_309D(): pass

    label("Function_14_309D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(-23640, 0, 7960, 0)
    OP_67(0, 5270, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(330000, 0)
    OP_6E(280, 0)
    OP_22(0x7A, 0x1, 0x50)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x10B, 0x40)
    SetChrPos(0x11, -24260, -1000, 4970, 270)
    SetChrPos(0x12, -21870, 650, 4940, 315)
    SetChrPos(0x10B, -18620, 3000, 4800, 270)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    OP_76(0xB, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x1, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xB, 0x2, 0x1, 0xFFFFFFFC, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #125
        0x10B,
        "#213F成、成功了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x11,
        (
            "#204F啊啊……\x01",
            "那个好像坠入瓦雷利亚湖了。\x02\x03",

            "#200F不用担心给地面居民造成伤害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x12,
        (
            "#490F结社那帮家伙\x01",
            "好像也已经夹着尾巴逃跑了。\x02\x03",

            "#191F干得太好了，乔丝特！\x02\x03",

            "刚才要不是你射落那帮家伙的话，\x01",
            "现在落入湖底的\x01",
            "也许就是我们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x11,
        "#202F啊，真是干得漂亮。\x02",
    )

    CloseMessageWindow()

    def lambda_32F2():
        OP_8F(0xFE, 0xFFFFB8D4, 0xBB8, 0x12C0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_32F2)
    WaitChrThread(0x10B, 0x1)
    Sleep(300)

    ChrTalk(    #129
        0x10B,
        (
            "#415F嘿嘿，你们俩称赞过头啦。\x02\x03",

            "就算再过一会儿，\x01",
            "吉尔哥也一定能甩掉他们的。\x02\x03",

            "而且，\x01",
            "多亏有了多伦哥的指挥。\x02\x03",

            "#213F……啊。\x02",
        )
    )

    Jump("loc_33B3")

    label("loc_33B3")

    CloseMessageWindow()
    OP_8C(0x12, 100, 500)
    Sleep(300)

    ChrTalk(    #130
        0x12,
        (
            "#192F怎、怎么了，乔丝特！？\x02\x03",

            "#198F………啊，对了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x11,
        (
            "#206F……嗯？\x02\x03",

            "难道说……\x01",
            "你们两个都还在闹别扭啊。\x02\x03",

            "#203F唉，该说你们是不坦率呢，\x01",
            "还是……\x02\x03",

            "#200F好了，乔丝特。\x01",
            "要是有什么话想说的话，\x01",
            "就爽快地说出来吧！\x02",
        )
    )

    Jump("loc_34CC")

    label("loc_34CC")

    CloseMessageWindow()

    ChrTalk(    #132
        0x10B,
        (
            "#215F嗯、嗯……\x02\x03",

            "……………………………\x02\x03",

            "#413F……对不起，多伦哥。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #133
        0x12,
        (
            "#192F乔、乔丝特……\x01",
            "你原谅我了吗。\x02\x03",

            "原谅我这个没用的哥哥……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x10B,
        (
            "#214F所、所以啊……\x01",
            "不是都那样说了嘛。\x02\x03",

            "#215F不要让我重复好几次啊！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #135
        0x12,
        "#192F#4S哦哦哦————！\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x12C)
    CloseMessageWindow()

    ChrTalk(    #136
        0x10B,
        "#216F多、多伦哥？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x12,
        (
            "#198F我……\x01",
            "我怎么这么幸福啊！\x02\x03",

            "有个这么可爱的妹妹……\x01",
            "再没有像我这样的幸运儿了！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #138
        0x12,
        "#191F#4S哦哦哦——！\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x12C)
    CloseMessageWindow()

    ChrTalk(    #139
        0x10B,
        (
            "#414F别、别说啦～多伦哥！\x01",
            "都被大家听到了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x12,
        "#198F哦、哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x10B,
        (
            "#413F还有，吉尔哥。\x01",
            "让你担心了，真是不好意思。\x02\x03",

            "#415F……谢谢你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x11,
        (
            "#200F算啦，乔丝特。\x01",
            "我也没特地去做什么事。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x80)
    OP_4A(0x15, 255)
    SetChrPos(0x15, -15500, 500, 4900, 270)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #143
        0x15,
        "男人的声音",
        "#1P小姐～小姐在吗？\x02",
    )

    CloseMessageWindow()

    def lambda_381B():
        OP_67(0, 5480, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_381B)

    def lambda_3833():
        OP_6D(-21640, 0, 7960, 1500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3833)

    def lambda_384B():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x10B, 2, lambda_384B)
    WaitChrThread(0x1A, 0x1)

    def lambda_385E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_385E)

    def lambda_3870():
        OP_8E(0xFE, 0xFFFFBF28, 0xFA, 0x1324, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3870)
    WaitChrThread(0x15, 0x1)
    Sleep(300)

    ChrTalk(    #144
        0x10B,
        (
            "#213F#1P洛西……？\x01",
            "发生什么事了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x15,
        (
            "没什么，\x01",
            "刚才在固定货物的时候，\x01",
            "发现了这个东西。\x02",
        )
    )

    Jump("loc_3905")

    label("loc_3905")

    CloseMessageWindow()

    ChrTalk(    #146
        0x15,
        (
            "仓库的地板上，\x01",
            "遗落了这样一个信封……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x15,
        "我想你们会不会有什么线索……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #148
        0x10B,
        "#213F#1P那是……\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_39D9():
        OP_67(0, 4900, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_39D9)

    def lambda_39F1():
        OP_8E(0xFE, 0xFFFFB9B0, 0xBB8, 0x10CC, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_39F1)
    WaitChrThread(0x10B, 0x1)
    OP_22(0xA3, 0x0, 0x50)

    def lambda_3A16():
        OP_96(0xFE, 0xFFFFBBA4, 0x0, 0xA50, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3A16)
    WaitChrThread(0x10B, 0x1)
    OP_23(0xA3)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_3A41():
        OP_8E(0xFE, 0xFFFFB758, 0x0, 0xA50, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3A41)
    WaitChrThread(0x10B, 0x1)

    def lambda_3A61():
        OP_8E(0xFE, 0xFFFFB758, 0x0, 0x1388, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3A61)
    WaitChrThread(0x10B, 0x1)

    def lambda_3A81():
        OP_8E(0xFE, 0xFFFFBAB4, 0x0, 0x1388, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3A81)
    WaitChrThread(0x10B, 0x1)
    Sleep(500)

    ChrTalk(    #149
        0x12,
        "#192F#5P难道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x11,
        (
            "#200F哈哈，\x01",
            "看来连收货人那儿也没送到呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x12,
        (
            "#198F#5P哎呀呀～\x01",
            "我怎么这么笨呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x15,
        "这、这就是那个了。\x02",
    )

    CloseMessageWindow()

    def lambda_3B47():
        OP_8E(0xFE, 0xFFFFBBE0, 0x0, 0x1388, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3B47)
    WaitChrThread(0x10B, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #153
        "\x07\x05从洛西手里接过了信封。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    def lambda_3BAC():
        OP_8F(0xFE, 0xFFFFBAB4, 0x0, 0x1388, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3BAC)
    WaitChrThread(0x10B, 0x1)
    Sleep(300)

    ChrTalk(    #154
        0x10B,
        "#415F#5P帝国的信封……果然。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x15,
        (
            "怎、怎么，\x01",
            "有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x10B,
        (
            "#210F#5P没关系，\x01",
            "已经解决了。\x02\x03",

            "谢谢你送过来。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #157
        0x15,
        (
            "没什么，哈哈。\x01",
            "只是举手之劳而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x15,
        "那么，我这就回去工作了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x15, 100, 500)

    def lambda_3CD2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_3CD2)

    def lambda_3CE4():
        OP_8E(0xFE, 0xFFFFC374, 0x1F4, 0x1324, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3CE4)
    WaitChrThread(0x15, 0x1)

    ChrTalk(    #159
        0x11,
        (
            "#200F呼，总之，\x01",
            "信没事真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x12,
        (
            "#490F#5P那，信里到底\x01",
            "写了些什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10B, 280, 500)
    Sleep(300)

    def lambda_3D6F():
        OP_6D(-24400, 0, 7800, 2500)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3D6F)

    def lambda_3D87():
        OP_67(0, 5250, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_3D87)

    def lambda_3D9F():
        OP_6B(2950, 2500)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_3D9F)

    def lambda_3DAF():
        OP_8E(0xFE, 0xFFFFAF88, 0x28A, 0x12D4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10B, 1, lambda_3DAF)
    WaitChrThread(0x10B, 0x1)

    ChrTalk(    #161
        0x10B,
        (
            "#210F这个嘛，嗯……\x02\x03",

            "#415F……啊，\x01",
            "说是马上要离开帝国了。\x02\x03",

            "好像是在找人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x11,
        (
            "#200F呵呵，是这样……\x01",
            "接下来会去什么地方呢。\x02\x03",

            "……对了，乔丝特。\x02\x03",

            "那小子没有给你写什么吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x10B,
        (
            "#414F嗯、嗯……\x02\x03",

            "不要刨根问底的啦。\x01",
            "就是『不要忘了休息一下』之类的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x11,
        (
            "#202F呵呵，虽然是若无其事的语气，\x01",
            "却是很体贴的问候呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x10B,
        "#416F那么，下面呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x11,
        "#200F下面？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10B,
        (
            "#212F这个是……那个没大脑的笨女人写的。\x02\x03",

            "『努力虽然是好事，\x01",
            "  但是身体弄坏了，就得不偿失了哦』……\x02\x03",

            "#214F哼，瞎操心！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x11,
        (
            "#202F哈哈，\x01",
            "的确符合那小姑娘的风格呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x12,
        (
            "#191F#5P哇哈哈……\x01",
            "不过她能够特地写信给你，\x01",
            "也真是挺难得的啊。\x02\x03",

            "#490F……唉，刚才发生了这么多事，\x01",
            "时间已经不早了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x10B,
        (
            "#210F确实……\x01",
            "也不能再这么悠闲下去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 1)
    Sleep(500)

    ChrTalk(    #171
        0x11,
        "#200F嘿嘿……我能冲刺吗，大哥？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 240, 500)
    Sleep(300)

    ChrTalk(    #172
        0x12,
        (
            "#490F#11P嗯，\x01",
            "争取多跑一些路吧。\x02\x03",

            "推力提升至９０％——\x01",
            "时速提升到\x01",
            "２０００塞尔矩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x11,
        "#202F明白！\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x11, 0)
    Sleep(500)

    def lambda_41D1():

        label("loc_41D1")

        OP_7C(0xA, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_41D1")

    QueueWorkItem2(0x11, 3, lambda_41D1)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2508)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_309D end

    def Function_15_4203(): pass

    label("Function_15_4203")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x109, -17690, 0, 2500, 0)
    SetChrPos(0x10F, -18960, 0, 2500, 0)
    SetChrPos(0xF0, -20380, 0, 2800, 0)
    SetChrPos(0xF1, -21710, 0, 2680, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(-20260, 500, 4890, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #174
        0x109,
        "#1079F#6P哦，那个是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x10F,
        (
            "#1446F#6P虽然看不太清楚，\x01",
            "不过，大概就是那种石头吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 90, 400)
    Sleep(100)

    def lambda_4332():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_4332)
    Sleep(100)

    def lambda_4345():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_4345)
    Sleep(100)

    ChrTalk(    #176
        0x10F,
        "#1440F#5P……我把它取回来吧？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #177
        0x109,
        (
            "#1060F#6P不，以防万一，\x01",
            "还是我去好了。\x02\x03",

            "大家在下面等我。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x109, -18110, 3000, 4140, 0)
    SetChrPos(0x10F, -18430, 0, 2500, 0)
    SetChrPos(0xF0, -19850, 0, 3260, 0)
    SetChrPos(0xF1, -20580, 0, 2500, 0)
    OP_6D(-20900, 500, 6780, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 7)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x1B, 0xFFFFB9B0, 0x1068, 0x1248, 0x12C, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x1B, 0x80)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #178
        "\x07\x00得到了\x1F\x55\x03\x07\x00。\x02",
    )

    Jump("loc_44E8")

    label("loc_44E8")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x355, 1)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x109, -17690, 0, 2500, 270)
    SetChrPos(0x10F, -19310, 0, 2920, 90)
    SetChrPos(0xF0, -20350, 0, 2500, 90)
    SetChrPos(0xF1, -19620, 200, 4580, 135)
    OP_6D(-20210, 0, 4940, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(327000, 0)
    OP_6E(280, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45FA")

    ChrTalk(    #179
        0x10D,
        (
            "#273F#5P哦……\x01",
            "那就是所谓的封印石吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4634")

    label("loc_45FA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4634")

    ChrTalk(    #180
        0x10E,
        (
            "#170F#5P唔……\x01",
            "又是那种石头吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4634")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4677")

    ChrTalk(    #181
        0x107,
        (
            "#560F#5P出现在这艘船上，\x01",
            "也就是说……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46BD")

    label("loc_4677")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46BD")

    ChrTalk(    #182
        0x10E,
        (
            "#176F#5P唔……\x01",
            "出现在这艘船上，也就是说……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46BD")


    ChrTalk(    #183
        0x109,
        (
            "#1065F#4P……总之，\x01",
            "暂且先回据点一趟吧。\x02\x03",

            "#1060F把它解放了之后，\x01",
            "说不定又会触发什么现象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x10F,
        "#1448F#5P嗯，那倒也是。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x270E)
    OP_28(0x2C, 0x1, 0x20)
    OP_64(0x0, 0x1)
    OP_6D(-18640, 0, 2770, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -18640, 0, 2770, 0)
    SetChrPos(0x1, -18640, 0, 2770, 0)
    SetChrPos(0x2, -18640, 0, 2770, 0)
    SetChrPos(0x3, -18640, 0, 2770, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_15_4203 end

    def Function_16_4827(): pass

    label("Function_16_4827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DA4")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A75")
    Fade(500)
    SetChrPos(0x109, -20320, 500, 4670, 270)
    SetChrPos(0x10F, -19460, 0, 3190, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4899")
    SetChrPos(0x107, -21700, 650, 4990, 270)
    SetChrPos(0xF1, -20650, 0, 2500, 315)
    Jump("loc_48C9")

    label("loc_4899")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48C9")
    SetChrPos(0x107, -21700, 650, 4990, 270)
    SetChrPos(0xF0, -20650, 0, 2500, 315)

    label("loc_48C9")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(-21220, 650, 5380, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(338000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #185
        "\x07\x05提妲打开终端的开关。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #186
        "\x07\x05但是，没有任何反应。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #187
        0x107,
        (
            "#062F#5P…………………\x02\x03",

            "#561F……不行。\x01",
            "启动钥匙明明已经插进去了，\x01",
            "怎么不能启动导力引擎呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x109,
        (
            "#1063F#6P唔……\x01",
            "和埃尔塞尤一样吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x10F,
        (
            "#1446F#6P……看来现在\x01",
            "只能暂时放弃了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CD3")

    label("loc_4A75")

    Fade(500)
    SetChrPos(0x109, -20320, 500, 4670, 270)
    SetChrPos(0x10F, -19460, 0, 3190, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4ACF")
    SetChrPos(0x10D, -21700, 650, 4990, 270)
    SetChrPos(0xF1, -20650, 0, 2500, 315)
    Jump("loc_4AFF")

    label("loc_4ACF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AFF")
    SetChrPos(0x10D, -21700, 650, 4990, 270)
    SetChrPos(0xF0, -20650, 0, 2500, 315)

    label("loc_4AFF")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(-21220, 650, 5380, 0)
    OP_67(0, 5140, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(338000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #190
        "\x07\x05穆拉打开终端的开关。\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #191
        "\x07\x05但是，没有任何反应。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #192
        0x10D,
        (
            "#272F#5P……导力引擎\x01",
            "好像无法启动。\x02\x03",

            "#270F但如你们所见，\x01",
            "启动钥匙已经在起作用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x10E,
        (
            "#178F#6P原来如此……\x01",
            "和埃尔塞尤一样吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x109,
        "#1841F#6P算了，反正早就想到会是这样。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x10F,
        (
            "#1440F#6P……看来现在\x01",
            "只能暂时放弃了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CD3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-21610, 650, 4890, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -21610, 650, 4890, 90)
    SetChrPos(0x1, -21610, 650, 4890, 90)
    SetChrPos(0x2, -21610, 650, 4890, 90)
    SetChrPos(0x3, -21610, 650, 4890, 90)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_A2(0x2710)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Jump("loc_4E33")

    label("loc_4DA4")

    TalkBegin(0xFF)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #196
        (
            "\x07\x05终端的开关已经打开，\x01",
            "但是什么反应也没有。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #197
        (
            "\x07\x05看来是因为\x01",
            "导力引擎无法启动。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_4E33")

    Return()

    # Function_16_4827 end

    SaveToFile()

Try(main)
