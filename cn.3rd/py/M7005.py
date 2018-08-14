from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7005   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7005.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60220",
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
        '异形的男人',                           # 9
        '贝沃',                                 # 10
        '伪装雕像',                             # 11
        '伪装雕像',                             # 12
        '伪装雕像',                             # 13
        '伪装雕像',                             # 14
        '',                                     # 15
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
        'ED6_DT27/CH04080 ._CH',             # 00
        'ED6_DT27/CH04150 ._CH',             # 01
        'ED6_DT07/CH00160 ._CH',             # 02
        'ED6_DT27/CH04580 ._CH',             # 03
        'ED6_DT29/CH14100 ._CH',             # 04
        'ED6_DT29/CH14110 ._CH',             # 05
        'ED6_DT27/CH04084 ._CH',             # 06
        'ED6_DT27/CH04154 ._CH',             # 07
        'ED6_DT07/CH00164 ._CH',             # 08
        'ED6_DT27/CH04584 ._CH',             # 09
        'ED6_DT27/CH04081 ._CH',             # 0A
        'ED6_DT27/CH04151 ._CH',             # 0B
        'ED6_DT07/CH00161 ._CH',             # 0C
        'ED6_DT27/CH04581 ._CH',             # 0D
        'ED6_DT27/CH03440 ._CH',             # 0E
        'ED6_DT27/CH04450 ._CH',             # 0F
        'ED6_DT27/CH04457 ._CH',             # 10
        'ED6_DT27/CH04458 ._CH',             # 11
        'ED6_DT27/CH04152 ._CH',             # 12
        'ED6_DT27/CH04153 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT27/CH04080P._CP',             # 00
        'ED6_DT27/CH04150P._CP',             # 01
        'ED6_DT07/CH00160P._CP',             # 02
        'ED6_DT27/CH04580P._CP',             # 03
        'ED6_DT29/CH14100P._CP',             # 04
        'ED6_DT29/CH14110P._CP',             # 05
        'ED6_DT27/CH04084P._CP',             # 06
        'ED6_DT27/CH04154P._CP',             # 07
        'ED6_DT07/CH00164P._CP',             # 08
        'ED6_DT27/CH04584P._CP',             # 09
        'ED6_DT27/CH04081P._CP',             # 0A
        'ED6_DT27/CH04151P._CP',             # 0B
        'ED6_DT07/CH00161P._CP',             # 0C
        'ED6_DT27/CH04581P._CP',             # 0D
        'ED6_DT27/CH03440P._CP',             # 0E
        'ED6_DT27/CH04450P._CP',             # 0F
        'ED6_DT27/CH04457P._CP',             # 10
        'ED6_DT27/CH04458P._CP',             # 11
        'ED6_DT27/CH04152P._CP',             # 12
        'ED6_DT27/CH04153P._CP',             # 13
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -3160,
        Y                   = -4000,
        Z                   = -5800,
        Range               = 2700,
        Unknown_10          = 0x73A,
        Unknown_14          = 0xFFFFF902,
        Unknown_18          = 0x0,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = -7280,
        Y                   = -500,
        Z                   = 57400,
        Range               = 7140,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xEC2C,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )

    DeclEvent(
        X                   = -4140,
        Y                   = 0,
        Z                   = 119500,
        Range               = 4880,
        Unknown_10          = 0x1F40,
        Unknown_14          = 0x1DC90,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )


    DeclActor(
        TriggerX            = 7900,
        TriggerZ            = -4000,
        TriggerY            = 13920,
        TriggerRange        = 1000,
        ActorX              = 7900,
        ActorZ              = -2000,
        ActorY              = 13920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_28E",          # 00, 0
        "Function_1_2EF",          # 01, 1
        "Function_2_356",          # 02, 2
        "Function_3_815",          # 03, 3
        "Function_4_82A",          # 04, 4
        "Function_5_844",          # 05, 5
        "Function_6_85E",          # 06, 6
        "Function_7_878",          # 07, 7
        "Function_8_889",          # 08, 8
        "Function_9_1024",         # 09, 9
        "Function_10_1062",        # 0A, 10
        "Function_11_111B",        # 0B, 11
        "Function_12_11D4",        # 0C, 12
        "Function_13_128D",        # 0D, 13
        "Function_14_1346",        # 0E, 14
        "Function_15_269D",        # 0F, 15
        "Function_16_26CB",        # 10, 16
        "Function_17_26F9",        # 11, 17
        "Function_18_2727",        # 12, 18
        "Function_19_2750",        # 13, 19
        "Function_20_2772",        # 14, 20
        "Function_21_28CE",        # 15, 21
        "Function_22_2A3C",        # 16, 22
        "Function_23_2D05",        # 17, 23
        "Function_24_2E3D",        # 18, 24
        "Function_25_30D5",        # 19, 25
        "Function_26_31B3",        # 1A, 26
        "Function_27_3293",        # 1B, 27
        "Function_28_33A9",        # 1C, 28
        "Function_29_33F7",        # 1D, 29
        "Function_30_34FE",        # 1E, 30
    )


    def Function_0_28E(): pass

    label("Function_0_28E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_2A6"),
        (SWITCH_DEFAULT, "loc_2AD"),
    )


    label("loc_2A6")

    Event(0, 25)
    Jump("loc_2AD")

    label("loc_2AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD")
    Event(0, 30)

    label("loc_2BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D2")
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2EE")
    OP_A3(0x2504)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 14)

    label("loc_2EE")

    Return()

    # Function_0_28E end

    def Function_1_2EF(): pass

    label("Function_1_2EF")

    OP_16(0x2, 0xFA0, 0xFFFE0B06, 0xFFFF32EC, 0x230081)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31A")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_31A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B")
    OP_1B(0x2, 0x0, 0x1A)

    label("loc_32B")

    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_72(0x801, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_355")
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x87, 0x0)

    label("loc_355")

    Return()

    # Function_1_2EF end

    def Function_2_356(): pass

    label("Function_2_356")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_B0(0x1, 0x28)
    OP_6F(0x1, 270)
    OP_70(0x1, 0x10E)
    OP_48()
    OP_6D(100, 15150, -3280, 0)
    OP_67(0, 12150, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(20000, 0)
    OP_6E(262, 0)
    OP_89(0x109, 0, 43000, -3270, 0)
    OP_89(0x10F, 900, 43000, -4180, 0)
    OP_89(0x107, -900, 43000, -4190, 0)
    OP_89(0x10E, 0, 43000, -5060, 0)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_B0(0x1, 0x28)
    OP_6F(0x1, 270)
    OP_70(0x1, 0x0)

    def lambda_418():
        OP_6D(10, -3850, -4150, 7000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_418)

    def lambda_430():
        OP_67(0, 8500, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_430)

    def lambda_448():
        OP_6B(3400, 7000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_448)

    def lambda_458():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_458)
    FadeToBright(1000, 0)
    Sleep(5000)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    WaitChrThread(0x0, 0x0)
    Sleep(500)

    def lambda_4D4():
        OP_6D(500, -4000, 10900, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4D4)

    def lambda_4EC():
        OP_67(0, 5770, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4EC)

    def lambda_504():
        OP_6B(3200, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_504)

    def lambda_514():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_514)

    def lambda_524():
        OP_6E(255, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_524)
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    OP_43(0x107, 0x0, 0x0, 0x5)
    OP_43(0x10E, 0x0, 0x0, 0x6)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #0
        0x10F,
        "#1444F#6P这气味……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        "#1063F#6P……你也感觉到了？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    OP_62(0x107, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #2
        0x107,
        "#064F#6P怎、怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10E,
        (
            "#172F魔兽的气息……？\x01",
            "我什么也没有感觉到啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_664():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_664)
    Sleep(100)
    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #4
        0x109,
        (
            "#1067F#5P不，不是教会的人的话，\x01",
            "是无法感觉到这种气味的。\x02\x03",

            "#1063F腐臭……\x01",
            "不，应该说是黄泉的气息才对。\x02\x03",

            "虽然十分微弱，\x01",
            "不过正从前方不断飘散过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        (
            "#1445F#5P与刚才遇到的骸骨相比，\x01",
            "可能是更加厉害的家伙……\x02\x03",

            "#1443F也许，是相当麻烦的敌人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x107,
        "#065F#6P哇、哇啊～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10E,
        (
            "#176F是吗……\x02\x03",

            "#178F……看起来，\x01",
            "我们要做好迎战准备了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x261C)
    OP_28(0x2A, 0x1, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_356 end

    def Function_3_815(): pass

    label("Function_3_815")

    OP_8E(0xFE, 0xFFFFFAC4, 0xFFFFF060, 0x2B5C, 0x7D0, 0x0)
    Return()

    # Function_3_815 end

    def Function_4_82A(): pass

    label("Function_4_82A")

    Sleep(300)
    OP_8E(0xFE, 0xE6, 0xFFFFF060, 0x2AF8, 0x7D0, 0x0)
    Return()

    # Function_4_82A end

    def Function_5_844(): pass

    label("Function_5_844")

    Sleep(800)
    OP_8E(0xFE, 0xFFFFFAA6, 0xFFFFF060, 0x2382, 0x7D0, 0x0)
    Return()

    # Function_5_844 end

    def Function_6_85E(): pass

    label("Function_6_85E")

    Sleep(1200)
    OP_8E(0xFE, 0x10E, 0xFFFFF060, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_6_85E end

    def Function_7_878(): pass

    label("Function_7_878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 5)), scpexpr(EXPR_END)), "loc_880")
    Return()

    label("loc_880")

    Call(0, 8)
    Call(0, 14)
    Return()

    # Function_7_878 end

    def Function_8_889(): pass

    label("Function_8_889")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1001.eff")
    Fade(1000)
    OP_6D(-660, 0, 78450, 0)
    OP_67(0, 8630, -10000, 0)
    OP_6B(4780, 0)
    OP_6C(45000, 0)
    OP_6E(311, 0)

    def lambda_90F():
        OP_6D(1060, 0, 71500, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_90F)

    def lambda_927():
        OP_67(0, 5020, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_927)

    def lambda_93F():
        OP_6B(2860, 6000)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_93F)

    def lambda_94F():
        OP_6E(384, 6000)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_94F)
    Sleep(1000)
    SetChrPos(0x109, -1290, 0, 59520, 0)
    SetChrPos(0x10F, 50, 0, 58970, 0)
    SetChrPos(0x107, -1320, 0, 57630, 0)
    SetChrPos(0x10E, 30, 0, 57000, 0)
    Sleep(1000)

    def lambda_9AD():
        OP_8E(0xFE, 0xFFFFFAE2, 0x0, 0x10162, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9AD)
    Sleep(50)

    def lambda_9CD():
        OP_8E(0xFE, 0xAA, 0x0, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_9CD)
    Sleep(50)

    def lambda_9ED():
        OP_8E(0xFE, 0xFFFFF9C0, 0x0, 0xFB72, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9ED)
    Sleep(100)

    def lambda_A0D():
        OP_8E(0xFE, 0xDC, 0x0, 0xFA96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_A0D)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x10F, 0x1)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x10E, 0x1)
    OP_20(0x7D0)
    Fade(1000)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, 0, 200, 75690, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 0)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 1)
    SetChrSubChip(0x10F, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 2)
    SetChrSubChip(0x107, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 3)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #8
        0x10F,
        "#1441F#5P……来了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x109,
        "#1069F#6P和预料的一样……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0x9A)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(-30, 0, 76870, 0)
    OP_67(0, 6360, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(0, 0)
    OP_6E(389, 0)
    PlayEffect(0x1, 0x1, 0xFF, 0, 100, 75690, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_43(0x11, 0x0, 0x0, 0x9)
    SetChrPos(0x109, -650, 0, 67010, 0)
    SetChrPos(0x10F, 850, 0, 67070, 0)
    SetChrPos(0x107, -1330, 0, 65030, 0)
    SetChrPos(0x10E, 1380, 0, 64840, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_C75():

        label("loc_C75")

        OP_7C(0x50, 0x50, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_C75")

    QueueWorkItem2(0x10F, 0, lambda_C75)

    def lambda_C90():
        OP_6D(0, 0, 78100, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_C90)

    def lambda_CA8():
        OP_67(0, 4430, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CA8)

    def lambda_CC0():
        OP_6B(1900, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_CC0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x109, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(1000)

    def lambda_CE5():
        OP_6D(0, 0, 77180, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CE5)

    def lambda_CFD():
        OP_67(0, 5710, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CFD)

    def lambda_D15():
        OP_6B(2250, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D15)
    OP_43(0x12, 0x0, 0x0, 0xA)
    OP_43(0x13, 0x0, 0x0, 0xB)
    OP_43(0x14, 0x0, 0x0, 0xC)
    OP_43(0x15, 0x0, 0x0, 0xD)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x15, 0x0)
    OP_44(0x10F, 0x0)
    OP_23(0x85)
    Sleep(1000)

    def lambda_D61():
        OP_6D(0, -700, 77000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D61)

    def lambda_D79():
        OP_67(0, 2600, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D79)

    def lambda_D91():
        OP_6B(3220, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D91)

    def lambda_DA1():
        OP_6E(339, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_DA1)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #10
        0x107,
        "#065F#6P哇哇……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10E,
        "#172F#6P什、什么啊，那是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10F,
        (
            "#1446F#6P黄泉的摆渡者。\x01",
            "引导死魂的灵柩。\x02\x03",

            "#1441F是记载于圣典的\x01",
            "七十七恶魔的其中一匹，\x01",
            "『叹息之柩』贝沃……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        (
            "#1065F#6P没想到居然有\x01",
            "与真正的恶魔面对面较量的一天……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #14
        0x109,
        (
            "#1069F#6P正合我意！\x01",
            "让他们见识一下女神之仆的力量！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_F1D():
        OP_6D(0, -400, 77950, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F1D)

    def lambda_F35():
        OP_67(0, 2260, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F35)

    def lambda_F4D():
        OP_6B(3500, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F4D)

    def lambda_F5D():
        OP_6E(360, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_F5D)
    PlayEffect(0x2, 0xFF, 0xFF, 0, 100, 75690, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_22(0x32E, 0x0, 0x64)

    def lambda_FA7():

        label("loc_FA7")

        OP_7C(0x50, 0x50, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_FA7")

    QueueWorkItem2(0x10F, 0, lambda_FA7)
    Sleep(2000)

    def lambda_FC7():
        OP_6D(0, -300, 77950, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FC7)

    def lambda_FDF():
        OP_67(0, 2130, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FDF)

    def lambda_FF7():
        OP_6B(2540, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_FF7)

    def lambda_1007():
        OP_6E(358, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1007)
    WaitChrThread(0x109, 0x0)
    Battle(0x73, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_8_889 end

    def Function_9_1024(): pass

    label("Function_9_1024")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, -5000, 75400, 180)

    def lambda_1040():

        label("loc_1040")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1040")

    QueueWorkItem2(0xFE, 1, lambda_1040)
    OP_8F(0xFE, 0x0, 0x3E8, 0x12688, 0x5DC, 0x0)
    Return()

    # Function_9_1024 end

    def Function_10_1062(): pass

    label("Function_10_1062")

    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, -2800, 100, 73500, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_0D()
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2800, -3000, 73500, 180)

    def lambda_10BE():

        label("loc_10BE")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_10BE")

    QueueWorkItem2(0xFE, 1, lambda_10BE)
    PlayEffect(0x1, 0x1, 0xFF, -2800, 100, 73500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_8F(0xFE, 0xFFFFF510, 0x0, 0x11F1C, 0x5DC, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Return()

    # Function_10_1062 end

    def Function_11_111B(): pass

    label("Function_11_111B")

    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, 2800, 100, 73500, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_0D()
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 2800, -3000, 73500, 180)

    def lambda_1177():

        label("loc_1177")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1177")

    QueueWorkItem2(0xFE, 1, lambda_1177)
    PlayEffect(0x1, 0x3, 0xFF, 2800, 100, 73500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_8F(0xFE, 0xAF0, 0x0, 0x11F1C, 0x5DC, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    Return()

    # Function_11_111B end

    def Function_12_11D4(): pass

    label("Function_12_11D4")

    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0xFF, -2800, 100, 78000, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_0D()
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2800, -3000, 78000, 180)

    def lambda_1230():

        label("loc_1230")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1230")

    QueueWorkItem2(0xFE, 1, lambda_1230)
    PlayEffect(0x1, 0x5, 0xFF, -2800, 100, 78000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_8F(0xFE, 0xFFFFF510, 0x0, 0x130B0, 0x5DC, 0x0)
    OP_82(0x4, 0x2)
    OP_82(0x5, 0x2)
    Return()

    # Function_12_11D4 end

    def Function_13_128D(): pass

    label("Function_13_128D")

    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x6, 0xFF, 2800, 100, 78000, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_0D()
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 2800, -3000, 78000, 180)

    def lambda_12E9():

        label("loc_12E9")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_12E9")

    QueueWorkItem2(0xFE, 1, lambda_12E9)
    PlayEffect(0x1, 0x7, 0xFF, 2800, 100, 78000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_8F(0xFE, 0xAF0, 0x0, 0x130B0, 0x5DC, 0x0)
    OP_82(0x6, 0x2)
    OP_82(0x7, 0x2)
    Return()

    # Function_13_128D end

    def Function_14_1346(): pass

    label("Function_14_1346")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_44(0x10F, 0x0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05莉丝学会了Ｓ战技\x01",
            "\x07\x02『天堂阻灭』\x07\x05。\x02",
        )
    )

    Jump("loc_13C5")

    label("loc_13C5")

    CloseMessageWindow()
    OP_22(0x21E, 0x0, 0x64)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #16
        "\x07\x05将『天堂阻灭』设定为Ｓ爆发技吗？\x18\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1410")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1490")

    Menu(
        1,
        -1,
        200,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_1446")

    label("loc_1446")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1464"),
        (SWITCH_DEFAULT, "loc_147C"),
    )


    label("loc_1464")

    OP_35(0xE, 0x11A)
    OP_BB(0xE, 0x6, 0x11A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_148D")

    label("loc_147C")

    OP_35(0xE, 0x11A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_148D")

    label("loc_148D")

    Jump("loc_1410")

    label("loc_1490")

    SetMessageWindowPos(72, 320, 56, 3)
    SetChrPos(0x109, -850, 0, 78370, 0)
    SetChrPos(0x10F, 1050, 0, 78060, 0)
    SetChrPos(0x107, -1170, 0, 76180, 0)
    SetChrPos(0x10E, 1090, 0, 76070, 0)
    SetChrChipByIndex(0x109, 6)
    SetChrSubChip(0x109, 3)
    SetChrChipByIndex(0x10F, 7)
    SetChrSubChip(0x10F, 3)
    SetChrChipByIndex(0x107, 8)
    SetChrSubChip(0x107, 3)
    SetChrChipByIndex(0x10E, 9)
    SetChrSubChip(0x10E, 3)
    SetChrFlags(0x109, 0x800)
    SetChrFlags(0x10F, 0x800)
    SetChrFlags(0x107, 0x800)
    SetChrFlags(0x107, 0x800)
    OP_6D(-500, 0, 82670, 0)
    OP_67(0, 8980, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(215000, 0)
    OP_6E(359, 0)

    def lambda_155C():
        OP_6D(-500, 0, 76480, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_155C)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Fade(1000)
    OP_6D(-930, 0, 76280, 0)
    OP_67(0, 4800, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(225000, 0)
    OP_6E(349, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #17
        0x109,
        "#1070F#5P呜……呼……呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10F,
        (
            "#1445F#5P那个是……\x01",
            "……真正的恶魔……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x107,
        "#562F#5P好、好恐怖……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10E,
        (
            "#175F#5P这个世界上，\x01",
            "居然存在着这样的怪物……\x02\x03",

            "这里究竟……\x01",
            "是什么地方啊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x10, 0, 0, 94050, 180)
    ClearChrFlags(0x10, 0x80)
    OP_20(0x7D0)

    NpcTalk(    #21
        0x10,
        "男子的声音",
        (
            "\x07\x05#1P呵呵……\x01",
            "已经开始为前路担忧了吗。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x12C, 1300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x12C, 1300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0xC8, 1300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x12C, 1300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0xB0)

    def lambda_1774():
        OP_6D(-1160, 0, 92580, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1774)

    def lambda_178C():
        OP_67(0, 5320, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_178C)

    def lambda_17A4():
        OP_6B(2400, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_17A4)
    Sleep(1000)
    ClearChrFlags(0x109, 0x800)
    ClearChrFlags(0x10F, 0x800)
    ClearChrFlags(0x107, 0x800)
    ClearChrFlags(0x107, 0x800)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)
    Fade(1000)
    OP_6D(-1240, 0, 95180, 0)
    OP_67(0, 4860, -10000, 0)
    OP_6B(2420, 0)
    OP_6C(315000, 0)
    OP_6E(357, 0)

    def lambda_181E():
        OP_6B(2150, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_181E)
    SetChrFlags(0x109, 0x800)
    SetChrFlags(0x10F, 0x800)
    SetChrFlags(0x107, 0x800)
    SetChrFlags(0x107, 0x800)
    OP_0D()
    Sleep(500)

    ChrTalk(    #22
        0x109,
        "#1063F#2P！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10F,
        "#1441F#2P是那个时候的……！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)

    def lambda_1896():
        OP_8E(0xFE, 0xFFFFFE98, 0x0, 0x15842, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1896)
    OP_6D(-1700, 300, 82800, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(314000, 0)
    OP_6E(355, 0)

    def lambda_18EE():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_18EE)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 0)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 1)
    SetChrSubChip(0x10F, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 2)
    SetChrSubChip(0x107, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 3)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    ClearChrFlags(0x109, 0x800)
    ClearChrFlags(0x10F, 0x800)
    ClearChrFlags(0x107, 0x800)
    ClearChrFlags(0x107, 0x800)
    Sleep(500)

    ChrTalk(    #24
        0x10E,
        (
            "#178F#6P他就是你们被光包围时\x01",
            "出现的那个奇怪男人吗……\x02\x03",

            "#177F你是何方神圣！？报上名来！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0x2)
    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #25
        0x10,
        (
            "\x07\x05#1591F哼……\x02\x03",

            "想要别人报上姓名的话，\x01",
            "首先应该报上自己的名字，\x01",
            "这才合乎规矩对吧？\x02\x03",

            "王室亲卫队大队长……\x01",
            "尤莉亚·舒华兹上尉。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0x10E,
        "#178F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1075F#6P看起来，\x01",
            "你对我们的身份调查得相当透彻嘛……\x02\x03",

            "#1060F你到底有什么目的？\x01",
            "刚才的恶魔是你召唤的吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #28
        0x109,
        (
            "#1069F#3S导致如今这种境况，\x01",
            "也是你这家伙干的好事吧！？\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "\x07\x05#1591F呵呵呵……\x01",
            "乱吼什么呀，凯文·格拉汉姆。\x02\x03",

            "你们的苦难\x01",
            "才刚刚开始……\x02\x03",

            "何必现在就急于陷入\x01",
            "绝望的境地之中呢……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        "#1063F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10F,
        "#1441F#6P…………哎…………………\x02",
    )

    CloseMessageWindow()

    def lambda_1C7B():
        OP_6D(-1300, 300, 88700, 800)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1C7B)

    def lambda_1C93():
        OP_67(0, 3490, -10000, 800)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1C93)

    def lambda_1CAB():
        OP_6B(2700, 1000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1CAB)

    def lambda_1CBB():
        OP_6C(338000, 800)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_1CBB)

    def lambda_1CCB():
        OP_6E(290, 800)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1CCB)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    LoadEffect(0x0, "map\\mp009_00.eff")
    OP_43(0x10F, 0x0, 0x0, 0x14)
    Sleep(100)
    OP_22(0x1F5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 15)
    SetChrSubChip(0x10, 0)
    Sleep(300)
    OP_43(0x10, 0x0, 0x0, 0x13)
    Sleep(500)
    FadeToDark(100, 16777215, 100)
    OP_22(0xD6, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, -300, 600, 87040, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0xFF, -300, 600, 87040, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)

    def lambda_1DA1():
        OP_7C(0xC8, 0xC8, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1DA1)
    Sleep(100)
    FadeToBright(100, 16777215)

    def lambda_1DC7():
        OP_6D(-450, 200, 85130, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1DC7)

    def lambda_1DDF():
        OP_67(0, 3000, -10000, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1DDF)

    def lambda_1DF7():
        OP_6B(3200, 2500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1DF7)

    def lambda_1E07():
        OP_6C(0, 500)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_1E07)

    def lambda_1E17():
        OP_6E(295, 2500)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1E17)
    SetChrPos(0x109, -850, 0, 78370, 0)
    SetChrPos(0x107, -1370, 0, 76180, 0)
    SetChrPos(0x10E, 900, 0, 76700, 0)
    WaitChrThread(0x10F, 0x0)
    OP_43(0x10F, 0x0, 0x0, 0x15)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    ChrTalk(    #32
        0x10F,
        "#1804F#6P……啊…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x109,
        "#1069F#6P莉丝……别乱来！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 15)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)

    def lambda_1EEC():
        OP_6B(3350, 10000)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_1EEC)

    def lambda_1EFC():
        OP_6E(300, 10000)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1EFC)

    ChrTalk(    #34
        0x10,
        (
            "\x07\x05#1591F#5P呵呵，七耀教会的法剑吗？\x02\x03",

            "技术的确出类拔萃……\x01",
            "不过，和你姐姐比起来，还相差甚远。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #35
        0x109,
        "#1079F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10F,
        "#1802F#6P………为什么……………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "\x07\x05#1591F#5P哈哈哈，别急嘛。\x02\x03",

            "由我们『影之国』所筹备的绝望之宴\x01",
            "才刚刚开始……\x02\x03",

            "挣扎吧，在深渊中做无谓的抗争吧。\x01",
            "若是不将你们折磨得死去活来的话，\x01",
            "我们的『王』会不高兴的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\mp254_00.eff")
    LoadEffect(0x1, "map\\mp254_02.eff")
    Sleep(300)
    Fade(1000)
    PlayEffect(0x0, 0x0, 0xFF, -360, 0, 88130, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_22(0xBA, 0x1, 0x64)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #38
        0x109,
        "#1069F#6P慢、慢着……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10E,
        "#177F#6P想逃吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        (
            "\x07\x05#1590F#5P……我就告诉你们一件事情，\x01",
            "当作见面礼吧。\x02\x03",

            "我的名字是『黑骑士』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #41
        0x10,
        "黑骑士",
        (
            "\x07\x05#1591F#5P侍奉伟大之『王』的\x01",
            "『影之国』的守护者。\x02\x03",

            "那么，后会有期——\x07\x00\x02",
        )
    )

    Jump("loc_22B1")

    label("loc_22B1")

    CloseMessageWindow()

    def lambda_22B8():
        OP_6D(570, 0, 90330, 1200)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_22B8)

    def lambda_22D0():
        OP_67(0, 5420, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_22D0)

    def lambda_22E8():
        OP_6B(2420, 1200)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_22E8)

    def lambda_22F8():
        OP_6C(45000, 1200)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_22F8)

    def lambda_2308():
        OP_6E(365, 1200)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_2308)
    WaitChrThread(0x109, 0x0)
    OP_43(0x109, 0x0, 0x0, 0xF)
    PlayEffect(0x1, 0x1, 0x10, 0, 500, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_2359():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2359)
    OP_22(0x59, 0x0, 0x64)
    OP_23(0xBA)
    OP_82(0x0, 0x2)
    Sleep(100)
    OP_43(0x10E, 0x0, 0x0, 0x11)
    Sleep(50)
    OP_43(0x10F, 0x0, 0x0, 0x10)
    Sleep(100)
    OP_43(0x107, 0x0, 0x0, 0x12)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(1000)
    Fade(500)
    SetChrSubChip(0x0, 0)
    SetChrChipByIndex(0x0, 65535)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(50)
    SetChrSubChip(0x1, 0)
    SetChrChipByIndex(0x1, 65535)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(50)
    SetChrSubChip(0x2, 0)
    SetChrChipByIndex(0x2, 65535)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(50)
    SetChrSubChip(0x3, 0)
    SetChrChipByIndex(0x3, 65535)
    OP_22(0xD5, 0x0, 0x64)
    OP_0D()
    Sleep(500)
    SetChrFlags(0x10, 0x80)

    ChrTalk(    #42
        0x109,
        "#1067F#5P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x107,
        "#065F#6P消、消失了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10F,
        "#1445F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10E,
        (
            "#176F#6P虽然还无法判断他是什么人……\x01",
            "不过，有件事已经非常清楚了。\x02\x03",

            "#178F……看来，\x01",
            "我们面前的确有『敌人』存在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x109,
        "#1065F#5P……啊，是啊。\x02",
    )

    CloseMessageWindow()

    def lambda_2531():
        OP_6D(570, 0, 88330, 1200)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2531)

    def lambda_2549():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2549)
    Sleep(100)

    def lambda_255C():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_255C)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #47
        0x109,
        (
            "#1063F#5P而且……\x01",
            "看起来是相当棘手的敌人呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_25B7():
        OP_6B(3200, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_25B7)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x261D)
    OP_44(0x109, 0x2)
    Sleep(3000)
    OP_AD(0x2400ED, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x2582)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x156), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存】\x01",              # 0
            "【继续下面剧情】\x01",      # 1
        )
    )

    Jump("loc_2640")

    label("loc_2640")

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2654")
    ShowSaveMenu()

    label("loc_2654")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_20(0x7D0)
    OP_21()
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2507)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_14_1346 end

    def Function_15_269D(): pass

    label("Function_15_269D")

    SetChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 10)
    OP_8E(0xFE, 0xFFFFF93E, 0x0, 0x157F2, 0x1770, 0x0)
    ClearChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 0)
    SetChrSubChip(0x109, 0)
    Return()

    # Function_15_269D end

    def Function_16_26CB(): pass

    label("Function_16_26CB")

    SetChrFlags(0x10F, 0x1000)
    SetChrChipByIndex(0x10F, 11)
    OP_8E(0xFE, 0x50, 0x0, 0x1572A, 0x1770, 0x0)
    ClearChrFlags(0x10F, 0x1000)
    SetChrChipByIndex(0x10F, 1)
    SetChrSubChip(0x10F, 0)
    Return()

    # Function_16_26CB end

    def Function_17_26F9(): pass

    label("Function_17_26F9")

    SetChrFlags(0x10E, 0x1000)
    SetChrChipByIndex(0x10E, 13)
    OP_8E(0xFE, 0x0, 0x0, 0x14FBE, 0x1770, 0x0)
    ClearChrFlags(0x10F, 0x1000)
    ClearChrFlags(0x10E, 0x1000)
    SetChrChipByIndex(0x10E, 3)
    Return()

    # Function_17_26F9 end

    def Function_18_2727(): pass

    label("Function_18_2727")

    SetChrFlags(0x107, 0x1000)
    SetChrChipByIndex(0x107, 12)
    OP_8E(0xFE, 0xFFFFF86C, 0x0, 0x14F14, 0x1770, 0x0)
    ClearChrFlags(0x107, 0x1000)
    SetChrChipByIndex(0x107, 2)
    Return()

    # Function_18_2727 end

    def Function_19_2750(): pass

    label("Function_19_2750")

    SetChrChipByIndex(0x10, 16)
    OP_99(0x10, 0x9, 0xF, 0xDAC)
    SetChrChipByIndex(0x10, 17)
    OP_99(0x10, 0x0, 0x5, 0xDAC)
    OP_22(0x1F9, 0x0, 0x64)
    Return()

    # Function_19_2750 end

    def Function_20_2772(): pass

    label("Function_20_2772")

    SetChrFlags(0xFE, 0x4)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    SetChrFlags(0xFE, 0x1000)
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0xFE, 11)

    def lambda_279B():
        OP_8F(0xFE, 0xFFFFFED4, 0x0, 0x13E5C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_279B)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 2)
    WaitChrThread(0xFE, 0x1)

    def lambda_27CA():
        OP_96(0xFE, 0xFFFFFC18, 0x64, 0x14A78, 0x578, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_27CA)
    OP_51(0x10F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0xC5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x4F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 18)
    SetChrSubChip(0xFE, 2)
    Sleep(300)

    def lambda_28A7():
        OP_99(0xFE, 0x3, 0x5, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_28A7)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_20_2772 end

    def Function_21_28CE(): pass

    label("Function_21_28CE")

    OP_51(0x10F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrPos(0xFE, 0, 100, 84600, 0)

    def lambda_299A():
        OP_96(0xFE, 0xF0, 0x0, 0x1437A, 0x320, 0x1F40)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_299A)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Sleep(150)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)

    def lambda_29DB():
        OP_99(0xFE, 0x1, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_29DB)

    def lambda_29EB():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_29EB)
    OP_8F(0xFE, 0x1B8, 0x0, 0x13BAA, 0x1770, 0x0)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_21_28CE end

    def Function_22_2A3C(): pass

    label("Function_22_2A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 1)), scpexpr(EXPR_END)), "loc_2A44")
    Return()

    label("loc_2A44")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(500, 4250, 134700, 0)
    OP_67(0, 10740, -10000, 0)
    OP_6B(3480, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x109, -220, 4250, 122750, 0)
    SetChrPos(0x10F, 680, 4250, 121750, 0)
    SetChrPos(0x107, -1250, 4250, 121850, 0)
    SetChrPos(0x10E, -290, 4250, 121530, 0)
    OP_0D()

    def lambda_2AD3():
        OP_6D(1050, 4250, 132190, 5500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2AD3)

    def lambda_2AEB():
        OP_67(0, 6320, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2AEB)

    def lambda_2B03():
        OP_6B(3300, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2B03)

    def lambda_2B13():
        OP_6C(45000, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2B13)

    def lambda_2B23():
        OP_6E(253, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_2B23)
    Sleep(1000)

    def lambda_2B38():
        OP_8E(0xFE, 0xA, 0x109A, 0x1FE96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2B38)
    Sleep(200)

    def lambda_2B58():
        OP_8E(0xFE, 0x398, 0x109A, 0x1F9A9, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2B58)
    Sleep(400)

    def lambda_2B78():
        OP_8E(0xFE, 0xFFFFFAF6, 0x109A, 0x1FA40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2B78)
    Sleep(700)

    def lambda_2B98():
        OP_8E(0xFE, 0xFFFFFE70, 0x109A, 0x1F4A9, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_2B98)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #48
        0x10E,
        (
            "#178F#6P这里是出口……\x01",
            "不，是通往下一层的入口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x107,
        (
            "#063F和设置在『据点』的魔法阵\x01",
            "是同一种形状……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10F,
        (
            "#1445F……………………………\x02\x03",

            "#1443F就是说，\x01",
            "这前面还可以通向其它地方吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x109,
        (
            "#1065F#5P……应该是。\x02\x03",

            "#1063F还是先做好战斗准备，\x01",
            "然后再进去为妙。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2701)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_22_2A3C end

    def Function_23_2D05(): pass

    label("Function_23_2D05")

    EventBegin(0x0)
    Fade(500)
    OP_6D(970, 4250, 135000, 0)
    OP_67(0, 7890, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(260, 0)
    SetChrPos(0x109, 40, 4250, 135380, 0)
    SetChrPos(0x10F, 1080, 4250, 134340, 0)
    SetChrPos(0x107, -800, 4250, 134190, 0)
    SetChrPos(0x10E, 200, 4250, 133170, 0)

    def lambda_2D93():
        OP_6D(790, 4250, 133520, 9000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2D93)

    def lambda_2DAB():
        OP_6B(2100, 9000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2DAB)

    def lambda_2DBB():
        OP_6C(135000, 9000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_2DBB)
    OP_0D()
    Sleep(500)
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 220, 4250, 134230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 28)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/U4100   ._SN", 115, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_23_2D05 end

    def Function_24_2E3D(): pass

    label("Function_24_2E3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0C")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(512)
    Sleep(500)
    Jump("loc_2F0F")

    label("loc_2F0C")

    TalkBegin(0xFF)

    label("loc_2F0F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #52
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_2F39")

    label("loc_2F39")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30A4")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_2F9E")

    label("loc_2F9E")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FBB"),
        (1, "loc_3036"),
        (2, "loc_3065"),
        (SWITCH_DEFAULT, "loc_3094"),
    )


    label("loc_2FBB")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xDC)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30A1")

    label("loc_3036")

    OP_A9(0x15)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #53
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_3062")

    label("loc_3062")

    Jump("loc_30A1")

    label("loc_3065")

    OP_A9(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #54
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_3091")

    label("loc_3091")

    Jump("loc_30A1")

    label("loc_3094")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30A1")

    label("loc_30A1")

    Jump("loc_2F4C")

    label("loc_30A4")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30D1")
    OP_A2(0x2585)
    EventEnd(0x1)
    Jump("loc_30D4")

    label("loc_30D1")

    TalkEnd(0xFF)

    label("loc_30D4")

    Return()

    # Function_24_2E3D end

    def Function_25_30D5(): pass

    label("Function_25_30D5")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 200, 4250, 133170, 180)
    SetChrPos(0x1, -800, 4250, 134000, 180)
    SetChrPos(0x2, 1080, 4250, 134100, 180)
    SetChrPos(0x3, 40, 4250, 135000, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 220, 4250, 134230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 27)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_25_30D5 end

    def Function_26_31B3(): pass

    label("Function_26_31B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31C3")
    Call(0, 23)

    label("loc_31C3")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 200, 4250, 133170, 0)
    SetChrPos(0x2, -800, 4250, 134000, 0)
    SetChrPos(0x1, 1080, 4250, 134100, 0)
    SetChrPos(0x0, 40, 4250, 135000, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 220, 4250, 134230, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3289")
    NewScene("ED6_DT21/U4100   ._SN", 115, 0, 0)
    IdleLoop()
    Jump("loc_3292")

    label("loc_3289")

    NewScene("ED6_DT21/U4150   ._SN", 115, 0, 0)
    IdleLoop()

    label("loc_3292")

    Return()

    # Function_26_31B3 end

    def Function_27_3293(): pass

    label("Function_27_3293")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32BC")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_32B0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_32B0)

    label("loc_32BC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32E5")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_32D9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_32D9)

    label("loc_32E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_330E")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3302():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3302)

    label("loc_330E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3337")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_332B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_332B)

    label("loc_3337")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3363")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3363")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_337A")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_337A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3391")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3391")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33A8")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_33A8")

    Return()

    # Function_27_3293 end

    def Function_28_33A9(): pass

    label("Function_28_33A9")


    def lambda_33AF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_33AF)

    def lambda_33C1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_33C1)

    def lambda_33D3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_33D3)

    def lambda_33E5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_33E5)
    Sleep(1000)
    Return()

    # Function_28_33A9 end

    def Function_29_33F7(): pass

    label("Function_29_33F7")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(10, -3850, -4150, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 0, -3850, -5060, 180)
    OP_89(0x1, -900, -3850, -4190, 180)
    OP_89(0x2, 900, -3850, -4180, 180)
    OP_89(0x3, 0, -3850, -3270, 180)
    OP_0D()
    Sleep(300)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_B0(0x1, 0x28)
    OP_6F(0x1, 0)
    OP_70(0x1, 0xE6)

    def lambda_34A7():
        OP_6D(10, 5100, -4150, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_34A7)

    def lambda_34BF():
        OP_67(0, 11530, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_34BF)

    def lambda_34D7():
        OP_6C(20000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_34D7)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7006   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_33F7 end

    def Function_30_34FE(): pass

    label("Function_30_34FE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_B0(0x1, 0x28)
    OP_6F(0x1, 270)
    OP_70(0x1, 0x10E)
    OP_48()
    OP_6D(100, 15150, -3280, 0)
    OP_67(0, 12150, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(20000, 0)
    OP_6E(262, 0)
    OP_89(0x0, 0, 43000, -3270, 0)
    OP_89(0x1, 900, 43000, -4180, 0)
    OP_89(0x2, -900, 43000, -4190, 0)
    OP_89(0x3, 0, 43000, -5060, 0)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_B0(0x1, 0x28)
    OP_6F(0x1, 270)
    OP_70(0x1, 0x0)

    def lambda_35C0():
        OP_6D(10, -3850, -4150, 7000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_35C0)

    def lambda_35D8():
        OP_67(0, 8500, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_35D8)

    def lambda_35F0():
        OP_6B(3400, 7000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_35F0)

    def lambda_3600():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_3600)
    FadeToBright(1000, 0)
    Sleep(5000)
    OP_24(0xEB, 0x5A)
    Sleep(50)
    OP_24(0xEB, 0x50)
    Sleep(50)
    OP_24(0xEB, 0x46)
    Sleep(50)
    OP_24(0xEB, 0x3C)
    Sleep(50)
    OP_24(0xEB, 0x32)
    Sleep(50)
    OP_24(0xEB, 0x28)
    Sleep(50)
    OP_24(0xEB, 0x1E)
    Sleep(50)
    OP_24(0xEB, 0x14)
    Sleep(50)
    OP_24(0xEB, 0xA)
    Sleep(50)
    OP_23(0xEB)
    WaitChrThread(0x0, 0x0)
    Sleep(500)
    Fade(1000)
    SetChrPos(0x0, 120, -4000, -580, 0)
    SetChrPos(0x1, 120, -4000, -580, 0)
    SetChrPos(0x2, 120, -4000, -580, 0)
    SetChrPos(0x3, 120, -4000, -580, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_30_34FE end

    SaveToFile()

Try(main)
