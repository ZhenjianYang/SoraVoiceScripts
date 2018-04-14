from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5601   ._SN',
        MapName             = 'Other',
        Location            = 'C5601.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60125",
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
        '银发的青年',                           # 9
        '怀斯曼教授',                           # 10
        '歼灭天使玲',                           # 11
        '艾丝蒂尔',                             # 12
        '小丑肯帕雷拉',                         # 13
        '结社艇',                               # 14
        '结社艇（影）',                         # 15
        '结社艇（光）',                         # 16
        '帕蒂尔·玛蒂尔',                       # 17
        '小船',                                 # 18
        '小船（诱饵）',                         # 19
        '目标用照相机',                         # 20
        '库拉茨',                               # 21
        '卡露娜',                               # 22
        '亚妮拉丝',                             # 23
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
        'ED6_DT27/CH03003 ._CH',             # 00
        'ED6_DT07/CH00023 ._CH',             # 01
        'ED6_DT07/CH00053 ._CH',             # 02
        'ED6_DT07/CH00033 ._CH',             # 03
        'ED6_DT07/CH00043 ._CH',             # 04
        'ED6_DT07/CH00063 ._CH',             # 05
        'ED6_DT07/CH00073 ._CH',             # 06
        'ED6_DT27/CH03083 ._CH',             # 07
        'ED6_DT07/CH02040 ._CH',             # 08
        'ED6_DT27/CH03550 ._CH',             # 09
        'ED6_DT27/CH03510 ._CH',             # 0A
        'ED6_DT27/CH03004 ._CH',             # 0B
        'ED6_DT29/CH12570 ._CH',             # 0C
        'ED6_DT29/CH12571 ._CH',             # 0D
        'ED6_DT27/CH03600 ._CH',             # 0E
        'ED6_DT26/CH20295 ._CH',             # 0F
        'ED6_DT26/CH20379 ._CH',             # 10
        'ED6_DT07/CH01260 ._CH',             # 11
        'ED6_DT07/CH01240 ._CH',             # 12
        'ED6_DT07/CH01630 ._CH',             # 13
        'ED6_DT26/CH20288 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT27/CH03003P._CP',             # 00
        'ED6_DT07/CH00023P._CP',             # 01
        'ED6_DT07/CH00053P._CP',             # 02
        'ED6_DT07/CH00033P._CP',             # 03
        'ED6_DT07/CH00043P._CP',             # 04
        'ED6_DT07/CH00063P._CP',             # 05
        'ED6_DT07/CH00073P._CP',             # 06
        'ED6_DT27/CH03083P._CP',             # 07
        'ED6_DT07/CH02040P._CP',             # 08
        'ED6_DT27/CH03550P._CP',             # 09
        'ED6_DT27/CH03510P._CP',             # 0A
        'ED6_DT27/CH03004P._CP',             # 0B
        'ED6_DT29/CH12570P._CP',             # 0C
        'ED6_DT29/CH12571P._CP',             # 0D
        'ED6_DT27/CH03600P._CP',             # 0E
        'ED6_DT26/CH20295P._CP',             # 0F
        'ED6_DT26/CH20379P._CP',             # 10
        'ED6_DT07/CH01260P._CP',             # 11
        'ED6_DT07/CH01240P._CP',             # 12
        'ED6_DT07/CH01630P._CP',             # 13
        'ED6_DT26/CH20288P._CP',             # 14
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
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
        NpcIndex            = 0x185,
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x188,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x1E5,
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
        NpcIndex            = 0x84,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6510,
        Z                   = -6050,
        Y                   = -26680,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -6770,
        Z                   = -5970,
        Y                   = -27880,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -6380,
        Z                   = -5900,
        Y                   = -28820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = 9520,
        TriggerZ            = 9000,
        TriggerY            = 6150,
        TriggerRange        = 1000,
        ActorX              = 9960,
        ActorZ              = 9000,
        ActorY              = 6600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -15010,
        TriggerZ            = 0,
        TriggerY            = -3880,
        TriggerRange        = 800,
        ActorX              = -15010,
        ActorZ              = 1000,
        ActorY              = -3880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -4500,
        TriggerZ            = -6000,
        TriggerY            = -27040,
        TriggerRange        = 1000,
        ActorX              = -4500,
        ActorZ              = -5000,
        ActorY              = -27040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_39E",          # 00, 0
        "Function_1_48D",          # 01, 1
        "Function_2_570",          # 02, 2
        "Function_3_65D",          # 03, 3
        "Function_4_70E",          # 04, 4
        "Function_5_76D",          # 05, 5
        "Function_6_8D7",          # 06, 6
        "Function_7_124B",         # 07, 7
        "Function_8_12C1",         # 08, 8
        "Function_9_1323",         # 09, 9
        "Function_10_1399",        # 0A, 10
        "Function_11_13FB",        # 0B, 11
        "Function_12_159E",        # 0C, 12
        "Function_13_1649",        # 0D, 13
        "Function_14_16FE",        # 0E, 14
        "Function_15_1FB1",        # 0F, 15
        "Function_16_200C",        # 10, 16
        "Function_17_205B",        # 11, 17
        "Function_18_20A2",        # 12, 18
        "Function_19_2137",        # 13, 19
        "Function_20_21D1",        # 14, 20
        "Function_21_2232",        # 15, 21
        "Function_22_22D5",        # 16, 22
        "Function_23_2329",        # 17, 23
        "Function_24_236C",        # 18, 24
        "Function_25_3A92",        # 19, 25
        "Function_26_3B1C",        # 1A, 26
        "Function_27_3B79",        # 1B, 27
        "Function_28_3C00",        # 1C, 28
        "Function_29_3C0C",        # 1D, 29
    )


    def Function_0_39E(): pass

    label("Function_0_39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 7)), scpexpr(EXPR_END)), "loc_3A8")
    Jump("loc_3E1")

    label("loc_3A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 5)), scpexpr(EXPR_END)), "loc_3C1")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_3E1")

    label("loc_3C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 3)), scpexpr(EXPR_END)), "loc_3D5")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_3E1")

    label("loc_3D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 0)), scpexpr(EXPR_END)), "loc_3E1")
    ClearChrFlags(0x14, 0x80)

    label("loc_3E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E9")

    label("loc_3E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_418")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10)
    OP_11(0x81, 0x99, 0xCF, 0x186A0, 0x493E0, 0x0)
    Event(0, 6)
    Jump("loc_48C")

    label("loc_418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_436")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    OP_64(0x0, 0x1)
    Event(0, 12)
    Jump("loc_48C")

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_454")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    OP_64(0x0, 0x1)
    Event(0, 13)
    Jump("loc_48C")

    label("loc_454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_473")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_48C")

    label("loc_473")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)

    label("loc_48C")

    Return()

    # Function_0_39E end

    def Function_1_48D(): pass

    label("Function_1_48D")

    OP_16(0x2, 0xFA0, 0xFFFDDD20, 0xFFFE3AE0, 0x230073)
    OP_22(0x1C5, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B6")
    OP_6F(0x1, 0)
    Jump("loc_4BD")

    label("loc_4B6")

    OP_6F(0x1, 60)

    label("loc_4BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 7)), scpexpr(EXPR_END)), "loc_4DF")
    OP_10(0x0, 0x1)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x10)
    OP_6F(0x4, 30)
    OP_64(0x1, 0x1)
    Jump("loc_4E2")

    label("loc_4DF")

    OP_10(0x0, 0x0)

    label("loc_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 4)), scpexpr(EXPR_END)), "loc_4FF")
    OP_A1(0x11, 0x3)
    SetChrPos(0x11, -8590, -8500, -33600, 90)

    label("loc_4FF")

    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_1C(0x5, 0x0, 0x1C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_566")
    LoadEffect(0x6, "map\\\\mp027_00.eff")
    PlayEffect(0x6, 0x6, 0xFF, -4500, -5000, -27040, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Jump("loc_56F")

    label("loc_566")

    OP_71(0x1D, 0x4)
    OP_64(0x2, 0x1)

    label("loc_56F")

    Return()

    # Function_1_48D end

    def Function_2_570(): pass

    label("Function_2_570")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 5)), scpexpr(EXPR_END)), "loc_5B9")

    ChrTalk(    #0
        0x14,
        (
            "#822F协会和军方应该\x01",
            "马上就会派出支援……\x02\x03",

            "别太勉强哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_659")

    label("loc_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 3)), scpexpr(EXPR_END)), "loc_5FF")

    ChrTalk(    #1
        0x14,
        (
            "#824F只剩下亚妮拉丝了吗……\x02\x03",

            "#822F抱歉，拜托你们了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_659")

    label("loc_5FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 0)), scpexpr(EXPR_END)), "loc_659")

    ChrTalk(    #2
        0x14,
        (
            "#826F呜……\x02\x03",

            "#824F不用管我，\x01",
            "继续探索吧……\x02\x03",

            "卡露娜和亚妮拉丝就拜托你们了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_659")

    TalkEnd(0x14)
    Return()

    # Function_2_570 end

    def Function_3_65D(): pass

    label("Function_3_65D")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 5)), scpexpr(EXPR_END)), "loc_6B3")

    ChrTalk(    #3
        0x15,
        (
            "#833F没想到那个黑发小伙子\x01",
            "也潜入了这里……\x02\x03",

            "#834F希望他平安无事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70A")

    label("loc_6B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 3)), scpexpr(EXPR_END)), "loc_70A")

    ChrTalk(    #4
        0x15,
        (
            "#836F呜……\x01",
            "不用管我们。\x02\x03",

            "#835F就算这种状态之下，\x01",
            "我们还是可以照顾自己的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70A")

    TalkEnd(0x15)
    Return()

    # Function_3_65D end

    def Function_4_70E(): pass

    label("Function_4_70E")

    TalkBegin(0x16)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #5
        0x16,
        (
            "#813F我想约修亚\x01",
            "可能去了屋顶……\x02\x03",

            "#812F艾丝蒂尔……\x01",
            "你要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 0)
    TalkEnd(0x16)
    Return()

    # Function_4_70E end

    def Function_5_76D(): pass

    label("Function_5_76D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_845")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1E9, 1)"), scpexpr(EXPR_END)), "loc_7DC")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xE9\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D28)
    Jump("loc_842")

    label("loc_7DC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xE9\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xE9\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_842")

    Jump("loc_876")

    label("loc_845")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_876")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8CE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x43)"), scpexpr(EXPR_END)), "loc_895")
    Jump("loc_8CE")

    label("loc_895")


    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xE9\x01\x07\x00的食谱。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #10
        "\x1F\xE9\x01\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_8CE")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_76D end

    def Function_6_8D7(): pass

    label("Function_6_8D7")

    EventBegin(0x0)
    ClearMapFlags(0x100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8FD")
    ClearMapFlags(0x10)
    Call(0, 25)
    Call(0, 26)
    SetMapFlags(0x10)

    label("loc_8FD")

    OP_6D(31040, -6770, 3020, 0)
    OP_67(0, 11880, -10000, 0)
    OP_6B(13600, 0)
    OP_6C(351000, 0)
    OP_6E(410, 0)
    OP_71(0x2, 0x4)
    OP_72(0x3, 0x2)
    OP_71(0x3, 0x40)
    OP_A1(0x11, 0x3)
    SetChrPos(0x11, 70630, -7500, 40480, 45)
    SetChrFlags(0x11, 0x40)
    OP_48()
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x109, 0x20)
    SetChrBattleFlags(0xF8, 0x20)
    SetChrBattleFlags(0xF9, 0x20)
    OP_89(0x101, 70320, -7500, 39620, 225)
    OP_89(0x109, 69800, -7500, 40000, 225)
    OP_89(0xF8, 71200, -7500, 40440, 225)
    OP_89(0xF9, 70680, -7500, 40990, 225)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x109, 0x40)
    SetChrFlags(0xF8, 0x40)
    SetChrFlags(0xF9, 0x40)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x101, 0)
    SetChrChipByIndex(0x109, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A11")
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 1)

    label("loc_A11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A29")
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 2)

    label("loc_A29")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A41")
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x104, 3)

    label("loc_A41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A59")
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 4)

    label("loc_A59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A71")
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 5)

    label("loc_A71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A89")
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 6)

    label("loc_A89")

    LoadEffect(0x0, "map\\\\mp013_02.eff")
    LoadEffect(0x1, "map\\\\mp013_00.eff")
    LoadEffect(0x2, "map\\\\mp013_01.eff")
    PlayEffect(0x1, 0x1, 0x11, 0, -50, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x11, 0, 0, -1800, 180, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_72(0x1B, 0x4)
    OP_71(0x3, 0x20)
    OP_B0(0x3, 0x1E)
    OP_6F(0x3, 0)
    OP_70(0x3, 0xF0)
    OP_22(0xDA, 0x1, 0x28)
    StopSound(0x88B8, 0x927C0, 0x0)
    OP_C8(0x200, 0x46, "C_PLAC18._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_B81():
        OP_6D(11950, -8800, -2530, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B81)

    def lambda_B99():
        OP_6C(3000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_B99)

    def lambda_BA9():
        OP_8F(0x11, 0x2828, 0xFFFFDECC, 0xFFFF7CF2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_BA9)
    Sleep(6000)
    OP_C4(0x0, 0x40)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_44(0x11, 0x0)
    StopSound(0x88B8, 0x1D4C0, 0x0)
    OP_67(0, 8029, -10000, 0)
    OP_6B(1800, 0)
    OP_6C(3000, 0)
    OP_6E(597, 0)
    OP_69(0x11, 0x0)
    OP_6A(0x11)

    def lambda_C21():
        OP_8F(0x11, 0x2828, 0xFFFFDECC, 0xFFFF7CF2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_C21)
    FadeToBright(500, 0)
    OP_24(0xDA, 0x4B)
    OP_0D()
    Sleep(500)

    ChrTalk(    #11 op#A op#5
        0x101,
        "#1004F#6P#5A啊……！\x05\x02",
    )

    OP_56(0x0)
    OP_59()
    Sleep(300)

    ChrTalk(    #12 op#A op#5
        0x109,
        "#1063F#5P#14A看来突破了……\x05\x02",
    )

    OP_56(0x0)
    OP_59()
    Sleep(500)
    OP_6A(0xFF)
    OP_C4(0x1, 0x40)
    Fade(500)
    OP_6D(-9850, -6060, -34780, 0)
    OP_67(0, 10860, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_C4(0x1, 0x40)
    WaitChrThread(0x11, 0x0)

    def lambda_CF2():
        OP_8C(0xFE, 90, 0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_CF2)

    def lambda_D00():
        OP_8C(0xFE, 270, 0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D00)

    def lambda_D0E():
        OP_8C(0xFE, 270, 0)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_D0E)

    def lambda_D1C():
        OP_8C(0xFE, 270, 0)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_D1C)

    def lambda_D2A():
        OP_8C(0xFE, 270, 0)
        ExitThread()

    QueueWorkItem(0xF9, 3, lambda_D2A)

    def lambda_D38():
        OP_8F(0xFE, 0xFFFFDE72, 0xFFFFDECC, 0xFFFF7CC0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D38)
    Sleep(400)
    OP_23(0xDA)
    OP_22(0xD4, 0x0, 0x64)
    Sleep(2600)

    def lambda_D65():
        OP_8F(0xFE, 0xFFFFDE72, 0xFFFFDECC, 0xFFFF7CC0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D65)
    Sleep(1500)

    def lambda_D85():
        OP_8F(0xFE, 0xFFFFDE72, 0xFFFFDECC, 0xFFFF7CC0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D85)
    Sleep(1000)

    def lambda_DA5():
        OP_8F(0xFE, 0xFFFFDE72, 0xFFFFDECC, 0xFFFF7CC0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_DA5)
    Sleep(1000)

    def lambda_DC5():
        OP_8F(0xFE, 0xFFFFDE72, 0xFFFFDECC, 0xFFFF7CC0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_DC5)
    WaitChrThread(0x11, 0x1)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    PlayEffect(0x0, 0x0, 0x11, 0, -180, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    ChrTalk(    #13
        0x101,
        "#1006F#6P好……抵达了。\x02",
    )

    CloseMessageWindow()

    def lambda_E42():
        OP_6D(-8500, -5850, -29870, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E42)

    def lambda_E5A():
        OP_67(0, 7820, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E5A)

    def lambda_E72():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E72)

    def lambda_E82():
        OP_6B(3310, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_E82)
    OP_43(0x109, 0x1, 0x0, 0x8)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0xA)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x7)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x9)
    Sleep(500)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    OP_82(0x0, 0x2)

    ChrTalk(    #14
        0x101,
        (
            "#1002F#6P这附近看起来\x01",
            "好像没有人的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x109,
        (
            "#1063F#5P不可掉以轻心。\x02\x03",

            "总之只能慎重调查一下\x01",
            "上面的建筑物了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F9F")

    ChrTalk(    #16
        0x108,
        (
            "#074F#5P何况，对手是他们啊。\x02\x03",

            "#072F要是觉得危险的话，\x01",
            "就果断地撤退吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1109")

    label("loc_F9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FFC")

    ChrTalk(    #17
        0x103,
        (
            "#025F#5P何况，对手是他们哦。\x02\x03",

            "#022F要是觉得危险的话，\x01",
            "就果断地撤退哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1109")

    label("loc_FFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1059")

    ChrTalk(    #18
        0x106,
        (
            "#053F#5P何况，对手是他们啊。\x02\x03",

            "#050F要是觉得危险的话，\x01",
            "就果断地撤退吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1109")

    label("loc_1059")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10B1")

    ChrTalk(    #19
        0x104,
        (
            "#032F#5P何况，对手是他们啊。\x02\x03",

            "要是觉得危险的话，\x01",
            "就果断地撤退吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1109")

    label("loc_10B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1109")

    ChrTalk(    #20
        0x105,
        (
            "#047F#5P何况，对手是他们。\x02\x03",

            "#042F要是觉得危险的话，\x01",
            "就果断地撤退吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1109")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116E")

    ChrTalk(    #21
        0x101,
        (
            "#1010F#6P嗯……说得也是。\x02\x03",

            "#1006F提妲。\x01",
            "要努力跟上来哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x107,
        "#062F#5P嗯……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1189")

    label("loc_116E")


    ChrTalk(    #23
        0x101,
        "#1006F#6P嗯……也对！\x02",
    )

    CloseMessageWindow()

    label("loc_1189")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-9590, -5860, -29950, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -9590, -5860, -29950, 270)
    SetChrPos(0x1, -9590, -5860, -29950, 270)
    SetChrPos(0x2, -9590, -5860, -29950, 270)
    SetChrPos(0x3, -9590, -5860, -29950, 270)
    OP_69(0x0, 0x0)
    OP_A2(0x1C04)
    OP_28(0x97, 0x4, 0x10)
    OP_28(0x97, 0x4, 0x20)
    OP_28(0x98, 0x4, 0x2)
    OP_28(0x98, 0x4, 0x8)
    OP_28(0x98, 0x1, 0x1)
    OP_28(0x98, 0x1, 0x2)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_8D7 end

    def Function_7_124B(): pass

    label("Function_7_124B")

    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 65535)
    OP_8C(0xFE, 0, 400)
    Sleep(200)
    OP_8E(0xFE, 0xFFFFDBF2, 0xFFFFDECC, 0xFFFF7E32, 0xBB8, 0x0)
    OP_96(0xFE, 0xFFFFD97C, 0xFFFFE890, 0xFFFF8616, 0x9C4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    OP_8E(0xFE, 0xFFFFD88C, 0xFFFFE886, 0xFFFF881E, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_7_124B end

    def Function_8_12C1(): pass

    label("Function_8_12C1")

    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 65535)
    OP_8C(0xFE, 0, 400)
    Sleep(200)
    OP_96(0xFE, 0xFFFFD97C, 0xFFFFE890, 0xFFFF8616, 0x9C4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    OP_8E(0xFE, 0xFFFFD922, 0xFFFFE8E0, 0xFFFF8EB8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_8_12C1 end

    def Function_9_1323(): pass

    label("Function_9_1323")

    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 65535)
    OP_8C(0xFE, 0, 400)
    Sleep(200)
    OP_8E(0xFE, 0xFFFFDF58, 0xFFFFDECC, 0xFFFF7E78, 0xBB8, 0x0)
    OP_96(0xFE, 0xFFFFDEFE, 0xFFFFE890, 0xFFFF8648, 0x9C4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    OP_8E(0xFE, 0xFFFFE05C, 0xFFFFE8AE, 0xFFFF88BE, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_1323 end

    def Function_10_1399(): pass

    label("Function_10_1399")

    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 65535)
    OP_8C(0xFE, 0, 400)
    Sleep(200)
    OP_96(0xFE, 0xFFFFDEFE, 0xFFFFE890, 0xFFFF8648, 0x9C4, 0x1388)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    SetChrFlags(0xFE, 0x1)
    OP_8E(0xFE, 0xFFFFDF30, 0xFFFFE8EA, 0xFFFF8EE0, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_10_1399 end

    def Function_11_13FB(): pass

    label("Function_11_13FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_155D")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #24
        "\x07\x05门牢牢地关着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(1000)
    OP_6D(-14880, 0, -4710, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(26000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -14410, 0, -7130, 0)
    SetChrPos(0x109, -15440, 0, -7210, 0)
    SetChrPos(0xF8, -13390, 0, -6670, 0)
    SetChrPos(0xF9, -16400, 0, -6540, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150C")

    ChrTalk(    #25
        0x101,
        "#1007F#4P打不开吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        (
            "#1067F#6P看来只好寻找\x01",
            "别的入口了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1555")

    label("loc_150C")


    ChrTalk(    #27
        0x101,
        "#1002F#4P打不开吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        (
            "#1068F#6P果然只能从刚才\x01",
            "那个入口潜入了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1555")

    OP_A2(0x1C05)
    EventEnd(0x0)
    Jump("loc_159D")

    label("loc_155D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05门牢牢地关着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_159D")

    Return()

    # Function_11_13FB end

    def Function_12_159E(): pass

    label("Function_12_159E")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-14460, 0, -2390, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(17000, 0)
    OP_6E(262, 0)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x10)
    OP_6F(0x4, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x4)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_159E end

    def Function_13_1649(): pass

    label("Function_13_1649")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-14460, 0, -2390, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(17000, 0)
    OP_6E(262, 0)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x10)
    OP_6F(0x4, 30)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x10)
    OP_6F(0x4, 30)
    OP_70(0x4, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x4)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1649 end

    def Function_14_16FE(): pass

    label("Function_14_16FE")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1718")
    Call(0, 25)
    Call(0, 26)
    RemoveParty(0x0, 0xFF)

    label("loc_1718")

    OP_6D(-7800, 15000, 15500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(47000, 0)
    OP_6E(262, 0)
    OP_6D(-7430, 15000, 16250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(47000, 0)
    OP_6E(262, 0)
    SetChrPos(0x109, -6230, 15000, 20660, 0)
    SetChrPos(0xF8, -6230, 15000, 20660, 0)
    SetChrPos(0xF9, -6230, 15000, 20660, 0)
    OP_72(0x0, 0x20)
    OP_6F(0x0, 1200)
    OP_A1(0xD, 0x0)
    SetChrPos(0xD, -25800, 15150, 11920, 0)
    OP_72(0x1B, 0x4)
    OP_A1(0xE, 0x1B)
    SetChrPos(0xE, -25800, 15250, 11920, 0)
    OP_72(0x1C, 0x4)
    OP_72(0x1C, 0x20)
    OP_6F(0x1C, 1200)
    OP_A1(0xF, 0x1C)
    SetChrPos(0xF, -25800, 15150, 11920, 0)
    OP_48()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xA, 0x1)
    SetChrBattleFlags(0x8, 0x20)
    SetChrBattleFlags(0x9, 0x20)
    SetChrBattleFlags(0xA, 0x20)
    OP_89(0x8, -25470, 18450, 9290, 90)
    OP_89(0x9, -23100, 18450, 9890, 90)
    OP_89(0xA, -23140, 18450, 8530, 90)
    SetChrChipByIndex(0x8, 16)
    SetChrSubChip(0x8, 0)
    OP_22(0x75, 0x1, 0x46)
    OP_79(0xC, 0x2)
    OP_7B()
    FadeToBright(1000, 0)
    OP_0D()
    OP_72(0x6, 0x10)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 0)
    OP_70(0x6, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x6)
    Sleep(200)
    OP_43(0x109, 0x1, 0x0, 0x11)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x13)
    WaitChrThread(0xF9, 0x1)
    Sleep(1000)

    ChrTalk(    #30
        0x109,
        "#1069F#5P糟糕……！\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (6, "loc_1930"),
        (4, "loc_1949"),
        (2, "loc_1962"),
        (5, "loc_197D"),
        (3, "loc_1996"),
        (7, "loc_19AF"),
        (SWITCH_DEFAULT, "loc_19C6"),
    )


    label("loc_1930")


    ChrTalk(    #31
        0x107,
        "#065F#5P啊……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_19C6")

    label("loc_1949")


    ChrTalk(    #32
        0x105,
        "#043F#5P啊……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_19C6")

    label("loc_1962")


    ChrTalk(    #33
        0x103,
        "#523F#5P什…什么！\x02",
    )

    CloseMessageWindow()
    Jump("loc_19C6")

    label("loc_197D")


    ChrTalk(    #34
        0x106,
        "#057F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_19C6")

    label("loc_1996")


    ChrTalk(    #35
        0x104,
        "#039F#5P唔……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_19C6")

    label("loc_19AF")


    ChrTalk(    #36
        0x108,
        "#077F#5P……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_19C6")

    label("loc_19C6")


    def lambda_19CC():
        OP_6D(-18050, 24180, 6110, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_19CC)

    def lambda_19E4():
        OP_67(0, 5750, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_19E4)

    def lambda_19FC():
        OP_6C(315000, 3500)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_19FC)

    def lambda_1A0C():
        OP_6E(341, 3500)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1A0C)

    def lambda_1A1C():
        OP_6B(1850, 3500)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_1A1C)
    Sleep(3000)
    SetChrPos(0x13, -18050, 24180, 6110, 0)

    def lambda_1A42():

        label("loc_1A42")

        OP_69(0x13, 0x0)
        OP_48()
        Jump("loc_1A42")

    QueueWorkItem2(0x13, 2, lambda_1A42)
    OP_B0(0x0, 0x3C)
    OP_6F(0x0, 361)
    OP_70(0x0, 0x230)
    Sleep(500)
    OP_22(0x76, 0x0, 0x64)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_73(0x0)
    Sleep(500)
    OP_43(0x109, 0x2, 0x0, 0x14)
    LoadEffect(0x0, "map\\\\mp021_00.eff")
    PlayEffect(0x0, 0x0, 0xE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0x75)
    OP_22(0x79, 0x1, 0x64)
    OP_22(0xCC, 0x0, 0x64)
    OP_B0(0x0, 0x1E)
    OP_6F(0x0, 561)
    OP_70(0x0, 0x28A)
    OP_B0(0x1C, 0x1E)
    OP_6F(0x1C, 561)
    OP_70(0x1C, 0x28A)

    def lambda_1B06():
        OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1B06)

    def lambda_1B21():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1B21)

    def lambda_1B3C():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1B3C)

    def lambda_1B57():
        OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1B57)
    WaitChrThread(0xD, 0x1)

    def lambda_1B77():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1B77)

    def lambda_1B92():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1B92)

    def lambda_1BAD():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1BAD)
    WaitChrThread(0xD, 0x1)

    def lambda_1BCD():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1BCD)

    def lambda_1BE8():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1BE8)

    def lambda_1C03():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1C03)
    WaitChrThread(0xD, 0x1)

    def lambda_1C23():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1C23)

    def lambda_1C3E():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1C3E)

    def lambda_1C59():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1C59)
    WaitChrThread(0xD, 0x1)

    def lambda_1C79():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1C79)

    def lambda_1C94():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1C94)

    def lambda_1CAF():
        OP_91(0xFE, 0x0, 0x7D0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1CAF)
    WaitChrThread(0xD, 0x1)

    def lambda_1CCF():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1CCF)

    def lambda_1CEA():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1CEA)

    def lambda_1D05():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1D05)
    WaitChrThread(0xD, 0x1)

    def lambda_1D25():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_1D25)

    def lambda_1D40():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1D40)

    def lambda_1D5B():
        OP_91(0xFE, 0x0, 0x3E8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1D5B)
    WaitChrThread(0xD, 0x1)
    OP_82(0x0, 0x2)
    OP_44(0x13, 0x2)
    OP_43(0xD, 0x3, 0x0, 0x10)
    OP_43(0xD, 0x2, 0x0, 0x16)

    def lambda_1D90():
        OP_6D(-5580, 30000, 22960, 7000)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_1D90)

    def lambda_1DA8():
        OP_6C(95000, 7000)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_1DA8)

    def lambda_1DB8():
        OP_97(0xFE, 0xFFFFD83C, 0x2E90, 0x20F58, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1DB8)

    def lambda_1DD4():
        OP_97(0xFE, 0xFFFFD83C, 0x2E90, 0x20F58, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1DD4)

    def lambda_1DF0():
        OP_97(0xFE, 0xFFFFD83C, 0x2E90, 0x20F58, 0x1F40, 0x1)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1DF0)
    OP_43(0x9, 0x0, 0x0, 0xF)
    Sleep(3000)
    OP_CA(0x1B, 0x1, 0x12C)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0xF, 0x1)
    WaitChrThread(0xE, 0x1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1E37():
        OP_6D(16140, 40000, 5000, 5000)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_1E37)

    def lambda_1E4F():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0xF8, 3, lambda_1E4F)

    def lambda_1E5F():
        OP_67(0, 6750, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1E5F)

    def lambda_1E77():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1E77)

    def lambda_1E8D():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1E8D)

    def lambda_1EA3():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1EA3)
    Sleep(500)

    def lambda_1EBE():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1EBE)

    def lambda_1ED4():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1ED4)

    def lambda_1EEA():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1EEA)
    Sleep(500)

    def lambda_1F05():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1F05)

    def lambda_1F1B():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1F1B)

    def lambda_1F31():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x5208, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1F31)
    Sleep(500)

    def lambda_1F4C():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1F4C)

    def lambda_1F62():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_1F62)

    def lambda_1F78():
        OP_94(0x1, 0xFE, 0x0, 0x186A0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1F78)
    OP_43(0xD, 0x3, 0x0, 0x17)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x10F7)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_16FE end

    def Function_15_1FB1(): pass

    label("Function_15_1FB1")

    Sleep(1000)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 4)
    Sleep(50)
    SetChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 4)
    Sleep(50)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 4)
    Sleep(1000)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 3)
    Sleep(50)
    SetChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 3)
    Sleep(50)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 3)
    Return()

    # Function_15_1FB1 end

    def Function_16_200C(): pass

    label("Function_16_200C")

    OP_73(0x0)
    OP_73(0x1C)
    OP_6F(0x0, 651)
    OP_70(0x0, 0x2A8)
    OP_6F(0x1C, 651)
    OP_70(0x1C, 0x2A8)
    OP_73(0x0)
    OP_73(0x1C)
    OP_71(0x0, 0x20)
    OP_71(0x1C, 0x20)
    OP_6F(0x0, 680)
    OP_70(0x0, 0x30C)
    OP_6F(0x1C, 680)
    OP_70(0x1C, 0x30C)
    Return()

    # Function_16_200C end

    def Function_17_205B(): pass

    label("Function_17_205B")

    OP_8E(0xFE, 0xFFFFE7F0, 0x3A98, 0x422C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFDD82, 0x3A98, 0x3B10, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_17_205B end

    def Function_18_20A2(): pass

    label("Function_18_20A2")

    OP_8E(0xFE, 0xFFFFE7F0, 0x3A98, 0x422C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFE0AC, 0x3A98, 0x3656, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20F8")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2136")

    label("loc_20F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_211F")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2136")

    label("loc_211F")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2136")

    Return()

    # Function_18_20A2 end

    def Function_19_2137(): pass

    label("Function_19_2137")

    OP_8E(0xFE, 0xFFFFE7F0, 0x3A98, 0x422C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFE084, 0x3A98, 0x3F84, 0x1388, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2192")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_21D0")

    label("loc_2192")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21B9")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_21D0")

    label("loc_21B9")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_21D0")

    Return()

    # Function_19_2137 end

    def Function_20_21D1(): pass

    label("Function_20_21D1")

    Sleep(500)

    def lambda_21DC():
        OP_91(0xFE, 0xFFFFC568, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_21DC)
    Sleep(100)

    def lambda_21FC():
        OP_91(0xFE, 0xFFFFC568, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_21FC)
    Sleep(100)

    def lambda_221C():
        OP_91(0xFE, 0xFFFFC568, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_221C)
    Return()

    # Function_20_21D1 end

    def Function_21_2232(): pass

    label("Function_21_2232")

    Sleep(2000)

    def lambda_223D():
        OP_8E(0xFE, 0x1D4C, 0x3A98, 0x39B2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_223D)
    Sleep(200)

    def lambda_225D():
        OP_8E(0xFE, 0x1A72, 0x3A98, 0x35FC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_225D)
    Sleep(200)

    def lambda_227D():
        OP_8E(0xFE, 0x1626, 0x3A98, 0x32DC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_227D)
    WaitChrThread(0x109, 0x1)

    def lambda_229D():

        label("loc_229D")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_229D")

    QueueWorkItem2(0x109, 1, lambda_229D)
    WaitChrThread(0xF8, 0x1)

    def lambda_22B3():

        label("loc_22B3")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_22B3")

    QueueWorkItem2(0xF8, 1, lambda_22B3)
    WaitChrThread(0xF9, 0x1)

    def lambda_22C9():

        label("loc_22C9")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_22C9")

    QueueWorkItem2(0xF9, 1, lambda_22C9)
    Return()

    # Function_21_2232 end

    def Function_22_22D5(): pass

    label("Function_22_22D5")

    OP_73(0x0)
    OP_73(0x1C)
    OP_22(0x79, 0x0, 0x64)
    OP_6F(0x0, 651)
    OP_70(0x0, 0x2A8)
    OP_6F(0x1C, 651)
    OP_70(0x1C, 0x2A8)
    OP_73(0x0)
    OP_73(0x1C)
    OP_71(0x0, 0x20)
    OP_71(0x1C, 0x20)
    OP_6F(0x0, 680)
    OP_70(0x0, 0x30C)
    OP_6F(0x1C, 680)
    OP_70(0x1C, 0x30C)
    Return()

    # Function_22_22D5 end

    def Function_23_2329(): pass

    label("Function_23_2329")

    OP_24(0x79, 0x5A)
    Sleep(200)
    OP_24(0x79, 0x50)
    Sleep(200)
    OP_24(0x79, 0x46)
    Sleep(200)
    OP_24(0x79, 0x3C)
    Sleep(200)
    OP_24(0x79, 0x32)
    Sleep(200)
    OP_24(0x79, 0x28)
    Sleep(200)
    OP_24(0x79, 0x1E)
    Sleep(200)
    OP_23(0x79)
    Return()

    # Function_23_2329 end

    def Function_24_236C(): pass

    label("Function_24_236C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_237F")
    Call(0, 27)

    label("loc_237F")

    LoadEffect(0x1, "map\\\\mp064_01.eff")
    LoadEffect(0x2, "map\\\\mp065_01.eff")
    LoadEffect(0x3, "map\\\\mp064_00.eff")
    LoadEffect(0x4, "map\\\\mp065_00.eff")
    LoadEffect(0x5, "map\\\\mp021_00.eff")
    OP_71(0x1B, 0x4)
    OP_71(0x0, 0x4)
    OP_6D(-13460, 15200, -850, 0)
    OP_67(0, 6560, -10000, 0)
    OP_6B(6010, 0)
    OP_6C(0, 0)
    OP_6E(598, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0xC, -26000, 18450, 11200, 180)
    OP_A1(0x10, 0x2)
    OP_71(0x2, 0x20)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0xF)
    OP_6F(0x2, 501)
    OP_70(0x2, 0x208)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x2)
    OP_CF(0xA, 0x2, "Frame85__ren")
    SetChrSubChip(0xA, 1)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x40)
    SetChrPos(0x10, 21380, 20000, -38500, 0)
    OP_97(0x10, 0x4B6E, 0x4A6, 0x3E8, 0x2710, 0x1)
    PlayEffect(0x1, 0x0, 0x10, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x10, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x10, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0x10, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x4, 0x10, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x5, 0x10, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2609():
        OP_6D(-23510, 15200, 14990, 12000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2609)

    def lambda_2621():
        OP_67(0, 7830, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2621)

    def lambda_2639():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2639)

    def lambda_2649():
        OP_6B(4200, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2649)
    OP_22(0x113, 0x1, 0x32)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(200)
    OP_24(0x113, 0x3C)
    Sleep(200)
    OP_24(0x113, 0x46)
    Sleep(200)
    OP_24(0x113, 0x50)
    Sleep(200)
    OP_24(0x113, 0x5A)
    Sleep(200)
    OP_24(0x113, 0x64)
    OP_97(0x10, 0x4B6E, 0x4A6, 0x57E4, 0x3E80, 0x1)
    OP_97(0x10, 0x4B6E, 0x4A6, 0x57E4, 0x3A98, 0x1)
    OP_97(0x10, 0x4B6E, 0x4A6, 0x57E4, 0x36B0, 0x1)
    OP_97(0x10, 0x4B6E, 0x4A6, 0x4E20, 0x32C8, 0x1)
    PlayEffect(0x3, 0x6, 0x10, 4400, 3000, 0, 0, 0, 15, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x7, 0x10, -4400, 3000, 0, 0, 0, 345, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_8C(0x10, 0, 400)
    OP_22(0x114, 0x0, 0x64)
    PlayEffect(0x1, 0x6, 0x10, 4400, 3000, 0, 0, 0, 15, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x7, 0x10, -4400, 3000, 0, 0, 0, 345, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x2, 0x20)
    OP_B0(0x2, 0xA)
    OP_6F(0x2, 500)
    OP_70(0x2, 0x1E1)

    def lambda_27E0():
        OP_8F(0xFE, 0xFFFF9B38, 0x4E20, 0x2E90, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_27E0)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    OP_82(0x4, 0x2)
    OP_82(0x5, 0x2)
    Sleep(500)
    OP_22(0x116, 0x0, 0x64)
    Sleep(500)
    WaitChrThread(0x10, 0x1)

    def lambda_2826():
        OP_8C(0xFE, 180, 50)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2826)
    Sleep(500)
    SetChrSubChip(0xA, 2)
    Sleep(500)
    SetChrSubChip(0xA, 3)
    Sleep(500)
    SetChrSubChip(0xA, 4)
    Sleep(500)
    SetChrSubChip(0xA, 5)
    WaitChrThread(0x10, 0x1)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    Fade(1000)
    OP_6D(-27510, 15200, 10990, 0)
    OP_67(0, 7580, -10000, 0)
    OP_6B(4140, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x1)
    SetChrPos(0x10, -24960, 18450, 7270, 90)
    SetChrFlags(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x40)

    def lambda_2905():
        OP_8F(0xFE, 0xFFFF9F20, 0x3BC4, 0x1C34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2905)
    PlayEffect(0x5, 0x0, 0x10, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 421)
    OP_70(0x2, 0x1CC)
    OP_0D()
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x10, 0x1)
    OP_82(0x0, 0x2)
    OP_82(0x6, 0x2)
    OP_82(0x7, 0x2)
    OP_23(0x113)
    OP_22(0x88, 0x0, 0x64)
    OP_22(0xF5, 0x0, 0x64)
    OP_7C(0x0, 0x12C, 0xFA0, 0x1F4)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 421)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0xA, 0x1)
    Sleep(2000)

    ChrTalk(    #37
        0xA,
        (
            "#263F哈哈哈，把那些野猪一样的\x01",
            "飞艇全部甩开了吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    OP_8C(0xA, 180, 0)
    OP_8C(0xA, 270, 400)
    Sleep(500)

    ChrTalk(    #38
        0xA,
        "#1306F谢谢你，『帕蒂尔·玛蒂尔』。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(2000)
    SetChrPos(0x8, -12840, 14800, 9830, 270)
    ClearChrFlags(0x8, 0x80)

    NpcTalk(    #39
        0x8,
        "青年的声音",
        "#1P终于回来了，玲。\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2A9A():
        OP_6D(-20330, 15000, 9930, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A9A)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    OP_8C(0xA, 180, 400)

    def lambda_2AC3():
        OP_8E(0xFE, 0xFFFFC252, 0x3A98, 0x23D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2AC3)
    WaitChrThread(0x8, 0x0)
    OP_8C(0x8, 270, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #40
        0xA,
        "#265F#6P莱维！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    OP_CF(0xA, 0x2, "Frame86__ren")
    OP_8C(0xA, 90, 0)
    SetChrChipByIndex(0xA, 20)
    SetChrSubChip(0xA, 0)
    SetChrFlags(0xA, 0x2)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(250)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0xA, 0x1)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2B5F():
        OP_99(0xFE, 0x2, 0x5, 0x28A)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2B5F)
    OP_96(0xA, 0xFFFFAFC4, 0x3A98, 0x240E, 0x258, 0x9C4)
    SetChrFlags(0xA, 0x1)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xA, 0x0)

    def lambda_2BA6():
        OP_99(0xFE, 0x6, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2BA6)
    WaitChrThread(0xA, 0x0)
    SetChrChipByIndex(0xA, 10)
    SetChrSubChip(0xA, 0)
    ClearChrFlags(0xA, 0x2)

    def lambda_2BCA():
        OP_8E(0xFE, 0xFFFFBCB2, 0x3A98, 0x2350, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2BCA)

    def lambda_2BE5():
        OP_6D(-17430, 15000, 9790, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2BE5)

    def lambda_2BFD():
        OP_67(0, 5290, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BFD)

    def lambda_2C15():
        OP_6B(3420, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C15)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #41
        0xA,
        (
            "#261F#5P嘿嘿，我回来了。\x02\x03",

            "玲可是按照你的吩咐，\x01",
            "成功做完了实验哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#123F呵呵，辛苦了。\x02\x03",

            "不过你把事情搞得\x01",
            "还真是大啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        (
            "#266F#5P因为这次说是\x01",
            "不能杀人嘛。\x02\x03",

            "#1306F这么无聊，\x01",
            "至少要热闹热闹嘛。\x02\x03",

            "托你的福，\x01",
            "开了个很开心的茶会哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#124F呵呵……是吗。\x02\x03",

            "#120F实验的结果怎样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        (
            "#263F#5P这个嘛。\x01",
            "还不坏吧。\x02\x03",

            "#260F虽然被教会的哥哥\x01",
            "给搅了一下局……\x02\x03",

            "但运作很稳定，\x01",
            "我想足够用于实战了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        "#124F嗯，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        (
            "#267F#5P不过『福音』\x01",
            "现在还不能量产吧？\x02\x03",

            "能否作为兵器使用，\x01",
            "现在还无法确定呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#120F没有量产的必要啊。\x02\x03",

            "此次的实验也是\x01",
            "单纯以测试新型\x01",
            "『福音』的潜在能力为目的。\x02\x03",

            "并不是以制作兵器\x01",
            "为目的的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xA,
        (
            "#264F#5P咦，是吗？\x02\x03",

            "#263F算了。\x01",
            "我也没什么兴趣。\x02\x03",

            "#265F对了，话说回来……\x01",
            "约修亚还没找到吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#124F啊啊……\x02\x03",

            "#120F我们为了扰乱军队而放出的\x01",
            "人形兵器被破坏了好几架。\x02\x03",

            "恐怕就是他干的好事吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "#262F#5P嗯～真有一手。\x02\x03",

            "虽然玲也很擅长捉迷藏，\x01",
            "但还是敌不过约修亚……\x02\x03",

            "#268F啊～啊，不好玩。\x02\x03",

            "为什么不干脆\x01",
            "返回结社呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        "#124F谁知道……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xA,
        (
            "#267F#5P这么说来，教授倒是\x01",
            "说过由于艾丝蒂尔的原因，\x01",
            "约修亚才不会回来。\x02\x03",

            "艾丝蒂尔好像也在\x01",
            "寻找约修亚呢～\x02\x03",

            "到底怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "#120F玲……\x02\x03",

            "教授说的话\x01",
            "还是不要盲目相信的好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xA,
        "#264F#5P为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "#124F所谓真相，\x01",
            "每个人的看法都不同。\x02\x03",

            "譬如月亮的脸\x01",
            "被大家比喻成各种各样的形态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xA,
        "#265F#5P比如小兔子啦，或者螃蟹之类的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#120F是啊。\x02\x03",

            "教授所讲出来的“真实”\x01",
            "和玲自己感悟到的“真实”是不同的。\x02\x03",

            "你一定要自己去看，自己去感受，\x01",
            "只有这样才能体会到属于玲自己的“真实”。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xA,
        (
            "#265F#5P嗯～听起来好深奥哦，\x01",
            "玲不是很明白……\x02\x03",

            "#261F不过玲好像确实\x01",
            "挺喜欢艾丝蒂尔她们…\x02\x03",

            "就算下次再见面，\x01",
            "大概也不会马上就杀死她们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        "#124F那就好。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x40)
    OP_8E(0x8, 0xFFFFBF8C, 0x3A98, 0x2328, 0x5DC, 0x0)
    Sleep(500)
    Fade(250)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x1)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 0)
    OP_0D()
    OP_99(0x8, 0x0, 0x2, 0x3E8)
    OP_99(0x8, 0x3, 0x6, 0x3E8)
    OP_99(0x8, 0x3, 0x6, 0x3E8)
    Sleep(500)

    ChrTalk(    #61
        0x8,
        "#123F#4P很了不起哦，玲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xA,
        "#261F#5P嘿嘿……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x9, -7420, 15000, 13980, 270)
    SetChrPos(0xC, -7990, 15000, 14810, 270)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)

    NpcTalk(    #63
        0x9,
        "男性的声音",
        "#1P呵呵，辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xA, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)
    OP_0D()

    def lambda_3398():
        OP_8E(0xFE, 0xFFFFBC9E, 0x3A98, 0x1EDC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3398)

    def lambda_33B3():
        OP_8E(0xFE, 0xFFFFC3C4, 0x3A98, 0x215C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_33B3)
    Sleep(500)

    def lambda_33D3():
        OP_8E(0xFE, 0xFFFFC43C, 0x3A98, 0x2684, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_33D3)

    def lambda_33EE():
        OP_6D(-16030, 15000, 9710, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_33EE)

    def lambda_3406():
        OP_6C(32000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3406)

    def lambda_3416():
        OP_6B(3290, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3416)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 90, 400)
    WaitChrThread(0xC, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #64
        0xA,
        (
            "#265F#6P教授……\x01",
            "还有肯帕雷拉！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xC,
        (
            "#853F贵安，玲。\x02\x03",

            "#850F你在王都似乎\x01",
            "过得相当愉快啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#261F#6P嘿嘿嘿，还好啦。\x02\x03",

            "#265F要是事先知道你要来的话，\x01",
            "绝对会招待你一起参加的。\x02\x03",

            "当时的场面可是非常热闹的哦！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3583")

    ChrTalk(    #67
        0xC,
        (
            "#851F呵呵，那可真是遗憾啊。\x02\x03",

            "我也请游击士大姐姐她们\x01",
            "看了场人偶剧……\x02\x03",

            "但比起你的茶会来，\x01",
            "实在是不值一提啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35F4")

    label("loc_3583")


    ChrTalk(    #68
        0xC,
        (
            "#851F呵呵，那可真是遗憾啊。\x02\x03",

            "我也请游击士大哥哥他们\x01",
            "看了场人偶剧……\x02\x03",

            "但比起你的茶会来，\x01",
            "实在是不值一提啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35F4")


    ChrTalk(    #69
        0x9,
        (
            "#1154F#2P哈哈，下次有机会\x01",
            "再请我吧。\x02\x03",

            "#1151F不过玲……\x02\x03",

            "你好像和艾丝蒂尔\x01",
            "相当投缘吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xA,
        (
            "#263F#6P嘿嘿，还好啦。\x02\x03",

            "#260F并不像教授说的那么讨厌，\x01",
            "是个还挺不错的大姐姐呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "#1150F#2P哈哈，我也没\x01",
            "说过她是个讨厌的人啊。\x02\x03",

            "实话说，倒真是一个性格善良，\x01",
            "魅力十足的小姑娘呢。\x02\x03",

            "#1154F只是，约修亚之所以不愿意回来，\x01",
            "原因确实是因为她。\x02\x03",

            "对吧，莱维？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "#124F确实……\x01",
            "我不否认这是原因之一。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "#1151F#2P如何，玲。\x02\x03",

            "如果艾丝蒂尔成为我们的同伴，\x01",
            "你会不会很高兴？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        "#126F同……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "#264F#6P让艾丝蒂尔成为同伴？\x02\x03",

            "#263F……嘻嘻。\x01",
            "那当然好啊！很好玩的样子！\x02\x03",

            "#265F虽然实力还差得很远，\x01",
            "但只要经过锻炼，应该也会很快变强吧……\x02\x03",

            "而且，如果艾丝蒂尔加入的话，\x01",
            "约修亚也会回来对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        "#1151F#2P呵呵，这是当然的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xC,
        (
            "#851F#5P啊哈哈，不愧是教授。\x01",
            "你还真是有兴致呀～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        (
            "#124F教授，玩笑开过头了吧……\x02\x03",

            "#121F即使是你，\x01",
            "也不能无视本人的意志，\x01",
            "强行将她拉入结社。\x02\x03",

            "这可是『盟主』制定的`\x01",
            "『噬身之蛇』规约。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "#1151F#2P哼哼，这自然不用你说。\x02\x03",

            "你以为身为『蛇之使徒』的我\x01",
            "会做出那种事吗？\x02\x03",

            "包括你和约修亚在内，\x01",
            "我也没有强迫过任何人吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        "#120F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        (
            "#1154F#2P要是那么做的话，\x01",
            "难得的乐趣就都被破坏了。\x02\x03",

            "必须让她完全自愿地\x01",
            "加入我们才行。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(500)
    ClearMapFlags(0x2000000)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_236C end

    def Function_25_3A92(): pass

    label("Function_25_3A92")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3B0F"),
        (1, "loc_3B15"),
        (SWITCH_DEFAULT, "loc_3B1B"),
    )


    label("loc_3B0F")

    OP_A2(0x1200)
    Jump("loc_3B1B")

    label("loc_3B15")

    OP_A2(0x1201)
    Jump("loc_3B1B")

    label("loc_3B1B")

    Return()

    # Function_25_3A92 end

    def Function_26_3B1C(): pass

    label("Function_26_3B1C")

    ClearMapFlags(0x1)
    OP_6D(-136530, -6000, 47970, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_26_3B1C end

    def Function_27_3B79(): pass

    label("Function_27_3B79")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3BF3"),
        (1, "loc_3BF9"),
        (SWITCH_DEFAULT, "loc_3BFF"),
    )


    label("loc_3BF3")

    OP_A2(0x1200)
    Jump("loc_3BFF")

    label("loc_3BF9")

    OP_A2(0x1201)
    Jump("loc_3BFF")

    label("loc_3BFF")

    Return()

    # Function_27_3B79 end

    def Function_28_3C00(): pass

    label("Function_28_3C00")

    TalkBegin(0xFF)
    OP_22(0x6D, 0x0, 0x64)
    TalkEnd(0xFF)
    Return()

    # Function_28_3C00 end

    def Function_29_3C0C(): pass

    label("Function_29_3C0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C5D")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #82
        "\x07\x05导力好像停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_3E1B")

    label("loc_3C5D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #83
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E00")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x6, 0x2)
    PlayEffect(0x6, 0x6, 0xFF, -4500, -5000, -27040, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1D, 0)
    OP_70(0x1D, 0x32)
    OP_73(0x1D)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x6, 0x2)
    LoadEffect(0x7, "map\\\\mp027_01.eff")
    PlayEffect(0x7, 0x7, 0xFF, -4500, -5000, -27040, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x7, 0x2)
    PlayEffect(0x6, 0x6, 0xFF, -4500, -5000, -27040, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x1D, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_3E00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E1A")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_3E1A")

    Return()

    label("loc_3E1B")

    Return()

    # Function_29_3C0C end

    SaveToFile()

Try(main)
