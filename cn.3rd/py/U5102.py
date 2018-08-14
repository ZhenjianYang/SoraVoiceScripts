from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U5102   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U5102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        '影之王',                               # 9
        '阿斯塔尔特',                           # 10
        '封印石',                               # 11
        '莉丝',                                 # 12
        '',                                     # 13
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
        'ED6_DT07/CH02770 ._CH',             # 00
        'ED6_DT26/CH20630 ._CH',             # 01
        'ED6_DT27/CH04082 ._CH',             # 02
        'ED6_DT27/CH03150 ._CH',             # 03
        'ED6_DT27/CH04150 ._CH',             # 04
        'ED6_DT27/CH04151 ._CH',             # 05
        'ED6_DT27/CH04152 ._CH',             # 06
        'ED6_DT27/CH04153 ._CH',             # 07
        'ED6_DT27/CH04154 ._CH',             # 08
        'ED6_DT27/CH04155 ._CH',             # 09
        'ED6_DT27/CH04156 ._CH',             # 0A
        'ED6_DT27/CH04158 ._CH',             # 0B
        'ED6_DT27/CH04159 ._CH',             # 0C
        'ED6_DT26/CH20654 ._CH',             # 0D
        'ED6_DT27/CH03155 ._CH',             # 0E
        'ED6_DT27/CH03151 ._CH',             # 0F
        'ED6_DT26/CH20726 ._CH',             # 10
        'ED6_DT26/CH20727 ._CH',             # 11
        'ED6_DT26/CH20621 ._CH',             # 12
        'ED6_DT26/CH20621 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH02770P._CP',             # 00
        'ED6_DT26/CH20630P._CP',             # 01
        'ED6_DT27/CH04082P._CP',             # 02
        'ED6_DT27/CH03150P._CP',             # 03
        'ED6_DT27/CH04150P._CP',             # 04
        'ED6_DT27/CH04151P._CP',             # 05
        'ED6_DT27/CH04152P._CP',             # 06
        'ED6_DT27/CH04153P._CP',             # 07
        'ED6_DT27/CH04154P._CP',             # 08
        'ED6_DT27/CH04155P._CP',             # 09
        'ED6_DT27/CH04156P._CP',             # 0A
        'ED6_DT27/CH04158P._CP',             # 0B
        'ED6_DT27/CH04159P._CP',             # 0C
        'ED6_DT26/CH20654P._CP',             # 0D
        'ED6_DT27/CH03155P._CP',             # 0E
        'ED6_DT27/CH03151P._CP',             # 0F
        'ED6_DT26/CH20726P._CP',             # 10
        'ED6_DT26/CH20727P._CP',             # 11
        'ED6_DT26/CH20621P._CP',             # 12
        'ED6_DT26/CH20621P._CP',             # 13
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -9530,
        Y                   = -1000,
        Z                   = 25280,
        Range               = 17600,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x77A6,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -3300,
        Y                   = -1000,
        Z                   = 40000,
        Range               = 9080,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xB14E,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )


    DeclActor(
        TriggerX            = -3550,
        TriggerZ            = 0,
        TriggerY            = -3000,
        TriggerRange        = 800,
        ActorX              = -4250,
        ActorZ              = 1000,
        ActorY              = -3000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 28,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_22E",          # 00, 0
        "Function_1_28C",          # 01, 1
        "Function_2_2EA",          # 02, 2
        "Function_3_7D4",          # 03, 3
        "Function_4_C24",          # 04, 4
        "Function_5_C35",          # 05, 5
        "Function_6_508F",         # 06, 6
        "Function_7_510A",         # 07, 7
        "Function_8_51B9",         # 08, 8
        "Function_9_52C1",         # 09, 9
        "Function_10_5590",        # 0A, 10
        "Function_11_57ED",        # 0B, 11
        "Function_12_581C",        # 0C, 12
        "Function_13_588E",        # 0D, 13
        "Function_14_58EA",        # 0E, 14
        "Function_15_592B",        # 0F, 15
        "Function_16_598C",        # 10, 16
        "Function_17_70D0",        # 11, 17
        "Function_18_710E",        # 12, 18
        "Function_19_82AD",        # 13, 19
        "Function_20_82D2",        # 14, 20
        "Function_21_8469",        # 15, 21
        "Function_22_8A2D",        # 16, 22
        "Function_23_8B1C",        # 17, 23
        "Function_24_8BFA",        # 18, 24
        "Function_25_8CB6",        # 19, 25
        "Function_26_8D83",        # 1A, 26
        "Function_27_8E99",        # 1B, 27
        "Function_28_8EE7",        # 1C, 28
    )


    def Function_0_22E(): pass

    label("Function_0_22E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26F")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_24E"),
        (104, "loc_255"),
        (100, "loc_25C"),
        (SWITCH_DEFAULT, "loc_26F"),
    )


    label("loc_24E")

    Event(0, 22)
    Jump("loc_26F")

    label("loc_255")

    Event(0, 23)
    Jump("loc_26F")

    label("loc_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26F")
    Event(0, 3)
    Jump("loc_26F")

    label("loc_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_28B")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)

    label("loc_28B")

    Return()

    # Function_0_22E end

    def Function_1_28C(): pass

    label("Function_1_28C")

    OP_16(0x2, 0xFA0, 0xFFFE13D0, 0xFFFDE4F0, 0x23006F)
    OP_1B(0x3, 0x0, 0x18)
    OP_1B(0x4, 0x0, 0x19)
    OP_1B(0x0, 0x0, 0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_2E9")
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_2E9")

    Return()

    # Function_1_28C end

    def Function_2_2EA(): pass

    label("Function_2_2EA")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp204_02.eff")
    SetChrPos(0x109, 7560, 0, 5540, 180)
    SetChrPos(0x102, 6540, 0, 6210, 180)
    SetChrPos(0xF0, 8230, 0, 6140, 180)
    SetChrPos(0xF1, 7310, 0, 7160, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(7010, 0, 6520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_3C0():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3C0)
    FadeToBright(2000, 0)
    OP_0D()
    PlayEffect(0x0, 0xFF, 0xFF, 7240, 0, 6380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(300)

    def lambda_41E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_41E)

    def lambda_430():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_430)

    def lambda_442():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_442)

    def lambda_454():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_454)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CA")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_531")

    label("loc_4CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F2")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_531")

    label("loc_4F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51A")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_531")

    label("loc_51A")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_531")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55E")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5C5")

    label("loc_55E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_586")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5C5")

    label("loc_586")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AE")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5C5")

    label("loc_5AE")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5C5")

    Sleep(1000)

    ChrTalk(    #0
        0x109,
        "#1079F#5P这是……\x02",
    )

    CloseMessageWindow()

    def lambda_5EE():
        OP_6D(-4000, 4600, 5220, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5EE)

    def lambda_606():
        OP_67(0, 7780, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_606)

    def lambda_61E():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_61E)

    def lambda_62E():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_62E)

    def lambda_63E():
        OP_6E(283, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_63E)
    Sleep(100)

    def lambda_653():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_653)
    Sleep(100)

    def lambda_666():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_666)
    Sleep(100)

    def lambda_679():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_679)
    Sleep(100)
    OP_8C(0xF0, 270, 400)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #1
        0x102,
        (
            "#1502F#1P照明什么时候……\x02\x03",

            "看来已经\x01",
            "变成了晚上呢。\x02",
        )
    )

    Jump("loc_6E3")

    label("loc_6E3")

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1063F#1P是啊……\x01",
            "和之前的王都一样呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(7010, 0, 6520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #3
        0x109,
        (
            "#1063F#6P也许附近会有什么变化……\x01",
            "我们仔细找一找吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        "#1502F#5P知道了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x290F)
    OP_28(0x34, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_2EA end

    def Function_3_7D4(): pass

    label("Function_3_7D4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -2009, 0, -39880, 0)
    SetChrPos(0x102, -3200, 0, -39980, 0)
    SetChrPos(0xF0, -2040, 0, -41870, 0)
    SetChrPos(0xF1, -3310, 0, -41390, 0)

    def lambda_82A():
        OP_8E(0xFE, 0xFFFFFA56, 0x0, 0xFFFF7EF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_82A)
    Sleep(150)

    def lambda_84A():
        OP_8E(0xFE, 0xFFFFF506, 0x0, 0xFFFF7FD6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_84A)
    Sleep(150)

    def lambda_86A():
        OP_8E(0xFE, 0xFFFFFA38, 0x0, 0xFFFF78A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_86A)
    Sleep(150)

    def lambda_88A():
        OP_8E(0xFE, 0xFFFFF420, 0x0, 0xFFFF7A36, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_88A)
    OP_6D(-3430, 0, -32600, 0)
    OP_67(0, 9080, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95F")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9C6")

    label("loc_95F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_987")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9C6")

    label("loc_987")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AF")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9C6")

    label("loc_9AF")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_9C6")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F3")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A5A")

    label("loc_9F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A5A")

    label("loc_A1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A43")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A5A")

    label("loc_A43")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A5A")

    Sleep(1000)

    ChrTalk(    #5
        0x109,
        "#1079F#6P真是……\x02",
    )

    CloseMessageWindow()

    def lambda_A83():
        OP_6D(-4000, 4600, 5220, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A83)

    def lambda_A9B():
        OP_67(0, 7780, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A9B)

    def lambda_AB3():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_AB3)

    def lambda_AC3():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AC3)

    def lambda_AD3():
        OP_6E(283, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_AD3)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #6
        0x102,
        (
            "#1502F#2P照明什么时候……\x02\x03",

            "看来已经\x01",
            "变成了晚上呢。\x02",
        )
    )

    Jump("loc_B33")

    label("loc_B33")

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1063F#2P啊啊……\x01",
            "和之前的王都一样呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(-3430, 0, -32600, 0)
    OP_67(0, 9080, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #8
        0x109,
        (
            "#1063F#6P也许附近会有什么变化……\x01",
            "我们仔细找一找吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        "#1502F#5P知道了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x290F)
    OP_28(0x34, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_3_7D4 end

    def Function_4_C24(): pass

    label("Function_4_C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_C2C")
    Return()

    label("loc_C2C")

    Call(0, 5)
    Call(0, 16)
    Return()

    # Function_4_C24 end

    def Function_5_C35(): pass

    label("Function_5_C35")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\mp251_00.eff")
    LoadEffect(0x1, "map\\mp251_01.eff")
    LoadEffect(0x2, "monster\\ms32000b.eff")
    LoadEffect(0x4, "monster\\msc1001.eff")
    LoadEffect(0x7, "monster\\ms32000.eff")
    OP_E0(238, 0x54, 0x2)
    OP_E0(238, 0x55, 0x5)
    OP_E0(239, 0x56, 0x2)
    OP_E0(239, 0x57, 0x5)
    OP_E0(240, 0x58, 0x2)
    OP_E0(240, 0x59, 0x5)
    OP_E0(241, 0x5A, 0x2)
    OP_E0(241, 0x5B, 0x5)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1E")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D85")

    label("loc_D1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D46")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D85")

    label("loc_D46")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6E")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_D85")

    label("loc_D6E")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_D85")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAD")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E14")

    label("loc_DAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD5")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E14")

    label("loc_DD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFD")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E14")

    label("loc_DFD")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E14")

    Sleep(1000)

    def lambda_E1F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E1F)

    def lambda_E2D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E2D)

    def lambda_E3B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_E3B)

    def lambda_E49():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_E49)
    Sleep(400)

    ChrTalk(    #10
        0x102,
        "#1502F#6P那是……！\x02",
    )

    CloseMessageWindow()

    def lambda_E7C():
        OP_6D(1760, 0, 46230, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E7C)

    def lambda_E94():
        OP_67(0, 5620, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E94)

    def lambda_EAC():
        OP_6B(4460, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_EAC)

    def lambda_EBC():
        OP_6C(327000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_EBC)

    def lambda_ECC():
        OP_6E(268, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ECC)
    WaitChrThread(0x109, 0x0)
    SetChrPos(0x109, 3340, 0, 32150, 0)
    SetChrPos(0x102, 1880, 0, 32180, 0)
    SetChrPos(0xF0, 3310, 0, 30620, 0)
    SetChrPos(0xF1, 1940, 0, 30550, 0)
    Sleep(500)

    ChrTalk(    #11
        0x109,
        (
            "#1063F#2P传送阵……\x01",
            "是通往下一个星层的入口吗！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FAC")

    ChrTalk(    #12
        0x10E,
        (
            "#178F#2P可是，白天的美景\x01",
            "竟然变成了这幅样子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1221")

    label("loc_FAC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FF9")

    ChrTalk(    #13
        0x10D,
        (
            "#270F#2P可是，白天的美景\x01",
            "竟然变成了这幅样子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1221")

    label("loc_FF9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1046")

    ChrTalk(    #14
        0x108,
        (
            "#072F#2P可是，白天的美景\x01",
            "竟然变成了这幅样子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1221")

    label("loc_1046")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1094")

    ChrTalk(    #15
        0x103,
        (
            "#1522F#2P可是，白天的美景\x01",
            "竟然变成了这幅样子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1221")

    label("loc_1094")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E6")

    ChrTalk(    #16
        0x10A,
        (
            "#1317F#2P可、可是，白天的美景\x01",
            "竟然变成了这幅样子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1221")

    label("loc_10E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1132")

    ChrTalk(    #17
        0x104,
        (
            "#1540F#2P可是，白天的美景\x01",
            "竟然变成了这幅样子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1221")

    label("loc_1132")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1180")

    ChrTalk(    #18
        0x105,
        (
            "#1163F#2P可是，白天的美景\x01",
            "竟然变成了这幅样子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1221")

    label("loc_1180")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D1")

    ChrTalk(    #19
        0x10B,
        (
            "#216F#2P可、可是，白天的美景\x01",
            "竟然变成了这幅样子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1221")

    label("loc_11D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1221")

    ChrTalk(    #20
        0x107,
        (
            "#065F#2P可、可是，那漂亮的景色\x01",
            "竟然变成了这幅样子……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1221")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_129D")

    ChrTalk(    #21
        0x106,
        (
            "#053F#2P哼……\x01",
            "终于剥下了伪装的外套吗。\x02\x03",

            "#051F虽然不知道为什么，\x01",
            "不过这不是很有意思吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1546")

    label("loc_129D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E0")

    ChrTalk(    #22
        0x107,
        (
            "#065F#2P那、那景色\x01",
            "果然也是假的啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1546")

    label("loc_12E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1325")

    ChrTalk(    #23
        0x10B,
        (
            "#212F#2P那景色果然\x01",
            "也是伪造出来的吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1546")

    label("loc_1325")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1384")

    ChrTalk(    #24
        0x105,
        (
            "#1162F#2P虽然不情愿，\x01",
            "不过也只好接受\x01",
            "这里是伪造的场所的事实了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1546")

    label("loc_1384")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13E5")

    ChrTalk(    #25
        0x104,
        (
            "#1545F#2P呵，虽然不情愿，\x01",
            "不过也只好接受\x01",
            "这里是伪造的场所的事实了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1546")

    label("loc_13E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1428")

    ChrTalk(    #26
        0x10A,
        (
            "#812F#2P那副光景\x01",
            "果然也是伪造的吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1546")

    label("loc_1428")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1489")

    ChrTalk(    #27
        0x103,
        (
            "#1525F#2P唉，虽然不情愿，\x01",
            "不过也只好接受\x01",
            "这里是伪造的场所的事实了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1546")

    label("loc_1489")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14E9")

    ChrTalk(    #28
        0x108,
        (
            "#074F#2P唔，虽然不情愿，\x01",
            "不过也只好接受\x01",
            "这里是伪造的场所的事实了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1546")

    label("loc_14E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1546")

    ChrTalk(    #29
        0x10D,
        (
            "#272F#2P哼，虽然不情愿，\x01",
            "不过也只好接受\x01",
            "这里是伪造的场所的事实了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1546")

    Sleep(300)
    Fade(500)
    SetChrPos(0x109, 4100, 0, 22650, 0)
    SetChrPos(0x102, 2630, 0, 22460, 0)
    SetChrPos(0xF0, 4620, 0, 21080, 0)
    SetChrPos(0xF1, 2300, 0, 20980, 0)
    OP_6D(2480, 0, 23060, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(253, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #30
        0x102,
        (
            "#1502F#5P那么……\x01",
            "我们要继续前进吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1067F#6P是啊……\x01",
            "至少先去确认一下情况──\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(300)
    OP_22(0x233, 0x0, 0x64)
    Fade(500)
    PlayEffect(0x0, 0x0, 0xFF, 3400, 200, 30120, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16ED")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1754")

    label("loc_16ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1715")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1754")

    label("loc_1715")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_173D")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1754")

    label("loc_173D")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1754")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1781")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17E8")

    label("loc_1781")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A9")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17E8")

    label("loc_17A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D1")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17E8")

    label("loc_17D1")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_17E8")

    Sleep(1000)

    def lambda_17F3():
        OP_6D(3420, 0, 27120, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_17F3)

    def lambda_180B():
        OP_67(0, 7290, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_180B)

    def lambda_1823():
        OP_6B(3390, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1823)

    def lambda_1833():
        OP_6E(270, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1833)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 20)
    SetChrSubChip(0xEE, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 22)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 24)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 26)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #32
        0x102,
        "#1502F#5P呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x109,
        "#1069F#6P来了吗……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0x9A)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0x85, 0x1, 0x64)

    def lambda_18FB():

        label("loc_18FB")

        OP_7C(0x50, 0x50, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_18FB")

    QueueWorkItem2(0x102, 3, lambda_18FB)
    PlayEffect(0x1, 0x1, 0xFF, 3400, 200, 30120, 0, 0, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x11, 3400, -9000, 30120, 180)
    OP_A1(0x11, 0x1)
    OP_72(0x401, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x28)

    def lambda_1979():
        OP_8F(0xFE, 0xD48, 0x1F4, 0x75A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1979)
    Fade(1000)
    OP_6D(3400, 1000, 27000, 0)
    OP_67(0, 3000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(330, 0)

    def lambda_19D6():
        OP_6D(3400, 4000, 30420, 9500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_19D6)

    def lambda_19EE():
        OP_67(0, 1020, -10000, 9500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_19EE)

    def lambda_1A06():
        OP_6B(2500, 9500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1A06)

    def lambda_1A16():
        OP_6E(320, 9500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A16)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x11, 0x0)
    OP_44(0x102, 0x3)
    OP_23(0x85)
    PlayEffect(0x7, 0x7, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    WaitChrThread(0x109, 0x0)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0x99, 0x0, 0x64)

    def lambda_1A94():
        OP_6D(3400, 2300, 30420, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A94)

    def lambda_1AAC():
        OP_67(0, 1020, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1AAC)

    def lambda_1AC4():
        OP_6B(3500, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1AC4)

    def lambda_1AD4():
        OP_6E(351, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1AD4)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #34
        0x102,
        "#1504F#6P这、这是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x109,
        (
            "#1069F#6P记载于圣典中的\x01",
            "七十七恶魔之一……\x02\x03",

            "炼狱大门看守的另一柱——\x01",
            "会使用恐怖禁咒的魔导师！\x02\x03",

            "『深渊』阿斯塔尔特吗！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    LoadEffect(0x0, "map\\mp307_00.eff")
    LoadEffect(0x1, "map\\mp262_00.eff")

    def lambda_1BCD():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1BCD)

    def lambda_1BDD():
        OP_6E(400, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1BDD)
    OP_D8(0x1, 0x3E8)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 141)
    OP_70(0x1, 0x96)
    OP_73(0x1)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 151)
    OP_70(0x1, 0xA0)
    PlayEffect(0x4, 0x3, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x137, 0x1, 0x50)
    OP_22(0x32E, 0x0, 0x64)
    Sleep(2000)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    PlayEffect(0x0, 0x0, 0xFF, 3400, 2800, 24700, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Fade(1000)
    OP_82(0x3, 0x2)
    OP_6D(-1830, 350, 31400, 0)
    OP_67(0, 2610, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(400, 0)
    SetChrPos(0x109, 4970, 0, 22650, 0)
    SetChrPos(0x102, 3100, 0, 22460, 0)
    SetChrPos(0xF0, 5420, 0, 20800, 0)
    SetChrPos(0xF1, 3050, 0, 20800, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)

    def lambda_1D39():
        OP_6D(-1830, 350, 30400, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1D39)

    def lambda_1D51():
        OP_67(0, 2120, -10000, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D51)

    def lambda_1D69():
        OP_6B(3940, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1D69)

    def lambda_1D79():
        OP_6E(337, 500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1D79)
    PlayEffect(0x1, 0x1, 0xFF, 4019, 0, 21890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1B9, 0x0, 0x64)
    OP_22(0x3DC, 0x1, 0x50)
    OP_0D()

    def lambda_1DC9():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1DC9)
    Sleep(10)

    def lambda_1DE8():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1DE8)
    Sleep(10)

    def lambda_1E07():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1E07)
    Sleep(10)

    def lambda_1E26():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1E26)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E9A")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F01")

    label("loc_1E9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EC2")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F01")

    label("loc_1EC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EEA")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F01")

    label("loc_1EEA")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1F01")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F2E")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F95")

    label("loc_1F2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F56")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F95")

    label("loc_1F56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F7E")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1F95")

    label("loc_1F7E")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1F95")

    Sleep(1000)
    OP_82(0x0, 0x2)
    OP_23(0x32E)
    OP_23(0x137)
    OP_D8(0x1, 0x5DC)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x28)
    Fade(250)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 21)
    SetChrSubChip(0xEE, 3)
    Sleep(50)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 23)
    SetChrSubChip(0xEF, 3)
    Sleep(80)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 25)
    SetChrSubChip(0xF0, 3)
    Sleep(50)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 27)
    SetChrSubChip(0xF1, 3)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2034")

    ChrTalk(    #36
        0x106,
        "#052F#6P哦！？\x02",
    )

    CloseMessageWindow()

    label("loc_2034")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_205F")

    ChrTalk(    #37
        0x107,
        "#065F#6P哇哇！？\x02",
    )

    CloseMessageWindow()

    label("loc_205F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_208E")

    ChrTalk(    #38
        0x10B,
        "#216F#6P怎、怎么！？\x02",
    )

    CloseMessageWindow()

    label("loc_208E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20BA")

    ChrTalk(    #39
        0x104,
        "#1543F#6P噢噢！？\x02",
    )

    CloseMessageWindow()

    label("loc_20BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20EA")

    ChrTalk(    #40
        0x105,
        "#1381F#6P啊啊……！？\x02",
    )

    CloseMessageWindow()

    label("loc_20EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2118")

    ChrTalk(    #41
        0x10A,
        "#1312F#6P呀……！？\x02",
    )

    CloseMessageWindow()

    label("loc_2118")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2146")

    ChrTalk(    #42
        0x103,
        "#1533F#6P呜……！？\x02",
    )

    CloseMessageWindow()

    label("loc_2146")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2173")

    ChrTalk(    #43
        0x10E,
        "#177F#6P什……！？\x02",
    )

    CloseMessageWindow()

    label("loc_2173")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21A0")

    ChrTalk(    #44
        0x10D,
        "#271F#6P呜……！？\x02",
    )

    CloseMessageWindow()

    label("loc_21A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21CF")

    ChrTalk(    #45
        0x108,
        "#077F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    label("loc_21CF")


    ChrTalk(    #46
        0x102,
        (
            "#1507F#6P这、这是……\x01",
            "怀斯曼的『魔眼』！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x109,
        (
            "#1070F#6P大概这是它的原型——\x01",
            "束缚空间本身的禁咒！\x02\x03",

            "混帐……\x01",
            "难道一点也动不了吗……！\x02",
        )
    )

    Jump("loc_227A")

    label("loc_227A")

    CloseMessageWindow()
    Sleep(300)
    LoadEffect(0x0, "monster\\ms30901b.eff")
    LoadEffect(0x2, "craft\\cr04150.eff")
    LoadEffect(0x3, "craft\\cr04151a.eff")
    LoadEffect(0x4, "craft\\cr04151b.eff")
    LoadEffect(0x5, "craft\\cr04151c.eff")
    LoadEffect(0x6, "craft\\cr04151d.eff")
    Fade(500)
    OP_6D(4000, 0, 32180, 0)
    OP_67(0, 2690, -10000, 0)
    OP_6B(3010, 0)
    OP_6C(0, 0)
    OP_6E(411, 0)
    SetChrPos(0x109, 4500, 0, 22650, 0)
    SetChrPos(0x102, 3200, 0, 22460, 0)
    SetChrPos(0xF0, 5220, 0, 20800, 0)
    SetChrPos(0xF1, 2750, 0, 20800, 0)
    SetChrPos(0x11, 3600, 0, 30120, 180)

    def lambda_239C():
        OP_6D(4000, 2200, 33000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_239C)

    def lambda_23B4():
        OP_67(0, 1470, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_23B4)

    def lambda_23CC():
        OP_6B(4660, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_23CC)

    def lambda_23DC():
        OP_6E(290, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_23DC)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_73(0x1)
    OP_D8(0x1, 0x3E8)

    def lambda_23F9():
        OP_8C(0xFE, 200, 200)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_23F9)
    OP_B0(0x1, 0xF)
    OP_22(0xED, 0x0, 0x64)
    OP_6F(0x1, 81)
    OP_70(0x1, 0x5A)
    OP_73(0x1)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_D8(0x1, 0x3E8)
    OP_6F(0x1, 331)
    OP_70(0x1, 0x171)
    Sleep(500)
    OP_22(0x2ED, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, 500, 8000, 29290, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #48
        0x102,
        (
            "#1506F#5P呜……\x01",
            "这样下去就会……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x109,
        (
            "#1067F#5P………哼………………\x01",
            "（这样的话就只好把那个……）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 4100, 0, 11400, 0)
    SetChrChipByIndex(0x13, 12)
    SetChrSubChip(0x13, 14)
    OP_51(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0xC5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x4F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x7D0)
    Sleep(1000)

    NpcTalk(    #50
        0x13,
        "女孩的声音",
        (
            "#5P──请退下。\x01",
            "背离女神的灾祸之兽。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_267E():
        OP_6D(4000, 2000, 35000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_267E)

    def lambda_2696():
        OP_67(0, 2890, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2696)

    def lambda_26AE():
        OP_6B(4000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_26AE)

    def lambda_26BE():
        OP_6E(300, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_26BE)
    OP_22(0x19A, 0x0, 0x64)
    OP_22(0xC9, 0x0, 0x64)
    PlayEffect(0x2, 0x3, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x3, 0xFF, 0xFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x4, 0x4, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x5, 0xFF, 0x11, -1500, 1500, 1000, 0, 0, 0, 1000, 1000, 1000, 0x11, 500, 2500, 0, 0)
    OP_B0(0x1, 0x1E)
    Sleep(200)

    def lambda_27C4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_27C4)

    def lambda_27D2():
        OP_7C(0x1F4, 0x1F4, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_27D2)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 121)
    OP_70(0x1, 0x8C)
    OP_82(0x2, 0x0)
    PlayEffect(0x5, 0xFF, 0x11, 2000, 2000, 500, 0, 0, 0, 1000, 1000, 1000, 0x11, 3000, 4000, 1000, 0)
    Sleep(200)

    def lambda_283B():
        OP_7C(0x1F4, 0x1F4, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_283B)
    OP_6F(0x1, 121)
    OP_70(0x1, 0x8C)
    PlayEffect(0x5, 0xFF, 0x11, -1000, 2500, 0, 0, 0, 0, 1000, 1000, 1000, 0x11, 500, 4000, 1000, 0)
    Sleep(200)

    def lambda_289B():
        OP_7C(0x1F4, 0x1F4, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_289B)
    OP_6F(0x1, 121)
    OP_70(0x1, 0x8C)
    PlayEffect(0x5, 0xFF, 0x11, 1500, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0x11, 2000, 2500, 1500, 0)
    Sleep(200)

    def lambda_28FB():
        OP_7C(0x1F4, 0x1F4, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_28FB)
    OP_6F(0x1, 121)
    OP_70(0x1, 0x8C)
    OP_82(0x4, 0x0)
    Sleep(200)
    OP_6F(0x1, 121)
    OP_70(0x1, 0x8C)
    Sleep(200)
    OP_6F(0x1, 121)
    OP_70(0x1, 0x8C)
    OP_73(0x1)
    OP_D8(0x1, 0x3E8)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 1)
    OP_70(0x1, 0x28)
    WaitChrThread(0x109, 0x0)

    def lambda_296A():
        OP_6D(4000, 0, 25150, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_296A)

    def lambda_2982():
        OP_67(0, 2690, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2982)

    def lambda_299A():
        OP_6B(3520, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_299A)

    def lambda_29AA():
        OP_6E(420, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29AA)
    WaitChrThread(0x109, 0x0)
    PlayEffect(0x6, 0xFF, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_23(0xC9)
    OP_82(0x3, 0x0)
    Fade(500)
    OP_1D(0x99)
    OP_71(0x401, 0x0)
    ExitThread()
    OP_51(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 4)
    SetChrSubChip(0x13, 0)
    OP_6D(3990, 600, 15800, 0)
    OP_67(0, 4590, -10000, 0)
    OP_6B(3410, 0)
    OP_6C(180000, 0)
    OP_6E(304, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #51
        0x102,
        "#1504F#5P莉丝小姐！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x13,
        (
            "#1447F#5P太好了……\x01",
            "看来赶上了呢。\x02\x03",

            "#1448F这里就交给我吧……\x01",
            "会很快做个了断的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    LoadEffect(0x2, "craft\\cr04150a.eff")
    LoadEffect(0x3, "craft\\cr04150b.eff")
    LoadEffect(0x4, "monster\\msc0641.eff")

    def lambda_2C63():
        OP_6D(8750, 4050, 23090, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2C63)

    def lambda_2C7B():
        OP_67(0, 4260, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C7B)

    def lambda_2C93():
        OP_6B(2430, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2C93)

    def lambda_2CA3():
        OP_6C(120000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2CA3)

    def lambda_2CB3():
        OP_6E(260, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2CB3)

    def lambda_2CC3():

        label("loc_2CC3")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_2CC3")

    QueueWorkItem2(0x11, 3, lambda_2CC3)
    OP_7D(0x0, 0x13, 0x32, 0x1F4)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 5)

    def lambda_2CE6():
        OP_8E(0xFE, 0x1130, 0xA, 0x3E4E, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2CE6)
    WaitChrThread(0x13, 0x1)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_2D0B():
        OP_96(0xFE, 0x21FC, 0xDAC, 0x59CE, 0x1770, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2D0B)

    def lambda_2D29():
        OP_8C(0xFE, 315, 0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2D29)
    OP_51(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0xC5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x4F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 11)
    SetChrSubChip(0x13, 4)
    PlayEffect(0x2, 0x3, 0x13, 0, 500, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_82(0x3, 0x0)
    PlayEffect(0x3, 0x4, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    PlayEffect(0x4, 0xFF, 0x11, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F9, 0x0, 0x64)
    OP_22(0x2CE, 0x0, 0x64)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Fade(500)
    OP_72(0x401, 0x0)
    ExitThread()
    SetChrSubChip(0x13, 4)
    PlayEffect(0x3, 0x4, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    PlayEffect(0x4, 0xFF, 0x11, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F9, 0x0, 0x64)
    OP_22(0x2CE, 0x0, 0x64)

    def lambda_2FC6():
        OP_7C(0x5DC, 0x5DC, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2FC6)
    OP_43(0x11, 0x0, 0x0, 0xF)
    OP_6D(4100, 3100, 29500, 0)
    OP_67(0, 3840, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(324000, 0)
    OP_6E(292, 0)

    def lambda_3022():
        OP_96(0xFE, 0x1F90, 0x0, 0x62E8, 0x12C, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3022)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(600)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    WaitChrThread(0x13, 0x1)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(40)
    Fade(250)
    OP_51(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 4)
    SetChrSubChip(0x13, 0)
    OP_0D()
    Sleep(300)

    def lambda_317A():
        OP_6D(2920, 300, 33750, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_317A)

    def lambda_3192():
        OP_67(0, 2350, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3192)

    def lambda_31AA():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_31AA)

    def lambda_31BA():
        OP_6C(331000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_31BA)

    def lambda_31CA():
        OP_6E(420, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_31CA)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "magic\\mg052_0.eff")
    LoadEffect(0x5, "Craft\\cr161_00.eff")
    Fade(250)
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)

    def lambda_323C():

        label("loc_323C")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_323C")

    QueueWorkItem2(0x13, 3, lambda_323C)
    OP_0D()
    Sleep(300)
    PlayEffect(0x0, 0x2, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x109, 0x0)

    def lambda_328F():
        OP_6D(-380, 800, 37550, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_328F)

    def lambda_32A7():
        OP_67(0, 2080, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_32A7)

    def lambda_32BF():
        OP_6B(3200, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_32BF)

    def lambda_32CF():
        OP_6C(327000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_32CF)

    def lambda_32DF():
        OP_6E(451, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_32DF)
    OP_44(0x13, 0x3)
    SetChrChipByIndex(0x13, 10)
    SetChrSubChip(0x13, 1)
    OP_82(0x2, 0x2)
    PlayEffect(0x2, 0x6, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x3, 0x3, 0x11, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0x11, 0, 0, 0, 0)
    Sleep(2500)
    OP_43(0x102, 0x0, 0x0, 0xB)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x14)
    OP_6F(0x1, 121)
    OP_70(0x1, 0x8C)
    OP_83(0x3, 0x2)
    OP_44(0x102, 0x0)
    OP_D8(0x1, 0x3E8)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x28)
    WaitChrThread(0x109, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x13, 4)
    SetChrSubChip(0x13, 0)
    OP_0D()
    OP_43(0x13, 0x0, 0x0, 0xA)
    Sleep(300)
    Fade(250)
    OP_6D(-1290, 0, 30660, 0)
    OP_67(0, 5210, -10000, 0)
    OP_6B(2100, 0)
    OP_6C(262000, 0)
    OP_6E(410, 0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x109, 0x0)

    def lambda_3428():
        OP_6D(680, 1250, 33380, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3428)

    def lambda_3440():
        OP_67(0, 5210, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3440)

    def lambda_3458():
        OP_6B(2500, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3458)

    def lambda_3468():
        OP_6C(309000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3468)

    def lambda_3478():
        OP_6E(410, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3478)

    def lambda_3488():
        OP_8C(0xFE, 200, 200)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_3488)
    OP_D8(0x1, 0x3E8)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 41)
    OP_70(0x1, 0x46)
    Sleep(300)
    OP_22(0xED, 0x0, 0x64)
    OP_43(0x13, 0x0, 0x0, 0x9)

    def lambda_34C3():
        OP_6D(700, 1650, 31450, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_34C3)

    def lambda_34DB():
        OP_67(0, 6030, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_34DB)

    def lambda_34F3():
        OP_6B(2520, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_34F3)

    def lambda_3503():
        OP_6C(333000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3503)

    def lambda_3513():
        OP_6E(405, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3513)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x109, 0x0)
    LoadEffect(0x0, "magic\\mg011_0.eff")
    LoadEffect(0x2, "monster\\msc1001.eff")
    LoadEffect(0x3, "craft\\cr04150.eff")
    LoadEffect(0x4, "craft\\cr04150a.eff")
    LoadEffect(0x5, "craft\\cr04150b.eff")
    LoadEffect(0x6, "monster\\msc0641.eff")

    def lambda_35AB():
        OP_6D(-270, 810, 27940, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_35AB)

    def lambda_35C3():
        OP_67(0, 6810, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_35C3)

    def lambda_35DB():
        OP_6B(2720, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_35DB)

    def lambda_35EB():
        OP_6C(344000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_35EB)

    def lambda_35FB():
        OP_6E(423, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_35FB)
    OP_D8(0x1, 0x3E8)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 141)
    OP_70(0x1, 0x96)
    OP_73(0x1)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 151)
    OP_70(0x1, 0xA0)
    PlayEffect(0x2, 0x3, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x32E, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x13, 0x0, 0x0, 0x8)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -740, 0, 26260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    PlayEffect(0x0, 0xFF, 0xFF, -2980, 0, 24530, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    PlayEffect(0x0, 0xFF, 0xFF, -1540, 0, 21440, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_82(0x3, 0x0)
    OP_23(0x32E)
    WaitChrThread(0x13, 0x0)
    OP_22(0x19A, 0x0, 0x64)
    OP_22(0xC9, 0x0, 0x64)
    PlayEffect(0x3, 0x3, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x109, 0x0)
    Fade(500)

    def lambda_3787():
        OP_6D(300, 850, 28290, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3787)

    def lambda_379F():
        OP_67(0, 6210, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_379F)

    def lambda_37B7():
        OP_6B(2080, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_37B7)

    def lambda_37C7():
        OP_6C(338000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_37C7)

    def lambda_37D7():
        OP_6E(376, 1000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_37D7)
    WaitChrThread(0x109, 0x0)
    OP_51(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0xC5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x4F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 11)
    SetChrSubChip(0x13, 4)
    PlayEffect(0x4, 0x4, 0x13, 0, 500, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_23(0xC9)
    PlayEffect(0x5, 0x0, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    Fade(500)
    OP_6D(1550, 1000, 37590, 0)
    OP_67(0, 3660, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(350000, 0)
    OP_6E(422, 0)

    def lambda_398A():
        OP_6B(2700, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_398A)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    PlayEffect(0x6, 0xFF, 0x11, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_39D5():
        OP_7C(0x5DC, 0x5DC, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_39D5)
    OP_43(0x11, 0x0, 0x0, 0xD)
    OP_22(0x1F9, 0x0, 0x64)
    OP_22(0x2CE, 0x0, 0x64)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(600)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Fade(250)
    OP_51(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 4)
    SetChrSubChip(0x13, 0)
    OP_0D()
    Sleep(300)
    Fade(500)
    OP_6D(2840, 0, 22280, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(173000, 0)
    OP_6E(404, 0)
    OP_71(0x401, 0x0)
    ExitThread()
    OP_82(0x7, 0x0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BA0")

    ChrTalk(    #53
        0x107,
        "#560F#5P厉、厉害……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C33")

    label("loc_3BA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BCF")

    ChrTalk(    #54
        0x105,
        "#1382F#5P厉害……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C33")

    label("loc_3BCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C02")

    ChrTalk(    #55
        0x10A,
        "#1310F#5P厉、厉害……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C33")

    label("loc_3C02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C33")

    ChrTalk(    #56
        0x10B,
        "#415F#5P厉、厉害啊……\x02",
    )

    CloseMessageWindow()

    label("loc_3C33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C6B")

    ChrTalk(    #57
        0x106,
        "#051F#5P这不是很厉害吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CFD")

    label("loc_3C6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C9C")

    ChrTalk(    #58
        0x103,
        "#1527F#5P真强啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CFD")

    label("loc_3C9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CCE")

    ChrTalk(    #59
        0x108,
        "#070F#5P干得不错……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CFD")

    label("loc_3CCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CFD")

    ChrTalk(    #60
        0x10D,
        "#275F#5P干得不错……\x02",
    )

    CloseMessageWindow()

    label("loc_3CFD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D35")

    ChrTalk(    #61
        0x10E,
        "#171F#5P不愧是星杯骑士……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DAB")

    label("loc_3D35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D75")

    ChrTalk(    #62
        0x104,
        (
            "#1541F#5P呼……\x01",
            "不愧是星杯骑士……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DAB")

    label("loc_3D75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DAB")

    ChrTalk(    #63
        0x102,
        "#1500F#5P不愧是星杯骑士……\x02",
    )

    CloseMessageWindow()

    label("loc_3DAB")


    ChrTalk(    #64
        0x109,
        (
            "#1069F#5P莉丝，别乱来！\x02\x03",

            "你应该知道那不是\x01",
            "一个人就能对付的敌人吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x13,
        (
            "#1441F#11P就算如此，我……\x01",
            "我也是一名星杯的随从骑士……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0x13, 7)
    SetChrSubChip(0x13, 0)
    OP_8C(0x13, 45, 0)

    def lambda_3E6A():
        OP_96(0xFE, 0xFFFFF600, 0x0, 0x60C2, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_3E6A)
    Fade(500)
    OP_6D(2090, 750, 26140, 0)
    OP_67(0, 5570, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(87000, 0)
    OP_6E(357, 0)
    SetChrPos(0x11, 5730, 500, 32250, 240)
    OP_72(0x401, 0x0)
    ExitThread()
    PlayEffect(0x7, 0x7, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x13, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0x13, 4)
    SetChrSubChip(0x13, 0)
    Sleep(300)

    def lambda_3F2F():
        OP_6D(2090, 750, 26140, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3F2F)

    def lambda_3F47():
        OP_67(0, 5570, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3F47)

    def lambda_3F5F():
        OP_6B(2720, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3F5F)

    def lambda_3F6F():
        OP_6E(357, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3F6F)
    Sleep(300)

    ChrTalk(    #66
        0x13,
        (
            "#1445F#6P虽然我想说的话\x01",
            "……有许多许多……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "magic\\mg055_0.eff")
    LoadEffect(0x4, "battle\\damage0.eff")
    LoadEffect(0x5, "monster\\ms32003a.eff")
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)

    def lambda_4040():

        label("loc_4040")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_4040")

    QueueWorkItem2(0x13, 3, lambda_4040)
    OP_0D()
    Sleep(300)
    PlayEffect(0x0, 0x2, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #67
        0x13,
        (
            "#1449F#6P可是我……\x01",
            "我要保护凯文……！\x02\x03",

            "就像保护了我的……\x01",
            "凯文和姐姐那样……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x109,
        "#1079F#5P#3S！！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0x0)
    OP_44(0x13, 0x3)
    SetChrChipByIndex(0x13, 10)
    SetChrSubChip(0x13, 1)
    OP_82(0x2, 0x2)
    PlayEffect(0x2, 0x6, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    def lambda_415E():
        OP_67(0, 7430, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_415E)

    def lambda_4176():
        OP_6B(2820, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4176)

    def lambda_4186():
        OP_6C(63000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4186)

    def lambda_4196():
        OP_6E(319, 1500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4196)
    PlayEffect(0x3, 0x4, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x11, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_41E0():
        OP_6D(6540, 750, 32090, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_41E0)
    PlayEffect(0x5, 0x5, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(800)
    OP_20(0x3E8)
    OP_22(0x59, 0x0, 0x64)
    Fade(1000)
    OP_71(0x401, 0x0)
    ExitThread()
    OP_82(0x7, 0x0)
    OP_0D()
    Fade(500)
    OP_6D(-4630, 1050, 22620, 0)
    OP_67(0, 6070, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(185000, 0)
    OP_6E(404, 0)
    SetChrChipByIndex(0x13, 10)
    SetChrSubChip(0x13, 1)
    SetChrPos(0x13, -1200, 0, 27310, 45)
    OP_0D()
    PlayEffect(0x5, 0x5, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x59, 0x0, 0x64)
    Fade(1000)
    OP_72(0x401, 0x0)
    ExitThread()
    SetChrPos(0x11, -4800, 500, 23360, 42)
    PlayEffect(0x7, 0x7, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_82(0x5, 0x2)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #69 op#A op#5
        0x13,
        "#1802F#5P#10A啊……\x05\x02",
    )

    CloseMessageWindow()

    def lambda_437A():
        OP_8C(0xFE, 225, 600)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_437A)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x13, 4)
    SetChrSubChip(0x13, 0)
    OP_D8(0x1, 0x3E8)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 81)
    OP_70(0x1, 0x78)
    Sleep(300)
    OP_22(0xED, 0x0, 0x64)
    Sleep(500)

    def lambda_43BE():
        OP_6D(7450, 0, 29880, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_43BE)
    WaitChrThread(0x13, 0x3)
    OP_43(0x13, 0x0, 0x0, 0x7)

    def lambda_43E2():
        OP_7C(0xC8, 0xC8, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_43E2)
    PlayEffect(0x4, 0xFF, 0x13, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x109, 0x0)
    OP_73(0x1)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 1)
    OP_70(0x1, 0x28)
    SetChrPos(0x11, -4790, 500, 23500, 42)

    ChrTalk(    #70
        0x109,
        "#1069F#6P#3S莉、莉丝！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_4495():
        OP_6D(3970, 1050, 27530, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4495)

    def lambda_44AD():
        OP_67(0, 4660, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_44AD)

    def lambda_44C5():
        OP_6B(2950, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_44C5)

    def lambda_44D5():
        OP_6C(233000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_44D5)

    def lambda_44E5():
        OP_6E(422, 2500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44E5)
    Sleep(1000)
    WaitChrThread(0x109, 0x0)
    PlayEffect(0x5, 0x5, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x59, 0x0, 0x64)
    Fade(1000)
    OP_71(0x401, 0x0)
    ExitThread()
    OP_82(0x7, 0x0)
    OP_0D()
    PlayEffect(0x5, 0x5, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x59, 0x0, 0x64)
    Fade(1000)
    OP_72(0x401, 0x0)
    ExitThread()
    SetChrPos(0x11, 4100, 500, 31000, 58)
    PlayEffect(0x7, 0x7, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_82(0x5, 0x2)

    def lambda_45E1():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_45E1)
    OP_99(0x13, 0x0, 0x2, 0x1F4)
    Sleep(500)

    ChrTalk(    #71
        0x13,
        "#1804F#5P#50W呜………啊………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    WaitChrThread(0x109, 0x0)
    LoadEffect(0x0, "map\\mp261_00.eff")
    LoadEffect(0x3, "map\\mp284_00.eff")
    LoadEffect(0x4, "map\\mp262_01.eff")
    LoadEffect(0x5, "monster\\ms30901b.eff")
    LoadEffect(0x6, "map\\mp283_00.eff")

    def lambda_46A0():
        OP_6D(2630, 0, 26040, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_46A0)

    def lambda_46B8():
        OP_67(0, 5600, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_46B8)

    def lambda_46D0():
        OP_6B(3260, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_46D0)

    def lambda_46E0():
        OP_6E(422, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_46E0)
    OP_44(0x11, 0x3)

    def lambda_46F4():
        OP_8C(0xFE, 80, 200)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_46F4)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_D8(0x1, 0x3E8)
    OP_B0(0x1, 0xF)
    OP_22(0xED, 0x0, 0x64)
    OP_6F(0x1, 81)
    OP_70(0x1, 0x5A)
    OP_73(0x1)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_D8(0x1, 0x3E8)
    OP_6F(0x1, 331)
    OP_70(0x1, 0x171)
    Sleep(500)
    OP_22(0x2ED, 0x0, 0x64)
    PlayEffect(0x5, 0x2, 0xFF, 2000, 8000, 26000, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #72
        0x102,
        "#1506F#5P不行……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47DB")

    ChrTalk(    #73
        0x105,
        "#1163F#5P莉丝小姐……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4910")

    label("loc_47DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_480F")

    ChrTalk(    #74
        0x107,
        "#065F#5P莉丝姐姐……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4910")

    label("loc_480F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4844")

    ChrTalk(    #75
        0x10A,
        "#1317F#5P莉丝小姐……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4910")

    label("loc_4844")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4877")

    ChrTalk(    #76
        0x104,
        "#1550F#5P莉丝君……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4910")

    label("loc_4877")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48AB")

    ChrTalk(    #77
        0x10E,
        "#177F#5P莉丝小姐……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4910")

    label("loc_48AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48DF")

    ChrTalk(    #78
        0x10B,
        "#214F#5P修女小姐……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4910")

    label("loc_48DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4910")

    ChrTalk(    #79
        0x108,
        "#076F#5P修女小姐……！\x02",
    )

    CloseMessageWindow()

    label("loc_4910")


    ChrTalk(    #80
        0x109,
        "#1065F#5P哼…………\x02",
    )

    CloseMessageWindow()
    OP_1D(0xB5)
    Sleep(500)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6D(3510, 0, 22340, 0)
    OP_67(0, 7490, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(237000, 0)
    OP_6E(325, 0)
    SetChrPos(0x13, 8560, 0, 32090, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_49A3():

        label("loc_49A3")

        OP_7C(0xC8, 0xC8, 0xBB8, 0x64)
        OP_48()
        Jump("loc_49A3")

    QueueWorkItem2(0x102, 3, lambda_49A3)

    def lambda_49BE():
        OP_6B(2200, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_49BE)
    OP_22(0x34F, 0x0, 0x64)
    OP_43(0x109, 0x0, 0x0, 0x6)
    Sleep(1000)

    ChrTalk(    #81 op#A op#5
        0x109,
        "#1069F#4S#5P#20A#60W噢噢噢噢噢噢噢噢噢噢噢！！\x05\x02",
    )

    CloseMessageWindow()
    OP_0D()
    WaitChrThread(0x109, 0x0)
    OP_44(0x102, 0x3)
    OP_23(0x85)
    Sleep(300)
    SetChrSubChip(0x109, 0)
    Sleep(500)
    OP_22(0x1BF, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0x109, 0, 1300, -700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x109, 17)
    SetChrSubChip(0x109, 0)
    OP_22(0x353, 0x0, 0x64)
    OP_22(0x34F, 0x0, 0x64)
    PlayEffect(0x3, 0x6, 0x109, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x85, 0x1, 0x64)

    def lambda_4AC8():

        label("loc_4AC8")

        OP_7C(0xC8, 0xC8, 0xBB8, 0x64)
        OP_48()
        Jump("loc_4AC8")

    QueueWorkItem2(0x102, 3, lambda_4AC8)
    Sleep(300)
    OP_22(0x139, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1B3, 0x0, 0x64)
    OP_82(0x1, 0x2)
    PlayEffect(0x4, 0x5, 0xFF, 4019, 0, 21890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0x3DC)

    def lambda_4B32():
        OP_7C(0x5DC, 0x5DC, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4B32)
    Fade(500)
    OP_6D(1260, 0, 25850, 0)
    OP_67(0, 5250, -10000, 0)
    OP_6B(2520, 0)
    OP_6C(314000, 0)
    OP_6E(395, 0)

    def lambda_4B8C():
        OP_6D(1260, 0, 28000, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4B8C)

    def lambda_4BA4():
        OP_6B(3200, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4BA4)

    def lambda_4BB4():
        OP_6E(410, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4BB4)
    OP_43(0x11, 0x0, 0x0, 0xC)
    WaitChrThread(0x11, 0x0)
    OP_82(0x6, 0x2)
    OP_44(0x102, 0x3)
    OP_23(0x85)

    def lambda_4BDA():
        OP_8C(0xFE, 180, 100)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4BDA)
    Sleep(1000)

    ChrTalk(    #82
        0x102,
        "#1504F#5P！？\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #83
        0x13,
        "#1802F#6P凯……凯文……？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    LoadEffect(0x1, "map\\mp260_00.eff")
    LoadEffect(0x2, "map\\mp260_01.eff")
    LoadEffect(0x3, "map\\mp261_01.eff")
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    OP_6D(4520, 0, 24500, 0)
    OP_67(0, 4510, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(0, 0)
    OP_6E(335, 0)
    OP_22(0x334, 0x0, 0x64)

    def lambda_4CC0():
        OP_6B(2290, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4CC0)
    WaitChrThread(0x109, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #84
        (
            "\x07\x05凯文学会了新的Ｓ战技\x01",
            "\x07\x02『魔枪洛亚』\x07\x05。\x02",
        )
    )

    Jump("loc_4D16")

    label("loc_4D16")

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x21E, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #85
        "\x07\x05将『魔枪洛亚』设定为Ｓ爆发技。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_59()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(2850, 0, 21250, 0)
    OP_67(0, 4310, -10000, 0)
    OP_6B(2060, 0)
    OP_6C(226000, 0)
    OP_6E(375, 0)
    SetChrPos(0x11, 4100, 500, 33000, 180)
    PlayEffect(0x1, 0x1, 0x109, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x117, 0x0, 0x64)
    FadeToBright(1000, 0)
    OP_0D()
    SoundLoad(213)
    SoundLoad(216)
    Sleep(1500)

    ChrTalk(    #86
        0x109,
        (
            "#1075F#5P哼哼……\x02\x03",

            "#1073F没想到这家伙能把我\x01",
            "逼到使用这种手段的境地……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E5B():
        OP_6D(2050, 0, 26000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4E5B)

    def lambda_4E73():
        OP_67(0, 5410, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4E73)

    def lambda_4E8B():
        OP_6B(2860, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4E8B)

    def lambda_4E9B():
        OP_6E(443, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4E9B)
    OP_82(0x1, 0x2)
    PlayEffect(0x2, 0x2, 0x109, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 20)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 22)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 24)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 26)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x109, 0x0)
    SetChrChipByIndex(0x109, 2)
    OP_99(0x109, 0x0, 0x7, 0xBB8)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #87
        0x109,
        (
            "#1073F#5P虽然这次的对象是恶魔……\x01",
            "但事到如今，我也只能认定你为『异端』了！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #88
        0x109,
        (
            "#1065F#5P死期将至，无望祈祷与悔恨！#2940W \x01",
            "#20W千厉荆棘，无尽绝望刻汝身！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #89
        0x109,
        (
            "#1072F#5P#3S化为尘埃\x01",
            "消失在无尽的黑暗中吧！！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)
    OP_35(0x8, 0x10F)
    OP_BB(0x8, 0x6, 0x10F)
    OP_A2(0x2911)
    Battle(0x1A6, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_5_C35 end

    def Function_6_508F(): pass

    label("Function_6_508F")

    Sleep(500)
    SetChrSubChip(0xFE, 3)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
    SetChrSubChip(0xFE, 2)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
    SetChrSubChip(0xFE, 1)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
    SetChrSubChip(0xFE, 0)
    OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xFA0)
    Fade(250)
    SetChrChipByIndex(0x109, 16)
    SetChrSubChip(0x109, 1)
    OP_0D()
    Sleep(500)
    Return()

    # Function_6_508F end

    def Function_7_510A(): pass

    label("Function_7_510A")

    SetChrChipByIndex(0x13, 7)
    SetChrSubChip(0x13, 0)

    def lambda_511A():
        OP_96(0xFE, 0x14F0, 0x0, 0x7788, 0x514, 0x1F40)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_511A)

    def lambda_5138():
        OP_9E(0xFE, 0x1E, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5138)
    WaitChrThread(0x13, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0x13, 0x20)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x800)
    ClearChrFlags(0x13, 0x2)
    OP_8C(0xFE, 45, 0)
    SetChrChipByIndex(0x13, 13)
    SetChrSubChip(0x13, 0)

    def lambda_5181():
        OP_8F(0xFE, 0x2170, 0x0, 0x7D5A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5181)

    ChrTalk(    #90 op#A op#5
        0x13,
        "#15A#5P啊……！\x05\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)
    Return()

    # Function_7_510A end

    def Function_8_51B9(): pass

    label("Function_8_51B9")

    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 45, 0)

    def lambda_51D5():
        OP_96(0xFE, 0xFFFFF45C, 0x0, 0x5FD2, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_51D5)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    Sleep(300)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 3)
    OP_8C(0xFE, 45, 0)

    def lambda_5222():
        OP_96(0xFE, 0xFFFFF9FC, 0x0, 0x53C0, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5222)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    Sleep(400)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 3)
    OP_8C(0xFE, 45, 0)

    def lambda_526F():
        OP_96(0xFE, 0xFFFFFDE4, 0x0, 0x5DD4, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_526F)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 5)

    def lambda_529C():
        OP_8E(0xFE, 0x1FE, 0x0, 0x6996, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_529C)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_8_51B9 end

    def Function_9_52C1(): pass

    label("Function_9_52C1")

    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 3)

    def lambda_52D6():
        OP_96(0xFE, 0xE10, 0x7D0, 0x7724, 0xDAC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_52D6)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 2)
    Sleep(100)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_5312():
        OP_96(0xFE, 0x596, 0x0, 0x693C, 0xBB8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5312)
    OP_51(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0xC5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x4F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 6)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 0, 0)
    OP_22(0x380, 0x0, 0x64)

    def lambda_53F6():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_53F6)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x5, 0xFF, 0x11, 0, 5000, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_544A():
        OP_7C(0x5DC, 0x5DC, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_544A)
    OP_43(0x11, 0x0, 0x0, 0xE)

    def lambda_5469():

        label("loc_5469")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_5469")

    QueueWorkItem2(0x11, 3, lambda_5469)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_51(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 2)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(200)
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0xFE, 0, 45)

    def lambda_5554():
        OP_96(0xFE, 0xFFFFFD6C, 0x0, 0x65FE, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5554)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_9_52C1 end

    def Function_10_5590(): pass

    label("Function_10_5590")

    SetChrFlags(0xFE, 0x1000)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 5)

    def lambda_55A5():
        OP_8E(0xFE, 0x1590, 0x0, 0x6C2A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55A5)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 2)
    Sleep(100)

    def lambda_55D4():
        OP_96(0xFE, 0xD20, 0x0, 0x765C, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55D4)
    Sleep(100)
    OP_51(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0xC5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0xB1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x4F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0x98), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 6)
    SetChrSubChip(0xFE, 0)
    OP_22(0x380, 0x0, 0x64)

    def lambda_56B6():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_56B6)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x5, 0xFF, 0x11, 0, 2000, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_570A():
        OP_7C(0x5DC, 0x5DC, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_570A)
    OP_43(0x11, 0x0, 0x0, 0xE)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_51(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 2)
    OP_22(0xA4, 0x0, 0x64)
    Return()

    # Function_10_5590 end

    def Function_11_57ED(): pass

    label("Function_11_57ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_581B")

    def lambda_57FC():
        OP_7C(0x1F4, 0x1F4, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_57FC)
    OP_22(0x280, 0x0, 0x64)
    Sleep(300)
    Jump("Function_11_57ED")

    label("loc_581B")

    Return()

    # Function_11_57ED end

    def Function_12_581C(): pass

    label("Function_12_581C")

    OP_22(0x223, 0x0, 0x64)
    OP_82(0x2, 0x2)

    def lambda_582A():
        OP_8F(0xFE, 0x1004, 0x1F4, 0x80E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_582A)

    def lambda_5845():
        OP_8C(0xFE, 0, 300)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5845)
    OP_D8(0x1, 0x3E8)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0xF)
    OP_6F(0x1, 121)
    OP_70(0x1, 0x8C)
    OP_73(0x1)
    OP_D8(0x1, 0x3E8)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x28)
    WaitChrThread(0xFE, 0x2)
    Return()

    # Function_12_581C end

    def Function_13_588E(): pass

    label("Function_13_588E")

    OP_22(0x223, 0x0, 0x64)

    def lambda_5899():
        OP_8F(0xFE, 0x1194, 0x0, 0x86C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5899)
    OP_D8(0x1, 0x3E8)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0xF)
    OP_6F(0x1, 121)
    OP_70(0x1, 0x8C)
    OP_73(0x1)
    OP_D8(0x1, 0x3E8)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x28)
    Return()

    # Function_13_588E end

    def Function_14_58EA(): pass

    label("Function_14_58EA")

    OP_22(0x223, 0x0, 0x64)
    OP_D8(0x1, 0x3E8)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0xF)
    OP_6F(0x1, 121)
    OP_70(0x1, 0x8C)
    OP_73(0x1)
    OP_D8(0x1, 0x3E8)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x28)
    Return()

    # Function_14_58EA end

    def Function_15_592B(): pass

    label("Function_15_592B")

    OP_22(0x223, 0x0, 0x64)

    def lambda_5936():
        OP_8F(0xFE, 0xA28, 0x0, 0x80E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5936)
    OP_D8(0x1, 0x3E8)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0xF)
    OP_6F(0x1, 121)
    OP_70(0x1, 0x8C)
    OP_73(0x1)
    Sleep(500)
    OP_D8(0x1, 0x3E8)
    OP_71(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x28)
    Return()

    # Function_15_592B end

    def Function_16_598C(): pass

    label("Function_16_598C")

    OP_20(0x0)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp254_00.eff")
    LoadEffect(0x1, "map\\mp254_01.eff")
    LoadEffect(0x2, "map\\mp253_00.eff")
    LoadEffect(0x3, "map\\mp253_01.eff")
    LoadEffect(0x4, "monster\\msc1000.eff")
    OP_E0(238, 0x54, 0x2)
    OP_E0(238, 0x55, 0x5)
    OP_E0(239, 0x56, 0x2)
    OP_E0(239, 0x57, 0x5)
    OP_E0(240, 0x58, 0x2)
    OP_E0(240, 0x59, 0x5)
    OP_E0(241, 0x5A, 0x2)
    OP_E0(241, 0x5B, 0x5)
    SetChrPos(0x109, 4040, 0, 25680, 0)
    SetChrPos(0x102, 3730, 0, 24050, 0)
    SetChrPos(0xF0, 3400, 0, 22350, 0)
    SetChrPos(0xF1, 5070, 0, 22060, 0)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 7)
    SetChrChipByIndex(0xEF, 22)
    SetChrSubChip(0xEF, 0)
    SetChrChipByIndex(0xF0, 24)
    SetChrSubChip(0xF0, 0)
    SetChrChipByIndex(0xF1, 26)
    SetChrSubChip(0xF1, 0)
    OP_7D(0x1, 0x13, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 7650, 0, 26500, 270)
    SetChrChipByIndex(0x13, 14)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x13, 0x4)
    ClearChrFlags(0x13, 0x2)
    SetChrFlags(0x13, 0x1)
    ClearChrFlags(0x13, 0x800)
    ClearChrFlags(0x13, 0x1000)
    ClearChrFlags(0x13, 0x20)
    OP_71(0x401, 0x0)
    ExitThread()
    OP_82(0x7, 0x0)
    OP_6D(5960, 0, 27870, 0)
    OP_67(0, 5340, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(135000, 0)
    OP_6E(294, 0)

    def lambda_5B25():
        OP_6D(5700, 0, 23300, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5B25)

    def lambda_5B3D():
        OP_67(0, 5120, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5B3D)

    def lambda_5B55():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5B55)

    def lambda_5B65():
        OP_6E(285, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B65)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x0, 65535)
    SetChrSubChip(0x0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x1, 65535)
    SetChrSubChip(0x1, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x2, 65535)
    SetChrSubChip(0x2, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #91
        0x109,
        "#1067F#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x13,
        "#1802F#5P凯、凯文……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x102,
        "#1502F#11P凯文……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    ClearChrFlags(0x12, 0x80)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x12, 3900, 1200, 28400, 0)
    PlayEffect(0x2, 0x7, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x13, 2)
    Sleep(500)

    def lambda_5CFE():
        OP_6D(5690, 0, 25210, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5CFE)
    OP_8F(0x109, 0xE9C, 0x0, 0x69B4, 0x3E8, 0x0)
    WaitChrThread(0x109, 0x0)
    Fade(250)
    SetChrChipByIndex(0x109, 18)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x12, 0xFBE, 0x4B0, 0x6B80, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x12, 0x80)
    OP_0D()
    Sleep(150)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #94
        "\x07\x00得到了\x1F\x5D\x03\x07\x00。\x02",
    )

    Jump("loc_5D9E")

    label("loc_5D9E")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x35D, 1)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #95
        0x102,
        "#1504F#11P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x109,
        (
            "#1075F#5P哼……\x01",
            "刚才那家伙带着这东西吗。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2960, 1000, 39000, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x10, 0x4)

    NpcTalk(    #97
        0x10,
        "嘶哑的声音",
        (
            "\x07\x02#2P呵呵……\x01",
            "做的不错，凯文·格拉汉姆。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0xC8, 1400, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5EFE")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5F65")

    label("loc_5EFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F26")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5F65")

    label("loc_5F26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F4E")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5F65")

    label("loc_5F4E")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5F65")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F92")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5FF9")

    label("loc_5F92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FBA")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5FF9")

    label("loc_5FBA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FE2")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5FF9")

    label("loc_5FE2")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5FF9")

    Sleep(1000)
    OP_1D(0xB0)

    def lambda_6006():
        OP_6D(4430, 0, 36490, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6006)

    def lambda_601E():
        OP_67(0, 5100, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_601E)

    def lambda_6036():
        OP_6B(2880, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6036)

    def lambda_6046():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6046)

    def lambda_6056():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6056)
    WaitChrThread(0x109, 0x0)
    SetChrPos(0x10, 3200, 0, 36000, 180)
    OP_22(0xBA, 0x1, 0x64)
    PlayEffect(0x0, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_60F5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_60F5)
    OP_22(0x59, 0x0, 0x64)
    WaitChrThread(0x109, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_23(0xBA)
    Sleep(1500)
    SetChrPos(0x109, 5070, 0, 22060, 0)

    ChrTalk(    #98
        0x109,
        "#1063F#1P你……\x02",
    )

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS417._CH")
    OP_C6(0x0, 0x0, 140000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1200)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("影之王")

    AnonymousTalk(    #99
        (
            "\x07\x02『──次回为兽之道。』\x02\x03",

            "『领受新供品，\x01",
            "  即让汝等发现印记。』\x02\x03",

            "『如此，炼狱之焰愈猛烈，\x01",
            "  吾王国竣工则指日可待——』\x02\x03",

            "呵呵，虽然还不够彻底，\x01",
            "不过情况不是完全相符吗？\x07\x00\x02",
        )
    )

    Jump("loc_6277")

    label("loc_6277")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    Sleep(1000)

    ChrTalk(    #100
        0x109,
        (
            "#1063F#1P……………………………………\x02\x03",

            "#1075F你……你到底是什么人……？\x02\x03",

            "#1060F你那低级趣味的面具……\x01",
            "也该摘下来了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x10,
        (
            "\x07\x02#1580F#5P哼哼，如果你希望的话。\x02\x03",

            "可是，凯文·格拉汉姆……\x02\x03",

            "……这真的是你\x01",
            "心底所希望的吗……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x109,
        "#1079F#1P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x10,
        (
            "\x07\x02#1580F#5P如果你真的希望如此，\x01",
            "我随时可以把面具摘下来。\x02\x03",

            "怎么样，凯文·格拉汉姆。\x02\x03",

            "你是否真的……\x01",
            "知道我的真面目了呢？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x109,
        (
            "#1067F#1P#50W…………………………………\x02\x03",

            "#1065F………我……我………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x13,
        "#1802F#1P……凯文………\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_8C(0x13, 315, 0)
    OP_6D(6270, 0, 29890, 0)
    OP_67(0, 4150, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(133000, 0)
    OP_6E(359, 0)
    SetChrPos(0x109, 3810, 0, 27800, 0)
    SetChrPos(0x102, 3990, 0, 25840, 0)
    SetChrPos(0xF0, 5970, 0, 23940, 0)
    SetChrPos(0xF1, 3410, 0, 24470, 0)
    SetChrPos(0x13, 5600, 0, 26980, 0)
    SetChrChipByIndex(0x13, 3)
    SetChrSubChip(0x13, 0)
    SetChrPos(0x10, 3500, 0, 36270, 180)

    def lambda_6591():
        OP_6D(5270, 0, 30890, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6591)
    OP_43(0x13, 0x0, 0x0, 0x11)
    WaitChrThread(0x13, 0x0)
    Sleep(500)

    ChrTalk(    #106
        0x13,
        (
            "#1449F#11P影之王……！\x01",
            "别再废话了……！\x02\x03",

            "虽然我不清楚情况，\x01",
            "但决不允许你再迷惑凯文……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10,
        (
            "\x07\x02#1580F#5P呵呵……\x01",
            "我可没有迷惑他。\x02\x03",

            "他只不过是选择了\x01",
            "不断自我迷惑而已。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x13,
        "#1443F#11P……呜………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x10,
        (
            "\x07\x02#1580F#5P哼哼……\x01",
            "这样一来阳光少女也得到解放了。\x02\x03",

            "你们的棋子也已经基本到齐，\x01",
            "终于可以准备\x01",
            "正式的游戏盘了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)

    def lambda_6734():

        label("loc_6734")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_6734")

    QueueWorkItem2(0x10, 3, lambda_6734)
    PlayEffect(0x4, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_82(0x0, 0x2)
    OP_22(0xBA, 0x1, 0x64)
    PlayEffect(0x0, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6818")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_687F")

    label("loc_6818")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6840")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_687F")

    label("loc_6840")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6868")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_687F")

    label("loc_6868")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_687F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68AC")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6913")

    label("loc_68AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68D4")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6913")

    label("loc_68D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68FC")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6913")

    label("loc_68FC")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6913")

    Sleep(1000)

    ChrTalk(    #110
        0x13,
        "#1441F#11P啊……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x102,
        "#1502F#11P……哼………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x10,
        (
            "\x07\x02#1580F#5P呵呵，接下来是梦魔之道……\x02\x03",

            "请一边穿越光与影的缝隙，\x01",
            "一边收集白与黑的棋子。\x02\x03",

            "当所有的棋子集齐时，\x01",
            "游戏将进入新的阶段。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_6A03():

        label("loc_6A03")

        OP_99(0xFE, 0x8, 0xF, 0x5DC)
        OP_48()
        Jump("loc_6A03")

    QueueWorkItem2(0x10, 3, lambda_6A03)
    PlayEffect(0x1, 0x2, 0x10, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_6A4B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6A4B)
    OP_22(0x59, 0x0, 0x64)
    OP_0D()
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    OP_23(0xBA)
    OP_20(0x7D0)
    Sleep(2500)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x13, 3)
    SetChrSubChip(0x13, 0)
    OP_0D()
    Sleep(500)

    def lambda_6A90():
        OP_6D(6680, 0, 25710, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6A90)

    def lambda_6AA8():
        OP_67(0, 4150, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6AA8)

    def lambda_6AC0():
        OP_6B(2650, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6AC0)

    def lambda_6AD0():
        OP_6E(340, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6AD0)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B21")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6B79")

    label("loc_6B21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B44")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6B79")

    label("loc_6B44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B67")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6B79")

    label("loc_6B67")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_6B79")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B9C")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6BF4")

    label("loc_6B9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BBF")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6BF4")

    label("loc_6BBF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BE2")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6BF4")

    label("loc_6BE2")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_6BF4")

    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x109, 0x0)
    OP_63(0x109)
    OP_63(0x102)
    OP_63(0xF0)
    OP_63(0xF1)
    OP_63(0x13)
    Sleep(500)

    ChrTalk(    #113
        0x109,
        "#1067F#5P#11P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 400)
    Sleep(300)

    ChrTalk(    #114
        0x13,
        "#1802F#6P凯文，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x109,
        (
            "#1065F#11P唉，虽然有很多事……\x01",
            "不过还是之后再说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x13,
        "#1444F#6P……哎…………\x02",
    )

    CloseMessageWindow()

    def lambda_6CED():
        OP_6D(6000, 0, 24700, 1300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6CED)
    OP_8C(0x109, 180, 400)
    Sleep(300)
    WaitChrThread(0x109, 0x0)
    Fade(250)
    SetChrChipByIndex(0x109, 18)
    SetChrSubChip(0x109, 0)
    Sleep(100)
    OP_22(0x233, 0x0, 0x64)
    ClearChrFlags(0x12, 0x80)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x12, 3850, 1200, 27050, 0)
    PlayEffect(0x2, 0x7, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1500)

    ChrTalk(    #117
        0x102,
        "#1504F#11P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x109,
        (
            "#1840F#6P『阳光少女』……\x01",
            "是大家期待已久的主角呢。\x02\x03",

            "首先还是先把她解放出来……\x01",
            "然后再说明详细情况吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        "#1501F#11P凯文先生……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EA6")

    ChrTalk(    #120
        0x106,
        "#051F#11P嘿……没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F70")

    label("loc_6EA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EDA")

    ChrTalk(    #121
        0x104,
        "#1541F#11P呵……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F70")

    label("loc_6EDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F0D")

    ChrTalk(    #122
        0x108,
        "#070F#11P啊……没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F70")

    label("loc_6F0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F40")

    ChrTalk(    #123
        0x10E,
        "#170F#11P啊……没错。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F70")

    label("loc_6F40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F70")

    ChrTalk(    #124
        0x10D,
        "#277F#11P啊……没错。\x02",
    )

    CloseMessageWindow()

    label("loc_6F70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FAD")

    ChrTalk(    #125
        0x107,
        "#066F#11P太好了……这样的话……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7066")

    label("loc_6FAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FEB")

    ChrTalk(    #126
        0x105,
        "#1168F#11P太好了……这样一来……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7066")

    label("loc_6FEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_702B")

    ChrTalk(    #127
        0x103,
        "#1527F#11P哎呀哎呀……这样一来……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7066")

    label("loc_702B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7066")

    ChrTalk(    #128
        0x10A,
        "#1314F#11P太好了……这样的话……\x02",
    )

    CloseMessageWindow()

    label("loc_7066")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7098")

    ChrTalk(    #129
        0x10B,
        "#210F#11P唉……没办法。\x02",
    )

    CloseMessageWindow()

    label("loc_7098")

    OP_20(0xBB8)

    def lambda_70A3():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_70A3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_35(0xE, 0x173)
    OP_A2(0x2504)
    OP_A2(0x250A)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_598C end

    def Function_17_70D0(): pass

    label("Function_17_70D0")

    SetChrChipByIndex(0xFE, 15)
    SetChrSubChip(0xFE, 0)
    OP_8F(0xFE, 0x104A, 0x0, 0x735A, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 3)
    SetChrSubChip(0xFE, 0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    OP_0D()
    Return()

    # Function_17_70D0 end

    def Function_18_710E(): pass

    label("Function_18_710E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 1)), scpexpr(EXPR_END)), "loc_7116")
    Return()

    label("loc_7116")

    EventBegin(0x0)
    Fade(500)
    OP_6D(2050, 0, 42000, 0)
    OP_67(0, 6620, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(315000, 0)
    OP_6E(268, 0)
    SetChrPos(0x10F, 3550, 0, 40170, 0)
    SetChrPos(0x101, 2220, 0, 40070, 0)
    SetChrPos(0xF0, 3570, 0, 38250, 0)
    SetChrPos(0xF1, 2000, 0, 38200, 0)
    OP_0D()
    OP_43(0x101, 0x0, 0x0, 0x13)
    WaitChrThread(0x101, 0x0)
    Sleep(300)

    ChrTalk(    #130
        0x101,
        (
            "#1004F#6P呜哇……\x02\x03",

            "虽然已经听你们说过了，\x01",
            "不过这还真是让人惊讶啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_728F")

    ChrTalk(    #131
        0x10A,
        (
            "#1310F#6P嗯嗯。\x02\x03",

            "#819F这种地方实在是\x01",
            "没法让人产生锻炼的心情呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#1016F#5P哈哈……的确是呢。\x02",
    )

    CloseMessageWindow()

    label("loc_728F")

    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(    #133
        0x101,
        (
            "#1002F#6P……那么，这边的魔法阵\x01",
            "就是进入下一个星层的入口对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x10F,
        (
            "#1446F#6P是的……\x01",
            "应该是『第五星层』了。\x02\x03",

            "#1443F就是『影之王』\x01",
            "所说的『正式的游戏盘』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1007F#6P嗯，从这些话上听起来，\x01",
            "好像是很难通过的地方呢。\x02\x03",

            "#1006F进去之前得做好准备才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x10F,
        (
            "#1446F#6P……是啊…………\x02\x03",

            "#1445F……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(300)

    ChrTalk(    #137
        0x101,
        (
            "#1011F#5P嗯？\x01",
            "莉丝小姐，怎么了？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_744F():
        OP_6D(2050, 0, 41200, 800)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_744F)
    OP_8C(0x10F, 270, 400)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)

    ChrTalk(    #138
        0x10F,
        (
            "#1802F#12P……艾丝蒂尔小姐。\x02\x03",

            "为什么你要特地\x01",
            "提出和我同行呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        "#1004F#5P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x10F,
        (
            "#1446F#12P在这种情况下，\x01",
            "你应该没有一定要来的理由的。\x02\x03",

            "可是，你的眼睛里\x01",
            "却充满了诚意和决心。\x02\x03",

            "#1440F我可以请教一下理由吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1016F#5P我、我觉得\x01",
            "并没有什么夸张的理由啊……\x02\x03",

            "#1015F嗯……对了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #142
        0x101,
        (
            "#1011F#5P真要说的话……\x01",
            "就算是报恩吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x10F,
        "#1444F#12P……报恩？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#1012F#5P也许你已经听说了，\x01",
            "我之前受了凯文先生\x01",
            "很大的照顾呢。\x02\x03",

            "他帮了我们很多忙，\x01",
            "最重要的是还协助约修亚\x01",
            "解决了那么困难的问题。\x02\x03",

            "#1025F现在凯文先生有难，\x01",
            "我就想一定要做些什么才行……\x02\x03",

            "所以我就来帮\x01",
            "莉丝小姐的忙了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_774D")

    ChrTalk(    #145
        0x102,
        "#1500F#6P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    Jump("loc_77E6")

    label("loc_774D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7780")

    ChrTalk(    #146
        0x105,
        "#1382F#6P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    Jump("loc_77E6")

    label("loc_7780")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77B6")

    ChrTalk(    #147
        0x107,
        "#066F#6P艾丝蒂尔姐姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_77E6")

    label("loc_77B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77E6")

    ChrTalk(    #148
        0x103,
        "#1527F#6P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    label("loc_77E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_781A")

    ChrTalk(    #149
        0x106,
        "#051F#6P嘿，是这样吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_78B6")

    label("loc_781A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_784C")

    ChrTalk(    #150
        0x104,
        "#1545F呵，是这样吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_78B6")

    label("loc_784C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7880")

    ChrTalk(    #151
        0x108,
        "#573F#6P呼，是这样吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_78B6")

    label("loc_7880")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78B6")

    ChrTalk(    #152
        0x10A,
        "#1314F#6P呵呵，是这样吗……\x02",
    )

    CloseMessageWindow()

    label("loc_78B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78F0")

    ChrTalk(    #153
        0x10E,
        "#179F#6P（……原来如此啊。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_7925")

    label("loc_78F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7925")

    ChrTalk(    #154
        0x10D,
        "#278F#6P（……是这样啊。）\x02",
    )

    CloseMessageWindow()

    label("loc_7925")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_795E")

    ChrTalk(    #155
        0x10B,
        "#413F#6P（还是老好人一个……）\x02",
    )

    CloseMessageWindow()

    label("loc_795E")


    ChrTalk(    #156
        0x10F,
        (
            "#1802F#12P可、可是……\x02\x03",

            "你要对凯文报恩，\x01",
            "和来帮助我有什么关系呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        (
            "#1004F#5P哎，可是……\x02\x03",

            "莉丝小姐，\x01",
            "不是凯文先生最重要的人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x10F)
    Sleep(500)

    ChrTalk(    #158
        0x10F,
        "#1444F#12P#3S哎。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        (
            "#1016F#5P啊，\x01",
            "我可不是说你们是恋人……\x02\x03",

            "#1025F从大家的话看来，\x01",
            "你们好像是家人的感觉……对吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x10F,
        (
            "#1445F#12P……我想你是搞错了。\x02\x03",

            "#1446F我和凯文已经\x01",
            "有五年时间没有见面了。\x02\x03",

            "在这次的事件中\x01",
            "才得以再次见面……\x02\x03",

            "#1806F可以说……\x01",
            "缘分早就已经断了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1001F#5P哈哈，才不是这样呢。\x02",
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #162
        0x10F,
        "#1444F#12P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#1012F#5P『深刻的缘分会成为羁绊，\x01",
            "  而羁绊永远不会被切断。』\x02\x03",

            "『就算相隔千里，或是立场相悖，\x01",
            "  羁绊也一定以某种形式存在着。』\x02\x03",

            "#1006F──这是某个总爱\x01",
            "得意忘形的大叔所说的话。\x02\x03",

            "不过我觉得这句话\x01",
            "的确是切中了要害。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x10F,
        "#1444F#12P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        (
            "#1011F#5P凯文先生不是毫不犹豫地\x01",
            "就把接下来的事托付给了莉丝小姐吗？\x02\x03",

            "而且莉丝小姐\x01",
            "也立刻明白了\x01",
            "凯文先生的用意。\x02\x03",

            "#1012F嗯，我觉得这就是所谓的羁绊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x10F,
        (
            "#1445F#12P…………………………………\x02\x03",

            "#1446F……我不太明白。\x02\x03",

            "#1806F不过，\x01",
            "我接受你同行的理由。\x02\x03",

            "那么再一次……\x01",
            "请多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#1016F#5P啊哈哈……\x01",
            "嗯，彼此彼此！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x10F,
        (
            "#1446F#12P然后……\x02\x03",

            "关于艾丝蒂尔小姐本人，\x01",
            "我也想打听一件事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        (
            "#1004F#5P我的事情？\x02\x03",

            "#1006F嗯，反正机会难得，\x01",
            "随便问什么都行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x10F,
        (
            "#1447F#12P那就……\x02\x03",

            "#1448F你是不是经常\x01",
            "被人叫做『老好人』啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #171
        0x101,
        "#1004F#5P咦……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FC0")

    ChrTalk(    #172
        0x10B,
        "#210F#6P噗……！\x02",
    )

    CloseMessageWindow()

    label("loc_7FC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FEC")

    ChrTalk(    #173
        0x102,
        "#1514F#6P哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_7FEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8018")

    ChrTalk(    #174
        0x105,
        "#1165F#6P呵呵……\x02",
    )

    CloseMessageWindow()

    label("loc_8018")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8043")

    ChrTalk(    #175
        0x107,
        "#067F#6P嘻嘻……\x02",
    )

    CloseMessageWindow()

    label("loc_8043")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_806F")

    ChrTalk(    #176
        0x103,
        "#1521F#6P呵呵……\x02",
    )

    CloseMessageWindow()

    label("loc_806F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8098")

    ChrTalk(    #177
        0x106,
        "#051F#6P嘿……\x02",
    )

    CloseMessageWindow()

    label("loc_8098")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80C2")

    ChrTalk(    #178
        0x104,
        "#1541F#6P呵……\x02",
    )

    CloseMessageWindow()

    label("loc_80C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80EF")

    ChrTalk(    #179
        0x108,
        "#071F#6P哈哈哈……\x02",
    )

    CloseMessageWindow()

    label("loc_80EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_811E")

    ChrTalk(    #180
        0x10A,
        "#819F#6P啊哈哈……！\x02",
    )

    CloseMessageWindow()

    label("loc_811E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8149")

    ChrTalk(    #181
        0x10E,
        "#171F#6P呵呵……\x02",
    )

    CloseMessageWindow()

    label("loc_8149")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8172")

    ChrTalk(    #182
        0x10D,
        "#275F#6P呵……\x02",
    )

    CloseMessageWindow()

    label("loc_8172")

    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8C(0x101, 135, 400)
    Sleep(300)

    ChrTalk(    #183
        0x101,
        (
            "#1019F#5P等、等一下！\x01",
            "为什么你们这么笑啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x10F,
        (
            "#1447F#12P……原来如此。\x01",
            "不用回答我也知道了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(300)

    ChrTalk(    #185
        0x101,
        (
            "#1007F#5P真、真是的……\x01",
            "别就这么擅自理解啊。\x02\x03",

            "#1008F算了，\x01",
            "我们赶快前往『第五星层』吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x10F,
        "#1448F#12P嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2A01)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_18_710E end

    def Function_19_82AD(): pass

    label("Function_19_82AD")

    OP_8C(0xFE, 270, 400)
    Sleep(300)
    OP_8C(0xFE, 45, 400)
    Sleep(300)
    OP_8C(0xFE, 315, 400)
    Sleep(300)
    Return()

    # Function_19_82AD end

    def Function_20_82D2(): pass

    label("Function_20_82D2")

    EventBegin(0x0)
    Fade(500)
    OP_6D(3650, 0, 44180, 0)
    OP_67(0, 7530, -10000, 0)
    OP_6B(3360, 0)
    OP_6C(45000, 0)
    OP_6E(271, 0)
    SetChrPos(0x10F, 2930, 0, 44660, 0)
    SetChrPos(0x101, 3840, 0, 43790, 0)
    SetChrPos(0xF0, 2100, 0, 43850, 0)
    SetChrPos(0xF1, 3060, 0, 42960, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_0D()
    Sleep(500)
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 2990, 0, 43800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_83E0():
        OP_6D(3650, 0, 44180, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_83E0)

    def lambda_83F8():
        OP_67(0, 7530, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_83F8)

    def lambda_8410():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_8410)

    def lambda_8420():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_8420)

    def lambda_8430():
        OP_6E(241, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8430)
    Call(0, 27)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x10F, 0x0)
    OP_44(0x10F, 0x1)
    OP_44(0x10F, 0x2)
    OP_44(0x10F, 0x3)
    OP_44(0x101, 0x1)
    NewScene("ED6_DT21/M7200   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_20_82D2 end

    def Function_21_8469(): pass

    label("Function_21_8469")

    ClearMapFlags(0x2000000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_848C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_849D")

    label("loc_848C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_849D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_849D")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_84C2"),
        (1, "loc_84F1"),
        (2, "loc_8520"),
        (SWITCH_DEFAULT, "loc_854F"),
    )


    label("loc_84C2")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP001._CH")
    Jump("loc_854F")

    label("loc_84F1")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP002._CH")
    Jump("loc_854F")

    label("loc_8520")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP003._CH")
    Jump("loc_854F")

    label("loc_854F")

    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8584")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_88F1")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_85AF"),
        (1, "loc_85DB"),
        (2, "loc_8618"),
        (SWITCH_DEFAULT, "loc_866A"),
    )


    label("loc_85AF")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
        )
    )

    Jump("loc_866A")

    label("loc_85DB")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",        # 0
            "【巴斯塔尔水道】\x01",      # 1
            "【圣科洛瓦森林】\x01",      # 2
        )
    )

    Jump("loc_866A")

    label("loc_8618")


    Menu(
        0,
        30,
        80,
        0,
        (
            "【训练场宿舍】\x01",            # 0
            "【巴斯塔尔水道】\x01",          # 1
            "【圣科洛瓦森林】\x01",          # 2
            "【格林姆瑟尔小要塞】\x01",      # 3
        )
    )

    Jump("loc_866A")

    label("loc_866A")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8694"),
        (1, "loc_8728"),
        (2, "loc_87BE"),
        (3, "loc_8854"),
        (SWITCH_DEFAULT, "loc_88EE"),
    )


    label("loc_8694")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #187
        "\x07\x05要移动至【训练场宿舍】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_86F3")

    label("loc_86F3")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8715"),
        (1, "loc_8722"),
        (SWITCH_DEFAULT, "loc_8725"),
    )


    label("loc_8715")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8725")

    label("loc_8722")

    Jump("loc_8725")

    label("loc_8725")

    Jump("loc_88EE")

    label("loc_8728")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #188
        "\x07\x05要移动至【巴斯塔尔水道】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_8789")

    label("loc_8789")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_87AB"),
        (1, "loc_87B8"),
        (SWITCH_DEFAULT, "loc_87BB"),
    )


    label("loc_87AB")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_87BB")

    label("loc_87B8")

    Jump("loc_87BB")

    label("loc_87BB")

    Jump("loc_88EE")

    label("loc_87BE")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #189
        "\x07\x05要移动至【圣科洛瓦森林】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_881F")

    label("loc_881F")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8841"),
        (1, "loc_884E"),
        (SWITCH_DEFAULT, "loc_8851"),
    )


    label("loc_8841")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8851")

    label("loc_884E")

    Jump("loc_8851")

    label("loc_8851")

    Jump("loc_88EE")

    label("loc_8854")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #190
        "\x07\x05要移动至【格林姆瑟尔小要塞】吗？\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "【是】\x01",      # 0
            "【否】\x01",      # 1
        )
    )

    Jump("loc_88B9")

    label("loc_88B9")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_88DB"),
        (1, "loc_88E8"),
        (SWITCH_DEFAULT, "loc_88EB"),
    )


    label("loc_88DB")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_88EB")

    label("loc_88E8")

    Jump("loc_88EB")

    label("loc_88EB")

    Jump("loc_88EE")

    label("loc_88EE")

    Jump("loc_8584")

    label("loc_88F1")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_890A"),
        (1, "loc_893E"),
        (2, "loc_8972"),
        (3, "loc_89A6"),
        (SWITCH_DEFAULT, "loc_89DA"),
    )


    label("loc_890A")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_89DA")

    label("loc_893E")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_89DA")

    label("loc_8972")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_89DA")

    label("loc_89A6")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_89DA")

    label("loc_89DA")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_89FC"),
        (1, "loc_8A08"),
        (2, "loc_8A14"),
        (3, "loc_8A20"),
        (SWITCH_DEFAULT, "loc_8A2C"),
    )


    label("loc_89FC")

    NewScene("ED6_DT21/U5102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_8A2C")

    label("loc_8A08")

    NewScene("ED6_DT21/M5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_8A2C")

    label("loc_8A14")

    NewScene("ED6_DT21/M5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_8A2C")

    label("loc_8A20")

    NewScene("ED6_DT21/M5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_8A2C")

    label("loc_8A2C")

    Return()

    # Function_21_8469 end

    def Function_22_8A2D(): pass

    label("Function_22_8A2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8A3E")
    Call(0, 2)
    Return()

    label("loc_8A3E")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 7560, 0, 5540, 180)
    SetChrPos(0x1, 6540, 0, 6210, 180)
    SetChrPos(0x2, 8230, 0, 6140, 180)
    SetChrPos(0x3, 7310, 0, 7160, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 7240, 0, 6380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 26)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x104), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_22_8A2D end

    def Function_23_8B1C(): pass

    label("Function_23_8B1C")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 3060, 0, 42960, 180)
    SetChrPos(0x1, 2100, 0, 43850, 180)
    SetChrPos(0x2, 3840, 0, 43790, 180)
    SetChrPos(0x3, 2930, 0, 44660, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 2990, 0, 43800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 26)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x104), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_23_8B1C end

    def Function_24_8BFA(): pass

    label("Function_24_8BFA")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 7450, 0, 5430, 0)
    SetChrPos(0x2, 6540, 0, 6210, 0)
    SetChrPos(0x1, 8230, 0, 6140, 0)
    SetChrPos(0x0, 7310, 0, 7160, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 7240, 0, 6380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 27)
    NewScene("ED6_DT21/M7107   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_24_8BFA end

    def Function_25_8CB6(): pass

    label("Function_25_8CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CC7")
    Call(0, 20)
    Return()

    label("loc_8CC7")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 3060, 0, 42960, 0)
    SetChrPos(0x2, 2100, 0, 43850, 0)
    SetChrPos(0x1, 3840, 0, 43790, 0)
    SetChrPos(0x0, 2930, 0, 44660, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 2990, 0, 43800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 27)
    NewScene("ED6_DT21/M7200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_8CB6 end

    def Function_26_8D83(): pass

    label("Function_26_8D83")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DAC")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8DA0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8DA0)

    label("loc_8DAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DD5")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8DC9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8DC9)

    label("loc_8DD5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DFE")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8DF2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_8DF2)

    label("loc_8DFE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E27")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_8E1B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_8E1B)

    label("loc_8E27")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E53")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_8E53")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E6A")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_8E6A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E81")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_8E81")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E98")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_8E98")

    Return()

    # Function_26_8D83 end

    def Function_27_8E99(): pass

    label("Function_27_8E99")


    def lambda_8E9F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8E9F)

    def lambda_8EB1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8EB1)

    def lambda_8EC3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_8EC3)

    def lambda_8ED5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_8ED5)
    Sleep(1000)
    Return()

    # Function_27_8E99 end

    def Function_28_8EE7(): pass

    label("Function_28_8EE7")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #191
        (
            "\x07\x05　　 游击士协会\x01",
            "【卢·洛克尔训练场】\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_28_8EE7 end

    SaveToFile()

Try(main)
