from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Lord of Phantasma',                    # 9
        'Astarte',                              # 10
        'Sealing Stone',                        # 11
        'Ries',                                 # 12
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
        "Function_3_830",          # 03, 3
        "Function_4_CDC",          # 04, 4
        "Function_5_CED",          # 05, 5
        "Function_6_5449",         # 06, 6
        "Function_7_54C4",         # 07, 7
        "Function_8_5568",         # 08, 8
        "Function_9_5670",         # 09, 9
        "Function_10_593F",        # 0A, 10
        "Function_11_5B9C",        # 0B, 11
        "Function_12_5BCB",        # 0C, 12
        "Function_13_5C3D",        # 0D, 13
        "Function_14_5C99",        # 0E, 14
        "Function_15_5CDA",        # 0F, 15
        "Function_16_5D3B",        # 10, 16
        "Function_17_7544",        # 11, 17
        "Function_18_7582",        # 12, 18
        "Function_19_8AEA",        # 13, 19
        "Function_20_8B0F",        # 14, 20
        "Function_21_8CA6",        # 15, 21
        "Function_22_9202",        # 16, 22
        "Function_23_92F1",        # 17, 23
        "Function_24_93CF",        # 18, 24
        "Function_25_948B",        # 19, 25
        "Function_26_9558",        # 1A, 26
        "Function_27_966E",        # 1B, 27
        "Function_28_96BC",        # 1C, 28
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
        "#1079F#5PHold on...\x02",
    )

    CloseMessageWindow()

    def lambda_5E9():
        OP_6D(-4000, 4600, 5220, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5E9)

    def lambda_601():
        OP_67(0, 7780, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_601)

    def lambda_619():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_619)

    def lambda_629():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_629)

    def lambda_639():
        OP_6E(283, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_639)
    Sleep(100)

    def lambda_64E():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_64E)
    Sleep(100)

    def lambda_661():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_661)
    Sleep(100)

    def lambda_674():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_674)
    Sleep(100)
    OP_8C(0xF0, 270, 400)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #1
        0x102,
        (
            "#1502F#1PIt looks like it changed to night here while\x01",
            "we were away.\x02\x03",

            "All the lights are on now, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1063F#1PYeah. We saw this happen back on the second plane,\x01",
            "too.\x02",
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
            "#1063F#6PAnd I bet the time of day isn't the only thing that's\x01",
            "changed here, too. Let's see if we can find anything\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x102,
        "#1502F#5PGot it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x290F)
    OP_28(0x34, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_2EA end

    def Function_3_830(): pass

    label("Function_3_830")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -2009, 0, -39880, 0)
    SetChrPos(0x102, -3200, 0, -39980, 0)
    SetChrPos(0xF0, -2040, 0, -41870, 0)
    SetChrPos(0xF1, -3310, 0, -41390, 0)

    def lambda_886():
        OP_8E(0xFE, 0xFFFFFA56, 0x0, 0xFFFF7EF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_886)
    Sleep(150)

    def lambda_8A6():
        OP_8E(0xFE, 0xFFFFF506, 0x0, 0xFFFF7FD6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8A6)
    Sleep(150)

    def lambda_8C6():
        OP_8E(0xFE, 0xFFFFFA38, 0x0, 0xFFFF78A6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_8C6)
    Sleep(150)

    def lambda_8E6():
        OP_8E(0xFE, 0xFFFFF420, 0x0, 0xFFFF7A36, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_8E6)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9BB")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A22")

    label("loc_9BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E3")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A22")

    label("loc_9E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A22")

    label("loc_A0B")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A22")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A4F")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AB6")

    label("loc_A4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A77")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AB6")

    label("loc_A77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9F")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_AB6")

    label("loc_A9F")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_AB6")

    Sleep(1000)

    ChrTalk(    #5
        0x109,
        "#1079F#6PHold on...\x02",
    )

    CloseMessageWindow()

    def lambda_ADA():
        OP_6D(-4000, 4600, 5220, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ADA)

    def lambda_AF2():
        OP_67(0, 7780, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_AF2)

    def lambda_B0A():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_B0A)

    def lambda_B1A():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B1A)

    def lambda_B2A():
        OP_6E(283, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B2A)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #6
        0x102,
        (
            "#1502F#2PIt looks like it changed to night here while\x01",
            "we were away.\x02\x03",

            "All the lights are on now, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1063F#2PYeah. We saw this happen back on the second plane,\x01",
            "too.\x02",
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
            "#1063F#6PAnd I bet the time of day isn't the only thing that's\x01",
            "changed here, too. Let's see if we can find anything\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        "#1502F#5PGot it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x290F)
    OP_28(0x34, 0x1, 0x20)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_3_830 end

    def Function_4_CDC(): pass

    label("Function_4_CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_CE4")
    Return()

    label("loc_CE4")

    Call(0, 5)
    Call(0, 16)
    Return()

    # Function_4_CDC end

    def Function_5_CED(): pass

    label("Function_5_CED")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD6")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E3D")

    label("loc_DD6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFE")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E3D")

    label("loc_DFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E26")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_E3D")

    label("loc_E26")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_E3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E65")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_ECC")

    label("loc_E65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8D")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_ECC")

    label("loc_E8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB5")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_ECC")

    label("loc_EB5")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_ECC")

    Sleep(1000)

    def lambda_ED7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ED7)

    def lambda_EE5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_EE5)

    def lambda_EF3():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_EF3)

    def lambda_F01():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_F01)
    Sleep(400)

    ChrTalk(    #10
        0x102,
        "#1502F#6PLook over there!\x02",
    )

    CloseMessageWindow()

    def lambda_F33():
        OP_6D(1760, 0, 46230, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F33)

    def lambda_F4B():
        OP_67(0, 5620, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F4B)

    def lambda_F63():
        OP_6B(4460, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F63)

    def lambda_F73():
        OP_6C(327000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_F73)

    def lambda_F83():
        OP_6E(268, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F83)
    WaitChrThread(0x109, 0x0)
    SetChrPos(0x109, 3340, 0, 32150, 0)
    SetChrPos(0x102, 1880, 0, 32180, 0)
    SetChrPos(0xF0, 3310, 0, 30620, 0)
    SetChrPos(0xF1, 1940, 0, 30550, 0)
    Sleep(500)

    ChrTalk(    #11
        0x109,
        "#1063F#2PThat must be the warp to the next plane!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1094")

    ChrTalk(    #12
        0x10E,
        (
            "#178F#2PStill, it's hard to believe that this is the same spot\x01",
            "where we saw that beautiful scenery earlier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_1094")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1116")

    ChrTalk(    #13
        0x10D,
        (
            "#270F#2PStill, it's hard to believe that this is the same spot\x01",
            "where we saw that beautiful scenery earlier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_1116")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1198")

    ChrTalk(    #14
        0x108,
        (
            "#072F#2PStill, it's hard to believe that this is the same spot\x01",
            "where we saw that beautiful scenery earlier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_1198")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_121B")

    ChrTalk(    #15
        0x103,
        (
            "#1522F#2PStill, it's hard to believe that this is the same spot\x01",
            "where we saw that beautiful scenery earlier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_121B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_129E")

    ChrTalk(    #16
        0x10A,
        (
            "#1317F#2PStill, it's hard to believe that this is the same spot\x01",
            "where we saw that beautiful scenery earlier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_129E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1321")

    ChrTalk(    #17
        0x104,
        (
            "#1540F#2PStill, it's hard to believe that this is the same spot\x01",
            "where we saw that beautiful scenery earlier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_1321")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13A4")

    ChrTalk(    #18
        0x105,
        (
            "#1163F#2PStill, it's hard to believe that this is the same spot\x01",
            "where we saw that beautiful scenery earlier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_13A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1426")

    ChrTalk(    #19
        0x10B,
        (
            "#216F#2PStill, it's hard to believe that this is the same spot\x01",
            "where we saw that beautiful scenery earlier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14A5")

    label("loc_1426")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14A5")

    ChrTalk(    #20
        0x107,
        (
            "#065F#2PStill, it's hard to believe that this is the same spot\x01",
            "where we saw that beautiful scenery earlier.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1551")

    ChrTalk(    #21
        0x106,
        (
            "#053F#2PHeh. The pretty covering's finally off to show us\x01",
            "what's underneath, huh?\x02\x03",

            "#051FIf nothin' else, you're not ever gonna get bored\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C3")

    label("loc_1551")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_159D")

    ChrTalk(    #22
        0x107,
        "#065F#2PSo the view we saw earlier wasn't real, then?\x02",
    )

    CloseMessageWindow()
    Jump("loc_18C3")

    label("loc_159D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15F9")

    ChrTalk(    #23
        0x10B,
        (
            "#212F#2PThe pretty view we saw earlier probably wasn't\x01",
            "real, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C3")

    label("loc_15F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_166C")

    ChrTalk(    #24
        0x105,
        (
            "#1162F#2PI don't think we can accept this being the\x01",
            "real Le Locle after seeing it like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C3")

    label("loc_166C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16E9")

    ChrTalk(    #25
        0x104,
        (
            "#1545F#2PHard to accept anything but the reality in front\x01",
            "of us, really. This isn't the real Le Locle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C3")

    label("loc_16E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_175C")

    ChrTalk(    #26
        0x10A,
        (
            "#812F#2PI don't think we've got much choice but to\x01",
            "accept that this isn't the real Le Locle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C3")

    label("loc_175C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17D7")

    ChrTalk(    #27
        0x103,
        (
            "#1525F#2P*sigh* I don't think we've got much choice but\x01",
            "to accept that this isn't the real Le Locle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C3")

    label("loc_17D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_184A")

    ChrTalk(    #28
        0x108,
        (
            "#074F#2PI don't think we've got much choice but to\x01",
            "accept that this isn't the real Le Locle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C3")

    label("loc_184A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18C3")

    ChrTalk(    #29
        0x10D,
        (
            "#272F#2PHard to accept anything but the reality in front\x01",
            "of us, really. This isn't the real Le Locle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C3")

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
        "#1502F#5PYou think we should proceed onward?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1067F#6PI'd say so. We might as well at least get a look\x01",
            "at what we're going to be facing on the nex--\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AA1")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B08")

    label("loc_1AA1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AC9")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B08")

    label("loc_1AC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AF1")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B08")

    label("loc_1AF1")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1B08")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B35")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B9C")

    label("loc_1B35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B5D")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B9C")

    label("loc_1B5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B85")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B9C")

    label("loc_1B85")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1B9C")

    Sleep(1000)

    def lambda_1BA7():
        OP_6D(3420, 0, 27120, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1BA7)

    def lambda_1BBF():
        OP_67(0, 7290, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1BBF)

    def lambda_1BD7():
        OP_6B(3390, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1BD7)

    def lambda_1BE7():
        OP_6E(270, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1BE7)
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
        "#1502F#5PGah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x109,
        "#1069F#6PBut not before we deal with this first!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0x9A)
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0x85, 0x1, 0x64)

    def lambda_1CBC():

        label("loc_1CBC")

        OP_7C(0x50, 0x50, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1CBC")

    QueueWorkItem2(0x102, 3, lambda_1CBC)
    PlayEffect(0x1, 0x1, 0xFF, 3400, 200, 30120, 0, 0, 0, 1800, 1800, 1800, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x11, 3400, -9000, 30120, 180)
    OP_A1(0x11, 0x1)
    OP_72(0x401, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x28)

    def lambda_1D3A():
        OP_8F(0xFE, 0xD48, 0x1F4, 0x75A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1D3A)
    Fade(1000)
    OP_6D(3400, 1000, 27000, 0)
    OP_67(0, 3000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(330, 0)

    def lambda_1D97():
        OP_6D(3400, 4000, 30420, 9500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1D97)

    def lambda_1DAF():
        OP_67(0, 1020, -10000, 9500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1DAF)

    def lambda_1DC7():
        OP_6B(2500, 9500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1DC7)

    def lambda_1DD7():
        OP_6E(320, 9500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1DD7)
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

    def lambda_1E55():
        OP_6D(3400, 2300, 30420, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1E55)

    def lambda_1E6D():
        OP_67(0, 1020, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1E6D)

    def lambda_1E85():
        OP_6B(3500, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1E85)

    def lambda_1E95():
        OP_6E(351, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1E95)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #34
        0x102,
        "#1504F#6PWh-What...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x109,
        (
            "#1069F#6PIt's another of the seventy-seven devils!\x02\x03",

            "The other gatekeeper of Gehenna, feared for\x01",
            "its dark incantations and frightful magic!\x02\x03",

            "Astarte of the Abyss!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    LoadEffect(0x0, "map\\mp307_00.eff")
    LoadEffect(0x1, "map\\mp262_00.eff")

    def lambda_1F9C():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1F9C)

    def lambda_1FAC():
        OP_6E(400, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1FAC)
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

    def lambda_2108():
        OP_6D(-1830, 350, 30400, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2108)

    def lambda_2120():
        OP_67(0, 2120, -10000, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2120)

    def lambda_2138():
        OP_6B(3940, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2138)

    def lambda_2148():
        OP_6E(337, 500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2148)
    PlayEffect(0x1, 0x1, 0xFF, 4019, 0, 21890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1B9, 0x0, 0x64)
    OP_22(0x3DC, 0x1, 0x50)
    OP_0D()

    def lambda_2198():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2198)
    Sleep(10)

    def lambda_21B7():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_21B7)
    Sleep(10)

    def lambda_21D6():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_21D6)
    Sleep(10)

    def lambda_21F5():
        OP_9E(0xFE, 0x1E, 0x0, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_21F5)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2269")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_22D0")

    label("loc_2269")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2291")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_22D0")

    label("loc_2291")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22B9")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_22D0")

    label("loc_22B9")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_22D0")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22FD")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2364")

    label("loc_22FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2325")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2364")

    label("loc_2325")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_234D")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2364")

    label("loc_234D")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2364")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23FE")

    ChrTalk(    #36
        0x106,
        "#052F#6PWha...?!\x02",
    )

    CloseMessageWindow()

    label("loc_23FE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_241F")

    ChrTalk(    #37
        0x107,
        "#065F#6PAaah!\x02",
    )

    CloseMessageWindow()

    label("loc_241F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_244B")

    ChrTalk(    #38
        0x10B,
        "#216F#6PWh-What the...?!\x02",
    )

    CloseMessageWindow()

    label("loc_244B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2470")

    ChrTalk(    #39
        0x104,
        "#1543F#6PWha...?!\x02",
    )

    CloseMessageWindow()

    label("loc_2470")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2495")

    ChrTalk(    #40
        0x105,
        "#1381F#6PWha...?!\x02",
    )

    CloseMessageWindow()

    label("loc_2495")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24BA")

    ChrTalk(    #41
        0x10A,
        "#1312F#6PWha...?!\x02",
    )

    CloseMessageWindow()

    label("loc_24BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24DB")

    ChrTalk(    #42
        0x103,
        "#1533F#6PGah!\x02",
    )

    CloseMessageWindow()

    label("loc_24DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24FB")

    ChrTalk(    #43
        0x10E,
        "#177F#6PAgh!\x02",
    )

    CloseMessageWindow()

    label("loc_24FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_251B")

    ChrTalk(    #44
        0x10D,
        "#271F#6PUgh!\x02",
    )

    CloseMessageWindow()

    label("loc_251B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_253F")

    ChrTalk(    #45
        0x108,
        "#077F#6PWha...?!\x02",
    )

    CloseMessageWindow()

    label("loc_253F")


    ChrTalk(    #46
        0x102,
        "#1507F#6PI-Is this Weissmann's Evil Eye?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x109,
        (
            "#1070F#6PIt's gotta be from the curse that was based on--\x01",
            "a far more powerful version that binds space\x01",
            "itself!\x02\x03",

            "Damn it! I can't move a muscle!\x02",
        )
    )

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

    def lambda_2724():
        OP_6D(4000, 2200, 33000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2724)

    def lambda_273C():
        OP_67(0, 1470, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_273C)

    def lambda_2754():
        OP_6B(4660, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2754)

    def lambda_2764():
        OP_6E(290, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2764)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_73(0x1)
    OP_D8(0x1, 0x3E8)

    def lambda_2781():
        OP_8C(0xFE, 200, 200)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2781)
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
            "#1506F#5PUgh... If we can't break out of this,\x01",
            "we're finished!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x109,
        (
            "#1067F#5PGah...\x01",
            "(Don't think I've got a choice here...)\x02",
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
        "Girl's Voice",
        "#5PBegone, foul, blasphemous beast.\x02",
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

    def lambda_2A0B():
        OP_6D(4000, 2000, 35000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A0B)

    def lambda_2A23():
        OP_67(0, 2890, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2A23)

    def lambda_2A3B():
        OP_6B(4000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2A3B)

    def lambda_2A4B():
        OP_6E(300, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A4B)
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

    def lambda_2B51():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_2B51)

    def lambda_2B5F():
        OP_7C(0x1F4, 0x1F4, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2B5F)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_6F(0x1, 121)
    OP_70(0x1, 0x8C)
    OP_82(0x2, 0x0)
    PlayEffect(0x5, 0xFF, 0x11, 2000, 2000, 500, 0, 0, 0, 1000, 1000, 1000, 0x11, 3000, 4000, 1000, 0)
    Sleep(200)

    def lambda_2BC8():
        OP_7C(0x1F4, 0x1F4, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2BC8)
    OP_6F(0x1, 121)
    OP_70(0x1, 0x8C)
    PlayEffect(0x5, 0xFF, 0x11, -1000, 2500, 0, 0, 0, 0, 1000, 1000, 1000, 0x11, 500, 4000, 1000, 0)
    Sleep(200)

    def lambda_2C28():
        OP_7C(0x1F4, 0x1F4, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2C28)
    OP_6F(0x1, 121)
    OP_70(0x1, 0x8C)
    PlayEffect(0x5, 0xFF, 0x11, 1500, 1000, 300, 0, 0, 0, 1000, 1000, 1000, 0x11, 2000, 2500, 1500, 0)
    Sleep(200)

    def lambda_2C88():
        OP_7C(0x1F4, 0x1F4, 0xBB8, 0x64)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2C88)
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

    def lambda_2CF7():
        OP_6D(4000, 0, 25150, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2CF7)

    def lambda_2D0F():
        OP_67(0, 2690, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2D0F)

    def lambda_2D27():
        OP_6B(3520, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2D27)

    def lambda_2D37():
        OP_6E(420, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D37)
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
        "#1504F#5PRies?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x13,
        (
            "#1447F#5PThank goodness... I was worried I might not\x01",
            "make it in time.\x02\x03",

            "#1448FLeave the devil to me. I'll take care of it in\x01",
            "no time.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    LoadEffect(0x2, "craft\\cr04150a.eff")
    LoadEffect(0x3, "craft\\cr04150b.eff")
    LoadEffect(0x4, "monster\\msc0641.eff")

    def lambda_300A():
        OP_6D(8750, 4050, 23090, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_300A)

    def lambda_3022():
        OP_67(0, 4260, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3022)

    def lambda_303A():
        OP_6B(2430, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_303A)

    def lambda_304A():
        OP_6C(120000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_304A)

    def lambda_305A():
        OP_6E(260, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_305A)

    def lambda_306A():

        label("loc_306A")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_306A")

    QueueWorkItem2(0x11, 3, lambda_306A)
    OP_7D(0x0, 0x13, 0x32, 0x1F4)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 5)

    def lambda_308D():
        OP_8E(0xFE, 0x1130, 0xA, 0x3E4E, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_308D)
    WaitChrThread(0x13, 0x1)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_30B2():
        OP_96(0xFE, 0x21FC, 0xDAC, 0x59CE, 0x1770, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_30B2)

    def lambda_30D0():
        OP_8C(0xFE, 315, 0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_30D0)
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

    def lambda_336D():
        OP_7C(0x5DC, 0x5DC, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_336D)
    OP_43(0x11, 0x0, 0x0, 0xF)
    OP_6D(4100, 3100, 29500, 0)
    OP_67(0, 3840, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(324000, 0)
    OP_6E(292, 0)

    def lambda_33C9():
        OP_96(0xFE, 0x1F90, 0x0, 0x62E8, 0x12C, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_33C9)
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

    def lambda_3521():
        OP_6D(2920, 300, 33750, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3521)

    def lambda_3539():
        OP_67(0, 2350, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3539)

    def lambda_3551():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3551)

    def lambda_3561():
        OP_6C(331000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3561)

    def lambda_3571():
        OP_6E(420, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3571)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x2, "battle\\mgaria1.eff")
    LoadEffect(0x3, "magic\\mg052_0.eff")
    LoadEffect(0x5, "Craft\\cr161_00.eff")
    Fade(250)
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)

    def lambda_35E3():

        label("loc_35E3")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_35E3")

    QueueWorkItem2(0x13, 3, lambda_35E3)
    OP_0D()
    Sleep(300)
    PlayEffect(0x0, 0x2, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x109, 0x0)

    def lambda_3636():
        OP_6D(-380, 800, 37550, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3636)

    def lambda_364E():
        OP_67(0, 2080, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_364E)

    def lambda_3666():
        OP_6B(3200, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3666)

    def lambda_3676():
        OP_6C(327000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3676)

    def lambda_3686():
        OP_6E(451, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3686)
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

    def lambda_37CF():
        OP_6D(680, 1250, 33380, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_37CF)

    def lambda_37E7():
        OP_67(0, 5210, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_37E7)

    def lambda_37FF():
        OP_6B(2500, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_37FF)

    def lambda_380F():
        OP_6C(309000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_380F)

    def lambda_381F():
        OP_6E(410, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_381F)

    def lambda_382F():
        OP_8C(0xFE, 200, 200)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_382F)
    OP_D8(0x1, 0x3E8)
    OP_72(0x2001, 0x0)
    ExitThread()
    OP_B0(0x1, 0x1E)
    OP_6F(0x1, 41)
    OP_70(0x1, 0x46)
    Sleep(300)
    OP_22(0xED, 0x0, 0x64)
    OP_43(0x13, 0x0, 0x0, 0x9)

    def lambda_386A():
        OP_6D(700, 1650, 31450, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_386A)

    def lambda_3882():
        OP_67(0, 6030, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3882)

    def lambda_389A():
        OP_6B(2520, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_389A)

    def lambda_38AA():
        OP_6C(333000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_38AA)

    def lambda_38BA():
        OP_6E(405, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38BA)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x109, 0x0)
    LoadEffect(0x0, "magic\\mg011_0.eff")
    LoadEffect(0x2, "monster\\msc1001.eff")
    LoadEffect(0x3, "craft\\cr04150.eff")
    LoadEffect(0x4, "craft\\cr04150a.eff")
    LoadEffect(0x5, "craft\\cr04150b.eff")
    LoadEffect(0x6, "monster\\msc0641.eff")

    def lambda_3952():
        OP_6D(-270, 810, 27940, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3952)

    def lambda_396A():
        OP_67(0, 6810, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_396A)

    def lambda_3982():
        OP_6B(2720, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3982)

    def lambda_3992():
        OP_6C(344000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3992)

    def lambda_39A2():
        OP_6E(423, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39A2)
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

    def lambda_3B2E():
        OP_6D(300, 850, 28290, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3B2E)

    def lambda_3B46():
        OP_67(0, 6210, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3B46)

    def lambda_3B5E():
        OP_6B(2080, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3B5E)

    def lambda_3B6E():
        OP_6C(338000, 1000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3B6E)

    def lambda_3B7E():
        OP_6E(376, 1000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B7E)
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

    def lambda_3D31():
        OP_6B(2700, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3D31)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    PlayEffect(0x6, 0xFF, 0x11, 0, 0, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_3D7C():
        OP_7C(0x5DC, 0x5DC, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3D7C)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F3E")

    ChrTalk(    #53
        0x107,
        "#560F#5PWh-Whoa...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FB2")

    label("loc_3F3E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F64")

    ChrTalk(    #54
        0x105,
        "#1382F#5PWow...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FB2")

    label("loc_3F64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F8C")

    ChrTalk(    #55
        0x10A,
        "#1310F#5PW-Wow...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FB2")

    label("loc_3F8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FB2")

    ChrTalk(    #56
        0x10B,
        "#415F#5PWh-Whoa...\x02",
    )

    CloseMessageWindow()

    label("loc_3FB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FDB")

    ChrTalk(    #57
        0x106,
        "#051F#5PNot bad...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4065")

    label("loc_3FDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4010")

    ChrTalk(    #58
        0x103,
        "#1527F#5PShe's not half bad...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4065")

    label("loc_4010")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_403C")

    ChrTalk(    #59
        0x108,
        "#070F#5PImpressive...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4065")

    label("loc_403C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4065")

    ChrTalk(    #60
        0x10D,
        "#275F#5PImpressive...\x02",
    )

    CloseMessageWindow()

    label("loc_4065")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40BA")

    ChrTalk(    #61
        0x10E,
        (
            "#171F#5PShe's certainly not letting the Gralsritter name\x01",
            "down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_416F")

    label("loc_40BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4115")

    ChrTalk(    #62
        0x104,
        (
            "#1541F#5PHeh. She's certainly not letting the Gralsritter\x01",
            "name down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_416F")

    label("loc_4115")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_416F")

    ChrTalk(    #63
        0x102,
        (
            "#1500F#5PShe's not letting the Gralsritter name down,\x01",
            "that's for sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_416F")


    ChrTalk(    #64
        0x109,
        (
            "#1069F#5PDon't push your luck, Ries!\x02\x03",

            "You know as well as I do that's not an opponent\x01",
            "you can take out on your own!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x13,
        (
            "#1441F#11PI know, but I'm a squire of the Gralsritter.\x01",
            "I have to at least try!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0x13, 7)
    SetChrSubChip(0x13, 0)
    OP_8C(0x13, 45, 0)

    def lambda_425D():
        OP_96(0xFE, 0xFFFFF600, 0x0, 0x60C2, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_425D)
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

    def lambda_4322():
        OP_6D(2090, 750, 26140, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4322)

    def lambda_433A():
        OP_67(0, 5570, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_433A)

    def lambda_4352():
        OP_6B(2720, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4352)

    def lambda_4362():
        OP_6E(357, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4362)
    Sleep(300)

    ChrTalk(    #66
        0x13,
        (
            "#1445F#6PI've got a lot of things that I want to say\x01",
            "to you...\x02",
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

    def lambda_443E():

        label("loc_443E")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_443E")

    QueueWorkItem2(0x13, 3, lambda_443E)
    OP_0D()
    Sleep(300)
    PlayEffect(0x0, 0x2, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #67
        0x13,
        (
            "#1449F#6P...but right now, what I want to do most of\x01",
            "all is protect you!\x02\x03",

            "Just like you and Rufina protected me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x109,
        "#1079F#5P#3S...!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0x0)
    OP_44(0x13, 0x3)
    SetChrChipByIndex(0x13, 10)
    SetChrSubChip(0x13, 1)
    OP_82(0x2, 0x2)
    PlayEffect(0x2, 0x6, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    def lambda_4568():
        OP_67(0, 7430, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4568)

    def lambda_4580():
        OP_6B(2820, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4580)

    def lambda_4590():
        OP_6C(63000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4590)

    def lambda_45A0():
        OP_6E(319, 1500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_45A0)
    PlayEffect(0x3, 0x4, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x11, 0, 0, 0, 0)
    Sleep(2000)

    def lambda_45EA():
        OP_6D(6540, 750, 32090, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_45EA)
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
        "#1802F#5P#10ANo...\x05\x02",
    )

    CloseMessageWindow()

    def lambda_477C():
        OP_8C(0xFE, 225, 600)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_477C)
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

    def lambda_47C0():
        OP_6D(7450, 0, 29880, 1000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_47C0)
    WaitChrThread(0x13, 0x3)
    OP_43(0x13, 0x0, 0x0, 0x7)

    def lambda_47E4():
        OP_7C(0xC8, 0xC8, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_47E4)
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
        "#1069F#6P#3SR-Ries!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_488D():
        OP_6D(3970, 1050, 27530, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_488D)

    def lambda_48A5():
        OP_67(0, 4660, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_48A5)

    def lambda_48BD():
        OP_6B(2950, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_48BD)

    def lambda_48CD():
        OP_6C(233000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_48CD)

    def lambda_48DD():
        OP_6E(422, 2500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_48DD)
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

    def lambda_49D9():
        OP_9E(0xFE, 0xF, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_49D9)
    OP_99(0x13, 0x0, 0x2, 0x1F4)
    Sleep(500)

    ChrTalk(    #71
        0x13,
        "#1804F#5P#50WU...gh...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    WaitChrThread(0x109, 0x0)
    LoadEffect(0x0, "map\\mp261_00.eff")
    LoadEffect(0x3, "map\\mp284_00.eff")
    LoadEffect(0x4, "map\\mp262_01.eff")
    LoadEffect(0x5, "monster\\ms30901b.eff")
    LoadEffect(0x6, "map\\mp283_00.eff")

    def lambda_4A8A():
        OP_6D(2630, 0, 26040, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4A8A)

    def lambda_4AA2():
        OP_67(0, 5600, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4AA2)

    def lambda_4ABA():
        OP_6B(3260, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4ABA)

    def lambda_4ACA():
        OP_6E(422, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4ACA)
    OP_44(0x11, 0x3)

    def lambda_4ADE():
        OP_8C(0xFE, 80, 200)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4ADE)
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
        "#1506F#5PNo!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BA7")

    ChrTalk(    #73
        0x105,
        "#1163F#5PRies!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C7E")

    label("loc_4BA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BCB")

    ChrTalk(    #74
        0x107,
        "#065F#5PRies!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C7E")

    label("loc_4BCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BF0")

    ChrTalk(    #75
        0x10A,
        "#1317F#5PRies!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C7E")

    label("loc_4BF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C15")

    ChrTalk(    #76
        0x104,
        "#1550F#5PRies!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C7E")

    label("loc_4C15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C39")

    ChrTalk(    #77
        0x10E,
        "#177F#5PRies!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C7E")

    label("loc_4C39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C5D")

    ChrTalk(    #78
        0x10B,
        "#214F#5PRies!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C7E")

    label("loc_4C5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C7E")

    ChrTalk(    #79
        0x108,
        "#076F#5PRies!\x02",
    )

    CloseMessageWindow()

    label("loc_4C7E")


    ChrTalk(    #80
        0x109,
        "#1065F#5PUgh...\x02",
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

    def lambda_4D06():

        label("loc_4D06")

        OP_7C(0xC8, 0xC8, 0xBB8, 0x64)
        OP_48()
        Jump("loc_4D06")

    QueueWorkItem2(0x102, 3, lambda_4D06)

    def lambda_4D21():
        OP_6B(2200, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4D21)
    OP_22(0x34F, 0x0, 0x64)
    OP_43(0x109, 0x0, 0x0, 0x6)
    Sleep(1000)

    ChrTalk(    #81 op#A op#5
        0x109,
        "#1069F#4S#5P#20A#60WRaaaaaaaaahhhh!!\x05\x02",
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

    def lambda_4E1A():

        label("loc_4E1A")

        OP_7C(0xC8, 0xC8, 0xBB8, 0x64)
        OP_48()
        Jump("loc_4E1A")

    QueueWorkItem2(0x102, 3, lambda_4E1A)
    Sleep(300)
    OP_22(0x139, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1B3, 0x0, 0x64)
    OP_82(0x1, 0x2)
    PlayEffect(0x4, 0x5, 0xFF, 4019, 0, 21890, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_23(0x3DC)

    def lambda_4E84():
        OP_7C(0x5DC, 0x5DC, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4E84)
    Fade(500)
    OP_6D(1260, 0, 25850, 0)
    OP_67(0, 5250, -10000, 0)
    OP_6B(2520, 0)
    OP_6C(314000, 0)
    OP_6E(395, 0)

    def lambda_4EDE():
        OP_6D(1260, 0, 28000, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4EDE)

    def lambda_4EF6():
        OP_6B(3200, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4EF6)

    def lambda_4F06():
        OP_6E(410, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F06)
    OP_43(0x11, 0x0, 0x0, 0xC)
    WaitChrThread(0x11, 0x0)
    OP_82(0x6, 0x2)
    OP_44(0x102, 0x3)
    OP_23(0x85)

    def lambda_4F2C():
        OP_8C(0xFE, 180, 100)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4F2C)
    Sleep(1000)

    ChrTalk(    #82
        0x102,
        "#1504F#5P?!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #83
        0x13,
        "#1802F#6PK-Kevin...?\x02",
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

    def lambda_4FFD():
        OP_6B(2290, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4FFD)
    WaitChrThread(0x109, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #84
        (
            "\x07\x05Kevin can now use the S-Craft\x01",
            "\x07\x02[Spear of Loa]\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x21E, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #85
        "\x07\x02Spear of Loa\x07\x05 was set as Kevin's S-Break.\x02",
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
            "#1075F#5PHeh...\x02\x03",

            "#1073FI sure wasn't expecting to end up having to use\x01",
            "THIS in here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_51A7():
        OP_6D(2050, 0, 26000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_51A7)

    def lambda_51BF():
        OP_67(0, 5410, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_51BF)

    def lambda_51D7():
        OP_6B(2860, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_51D7)

    def lambda_51E7():
        OP_6E(443, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_51E7)
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
            "#1073F#5PThis is just a formality for a worthless devil like\x01",
            "you...but I hereby acknowledge you as a heretic\x01",
            "to be hunted.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #88
        0x109,
        (
            "#1065F#5PYour chances to repent or beg for the Goddess'\x01",
            "forgiveness have long passed! May a thousand thorns\x01",
            "adorn your flesh with sorrow!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #89
        0x109,
        (
            "#1072F#5P#3SBecome dust, and vanish into the void of\x01",
            "ignorance!\x02",
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

    # Function_5_CED end

    def Function_6_5449(): pass

    label("Function_6_5449")

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

    # Function_6_5449 end

    def Function_7_54C4(): pass

    label("Function_7_54C4")

    SetChrChipByIndex(0x13, 7)
    SetChrSubChip(0x13, 0)

    def lambda_54D4():
        OP_96(0xFE, 0x14F0, 0x0, 0x7788, 0x514, 0x1F40)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_54D4)

    def lambda_54F2():
        OP_9E(0xFE, 0x1E, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_54F2)
    WaitChrThread(0x13, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    SetChrFlags(0x13, 0x20)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x800)
    ClearChrFlags(0x13, 0x2)
    OP_8C(0xFE, 45, 0)
    SetChrChipByIndex(0x13, 13)
    SetChrSubChip(0x13, 0)

    def lambda_553B():
        OP_8F(0xFE, 0x2170, 0x0, 0x7D5A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_553B)

    ChrTalk(    #90 op#A op#5
        0x13,
        "#15A#5PAgh!\x05\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x13, 0x1)
    Return()

    # Function_7_54C4 end

    def Function_8_5568(): pass

    label("Function_8_5568")

    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 45, 0)

    def lambda_5584():
        OP_96(0xFE, 0xFFFFF45C, 0x0, 0x5FD2, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5584)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    Sleep(300)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 3)
    OP_8C(0xFE, 45, 0)

    def lambda_55D1():
        OP_96(0xFE, 0xFFFFF9FC, 0x0, 0x53C0, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_55D1)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    Sleep(400)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 3)
    OP_8C(0xFE, 45, 0)

    def lambda_561E():
        OP_96(0xFE, 0xFFFFFDE4, 0x0, 0x5DD4, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_561E)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 5)

    def lambda_564B():
        OP_8E(0xFE, 0x1FE, 0x0, 0x6996, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_564B)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_8_5568 end

    def Function_9_5670(): pass

    label("Function_9_5670")

    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 5)
    SetChrSubChip(0xFE, 3)

    def lambda_5685():
        OP_96(0xFE, 0xE10, 0x7D0, 0x7724, 0xDAC, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5685)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 2)
    Sleep(100)
    OP_22(0xCB, 0x0, 0x64)

    def lambda_56C1():
        OP_96(0xFE, 0x596, 0x0, 0x693C, 0xBB8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_56C1)
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

    def lambda_57A5():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_57A5)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x5, 0xFF, 0x11, 0, 5000, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_57F9():
        OP_7C(0x5DC, 0x5DC, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_57F9)
    OP_43(0x11, 0x0, 0x0, 0xE)

    def lambda_5818():

        label("loc_5818")

        TurnDirection(0xFE, 0x13, 400)
        OP_48()
        Jump("loc_5818")

    QueueWorkItem2(0x11, 3, lambda_5818)
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

    def lambda_5903():
        OP_96(0xFE, 0xFFFFFD6C, 0x0, 0x65FE, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5903)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 4)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_9_5670 end

    def Function_10_593F(): pass

    label("Function_10_593F")

    SetChrFlags(0xFE, 0x1000)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 5)

    def lambda_5954():
        OP_8E(0xFE, 0x1590, 0x0, 0x6C2A, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5954)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 8)
    SetChrSubChip(0xFE, 2)
    Sleep(100)

    def lambda_5983():
        OP_96(0xFE, 0xD20, 0x0, 0x765C, 0x7D0, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5983)
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

    def lambda_5A65():
        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5A65)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x5, 0xFF, 0x11, 0, 2000, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_5AB9():
        OP_7C(0x5DC, 0x5DC, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_5AB9)
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

    # Function_10_593F end

    def Function_11_5B9C(): pass

    label("Function_11_5B9C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BCA")

    def lambda_5BAB():
        OP_7C(0x1F4, 0x1F4, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_5BAB)
    OP_22(0x280, 0x0, 0x64)
    Sleep(300)
    Jump("Function_11_5B9C")

    label("loc_5BCA")

    Return()

    # Function_11_5B9C end

    def Function_12_5BCB(): pass

    label("Function_12_5BCB")

    OP_22(0x223, 0x0, 0x64)
    OP_82(0x2, 0x2)

    def lambda_5BD9():
        OP_8F(0xFE, 0x1004, 0x1F4, 0x80E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5BD9)

    def lambda_5BF4():
        OP_8C(0xFE, 0, 300)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5BF4)
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

    # Function_12_5BCB end

    def Function_13_5C3D(): pass

    label("Function_13_5C3D")

    OP_22(0x223, 0x0, 0x64)

    def lambda_5C48():
        OP_8F(0xFE, 0x1194, 0x0, 0x86C4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5C48)
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

    # Function_13_5C3D end

    def Function_14_5C99(): pass

    label("Function_14_5C99")

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

    # Function_14_5C99 end

    def Function_15_5CDA(): pass

    label("Function_15_5CDA")

    OP_22(0x223, 0x0, 0x64)

    def lambda_5CE5():
        OP_8F(0xFE, 0xA28, 0x0, 0x80E8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5CE5)
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

    # Function_15_5CDA end

    def Function_16_5D3B(): pass

    label("Function_16_5D3B")

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

    def lambda_5ED4():
        OP_6D(5700, 0, 23300, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5ED4)

    def lambda_5EEC():
        OP_67(0, 5120, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5EEC)

    def lambda_5F04():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5F04)

    def lambda_5F14():
        OP_6E(285, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5F14)
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
        "#1067F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x13,
        "#1802F#5PK-Kevin...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x102,
        "#1502F#11PKevin...\x02",
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

    def lambda_6081():
        OP_6D(5690, 0, 25210, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6081)
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
        "\x07\x05Received \x1F\x5D\x03\x07\x05.\x02",
    )

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
        "#1504F#11POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x109,
        (
            "#1075F#5PHeh. Well at least it gave us something\x01",
            "to justify the trouble.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 2960, 1000, 39000, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x10, 0x4)

    NpcTalk(    #97
        0x10,
        "Hoarse Voice",
        "\x07\x02#2PHaha... Well done, Kevin Graham.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6287")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_62EE")

    label("loc_6287")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62AF")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_62EE")

    label("loc_62AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62D7")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_62EE")

    label("loc_62D7")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_62EE")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_631B")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6382")

    label("loc_631B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6343")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6382")

    label("loc_6343")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_636B")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6382")

    label("loc_636B")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6382")

    Sleep(1000)
    OP_1D(0xB0)

    def lambda_638F():
        OP_6D(4430, 0, 36490, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_638F)

    def lambda_63A7():
        OP_67(0, 5100, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_63A7)

    def lambda_63BF():
        OP_6B(2880, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_63BF)

    def lambda_63CF():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_63CF)

    def lambda_63DF():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_63DF)
    WaitChrThread(0x109, 0x0)
    SetChrPos(0x10, 3200, 0, 36000, 180)
    OP_22(0xBA, 0x1, 0x64)
    PlayEffect(0x0, 0x1, 0x10, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    PlayEffect(0x1, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)

    def lambda_647E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_647E)
    OP_22(0x59, 0x0, 0x64)
    WaitChrThread(0x109, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    OP_23(0xBA)
    Sleep(1500)
    SetChrPos(0x109, 5070, 0, 22060, 0)

    ChrTalk(    #98
        0x109,
        "#1063F#1PYou again...\x02",
    )

    CloseMessageWindow()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x64, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS417._CH")
    OP_C6(0x0, 0x0, 140000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1200)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Lord of Phantasma")

    AnonymousTalk(    #99
        (
            "\x07\x02'Your next destination is the path of beasts.'\x01\x02\x03",

            "Devour the new offering presented to you, and display your seal once more.'\x02\x03",

            "'Then shall the flames of Gehenna burn ever fiercer, and my kingdom draw\x01",
            "closer to its true completion.'\x02\x03",

            "Heh. You didn't perform as well as I hoped, but my words still came true,\x01",
            "did they not?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    Sleep(1000)

    ChrTalk(    #100
        0x109,
        (
            "#1063F#1P...\x02\x03",

            "#1075FJust who are you?\x02\x03",

            "#1060FI think it's about time you took that lame-looking\x01",
            "mask off and showed us your face, don't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x10,
        (
            "\x07\x02#1580F#5PIf that is what you wish, I would be\x01",
            "happy to oblige.\x02\x03",

            "But ask yourself this:\x02\x03",

            "Is that truly what you desire?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x109,
        "#1079F#1PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x10,
        (
            "\x07\x02#1580F#5PYou have but to say the word, and the\x01",
            "deed shall be done.\x02\x03",

            "Well? What's it to be?\x02\x03",

            "Do you wish to see my face?\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x109,
        (
            "#1067F#1P#50W...\x02\x03",

            "#1065FI... I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x13,
        "#1802F#1P...Kevin?\x02",
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

    def lambda_6942():
        OP_6D(5270, 0, 30890, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6942)
    OP_43(0x13, 0x0, 0x0, 0x11)
    WaitChrThread(0x13, 0x0)
    Sleep(500)

    ChrTalk(    #106
        0x13,
        (
            "#1449F#11PThat's enough, Lord of Phantasma!\x02\x03",

            "Stop trying to mess with Kevin's head\x01",
            "with your cryptic nonsense!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10,
        (
            "\x07\x02#1580F#5PHaha... I am doing no such thing.\x02\x03",

            "If he doesn't understand my words,\x01",
            "that is because he chooses not to by\x01",
            "himself.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x13,
        "#1443F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x10,
        (
            "\x07\x02#1580F#5PRegardless, the time has come for the child\x01",
            "of the sun to return to you.\x02\x03",

            "And with that, you will finally have sufficient\x01",
            "pieces for me to prepare some more advanced\x01",
            "game boards for you.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)

    def lambda_6B4F():

        label("loc_6B4F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_6B4F")

    QueueWorkItem2(0x10, 3, lambda_6B4F)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C33")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6C9A")

    label("loc_6C33")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C5B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6C9A")

    label("loc_6C5B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C83")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6C9A")

    label("loc_6C83")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6C9A")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CC7")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6D2E")

    label("loc_6CC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CEF")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6D2E")

    label("loc_6CEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D17")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6D2E")

    label("loc_6D17")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6D2E")

    Sleep(1000)

    ChrTalk(    #110
        0x13,
        "#1441F#11PNo!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x102,
        "#1502F#11PNot again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x10,
        (
            "\x07\x02#1580F#5PHaha. Your next destination is the path of the\x01",
            "dream devils.\x02\x03",

            "Cross between the realms of shadow and light,\x01",
            "and gather the black and white pieces therein.\x02\x03",

            "Only upon the completion of your collection will\x01",
            "your path to yet a new game board become\x01",
            "clear.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_6E7C():

        label("loc_6E7C")

        OP_99(0xFE, 0x8, 0xF, 0x5DC)
        OP_48()
        Jump("loc_6E7C")

    QueueWorkItem2(0x10, 3, lambda_6E7C)
    PlayEffect(0x1, 0x2, 0x10, 0, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_6EC4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_6EC4)
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

    def lambda_6F09():
        OP_6D(6680, 0, 25710, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6F09)

    def lambda_6F21():
        OP_67(0, 4150, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6F21)

    def lambda_6F39():
        OP_6B(2650, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6F39)

    def lambda_6F49():
        OP_6E(340, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_6F49)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F9A")
    OP_62(0xF0, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6FF2")

    label("loc_6F9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FBD")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6FF2")

    label("loc_6FBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FE0")
    OP_62(0xF0, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_6FF2")

    label("loc_6FE0")

    OP_62(0xF0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_6FF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7015")
    OP_62(0xF1, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_706D")

    label("loc_7015")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7038")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_706D")

    label("loc_7038")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_705B")
    OP_62(0xF1, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_706D")

    label("loc_705B")

    OP_62(0xF1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_706D")

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
        "#1067F#5P#11P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x13, 180, 400)
    Sleep(300)

    ChrTalk(    #114
        0x13,
        "#1802F#6PKevin, I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x109,
        (
            "#1065F#11PI know you've got a lot you wanna talk about,\x01",
            "but let's save that until later, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x13,
        "#1444F#6PBut...\x02",
    )

    CloseMessageWindow()

    def lambda_7153():
        OP_6D(6000, 0, 24700, 1300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7153)
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
        "#1504F#11POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x109,
        (
            "#1840F#6PAfter all, it sounds like this contains the girl\x01",
            "we've all been waiting for.\x02\x03",

            "Everything else can wait until after she's out\x01",
            "of this stone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        "#1501F#11PThanks, Kevin.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_731D")

    ChrTalk(    #120
        0x106,
        "#051F#11PHeh. Damn right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_73C8")

    label("loc_731D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_734A")

    ChrTalk(    #121
        0x104,
        "#1541F#11PHah. Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_73C8")

    label("loc_734A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_737D")

    ChrTalk(    #122
        0x108,
        "#070F#11PYeah, you're right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_73C8")

    label("loc_737D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73A4")

    ChrTalk(    #123
        0x10E,
        "#170F#11PIndeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_73C8")

    label("loc_73A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_73C8")

    ChrTalk(    #124
        0x10D,
        "#277F#11PIndeed.\x02",
    )

    CloseMessageWindow()

    label("loc_73C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7409")

    ChrTalk(    #125
        0x107,
        "#066F#11PThank goodness we've found her...\x02",
    )

    CloseMessageWindow()
    Jump("loc_74D0")

    label("loc_7409")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_744B")

    ChrTalk(    #126
        0x105,
        "#1168F#11PThank goodness we've found her...\x02",
    )

    CloseMessageWindow()
    Jump("loc_74D0")

    label("loc_744B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7491")

    ChrTalk(    #127
        0x103,
        "#1527F#11PThank Aidios we've finally found her.\x02",
    )

    CloseMessageWindow()
    Jump("loc_74D0")

    label("loc_7491")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74D0")

    ChrTalk(    #128
        0x10A,
        "#1314F#11PThank goodness we've found her...\x02",
    )

    CloseMessageWindow()

    label("loc_74D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_750C")

    ChrTalk(    #129
        0x10B,
        "#210F#11PWell, I guess that's only fair.\x02",
    )

    CloseMessageWindow()

    label("loc_750C")

    OP_20(0xBB8)

    def lambda_7517():
        OP_6B(4000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7517)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_35(0xE, 0x173)
    OP_A2(0x2504)
    OP_A2(0x250A)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_5D3B end

    def Function_17_7544(): pass

    label("Function_17_7544")

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

    # Function_17_7544 end

    def Function_18_7582(): pass

    label("Function_18_7582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 1)), scpexpr(EXPR_END)), "loc_758A")
    Return()

    label("loc_758A")

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
            "#1004F#6PWhoooa...\x02\x03",

            "I thought I was ready after you guys told\x01",
            "me what happened, but seeing the place\x01",
            "you once trained at like this is...weird.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_775B")

    ChrTalk(    #131
        0x10A,
        (
            "#1310F#6PYou got that right.\x02\x03",

            "#819FI sure wouldn't have wanted to do any\x01",
            "courses here if it looked like this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#1016F#5PAhaha... Same here.\x02",
    )

    CloseMessageWindow()

    label("loc_775B")

    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(    #133
        0x101,
        (
            "#1002F#6PSo this warp thingy here is gonna take us\x01",
            "to the next plane?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x10F,
        (
            "#1446F#6PThat's right. The next should be the fifth.\x02\x03",

            "#1443FPresumably the first of the 'more advanced game\x01",
            "boards' the Lord of Phantasma mentioned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        (
            "#1007F#6PWe're gonna be in for a really tough ride,\x01",
            "aren't we?\x02\x03",

            "#1006FBut hey! We've come through plenty of those\x01",
            "just fine. We can knock this one out, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x10F,
        (
            "#1446F#6PI certainly hope so...\x02\x03",

            "#1445F...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(300)

    ChrTalk(    #137
        0x101,
        "#1011F#5PHmm? Something wrong?\x02",
    )

    CloseMessageWindow()

    def lambda_7954():
        OP_6D(2050, 0, 41200, 800)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_7954)
    OP_8C(0x10F, 270, 400)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)

    ChrTalk(    #138
        0x10F,
        (
            "#1802F#12PNo, but I do have a question.\x02\x03",

            "Why did you specifically put your name\x01",
            "forward to accompany me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        "#1004F#5PHuh? Is it really that big a deal?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x10F,
        (
            "#1446F#12PI can't think of any specific reason you could\x01",
            "have to offer to support me.\x02\x03",

            "And yet when making your request, your eyes\x01",
            "were filled with determination and resolve, so\x01",
            "it wasn't something you did on a whim...\x02\x03",

            "#1440FYou don't mind my inquiry, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1016F#5PNope. It wasn't a whim, though, so you're right\x01",
            "about that. It's just that I don't have some big,\x01",
            "special reason for doing it, either...\x02\x03",

            "#1015FHmm...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #142
        0x101,
        "#1011F#5PI guess I just wanted to give something back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x10F,
        "#1444F#12PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#1012F#5PWell, like, Kevin did a lot for me back during\x01",
            "all that trouble in Liberl.\x02\x03",

            "He bailed me out of trouble more times than\x01",
            "I can count, and he helped Joshua deal with\x01",
            "what was burdening him, too...\x02\x03",

            "#1025FNow he's in trouble just like we were, so...it's\x01",
            "this thing where I found myself wondering\x01",
            "whether there was anything I could do to help.\x02\x03",

            "Coming and backing you up was the best way\x01",
            "I could do that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DF0")

    ChrTalk(    #145
        0x102,
        "#1500F#6PEstelle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E6A")

    label("loc_7DF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E1A")

    ChrTalk(    #146
        0x105,
        "#1382F#6PEstelle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E6A")

    label("loc_7E1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E43")

    ChrTalk(    #147
        0x107,
        "#066F#6PEstelle...\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E6A")

    label("loc_7E43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E6A")

    ChrTalk(    #148
        0x103,
        "#1527F#6PEstelle...\x02",
    )

    CloseMessageWindow()

    label("loc_7E6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E9B")

    ChrTalk(    #149
        0x106,
        "#051F#6PHeh. Now I get it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F2A")

    label("loc_7E9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7ECA")

    ChrTalk(    #150
        0x104,
        "#1545FHeh. Now I get it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F2A")

    label("loc_7ECA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7EFB")

    ChrTalk(    #151
        0x108,
        "#573F#6PHah. Now I get it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F2A")

    label("loc_7EFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F2A")

    ChrTalk(    #152
        0x10A,
        "#1314F#6PHeehee. Now I see.\x02",
    )

    CloseMessageWindow()

    label("loc_7F2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F63")

    ChrTalk(    #153
        0x10E,
        "#179F#6P(...That does make sense.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F99")

    label("loc_7F63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F99")

    ChrTalk(    #154
        0x10D,
        "#278F#6P(...That does make sense.)\x02",
    )

    CloseMessageWindow()

    label("loc_7F99")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FDC")

    ChrTalk(    #155
        0x10B,
        "#413F#6P(She's always been such a darn softie.)\x02",
    )

    CloseMessageWindow()

    label("loc_7FDC")


    ChrTalk(    #156
        0x10F,
        (
            "#1802F#12PI-I'm still not sure that I understand...\x02\x03",

            "I understand that you feel indebted to Kevin,\x01",
            "but how does helping me go towards repaying\x01",
            "that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        (
            "#1004F#5PIsn't that obvious?\x02\x03",

            "You're super important to him, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x10F)
    Sleep(500)

    ChrTalk(    #158
        0x10F,
        "#1444F#12P#3SWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        (
            "#1016F#5PErr, I'm not implying you're going out or anything.\x02\x03",

            "#1025FJust from all I've heard and seen since getting\x01",
            "here, it seems like you basically view each other\x01",
            "as family... I'm not wrong, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x10F,
        (
            "#1445F#12P...No. You're right.\x02\x03",

            "#1446FBefore all of this started, we hadn't met\x01",
            "for almost five whole years.\x02\x03",

            "The only reason we met again at all was\x01",
            "because of work.\x02\x03",

            "#1806FI'm not sure there's any bond between the\x01",
            "two of us at all anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1001F#5PPffft. Yeah, I'm not buying that one.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #162
        0x10F,
        "#1444F#12PWhat's so funny?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#1012F#5P'The connections between people deepen over time\x01",
            "to become bonds, and once such bonds have formed, \x01",
            "they can never be broken.'\x02\x03",

            "'However far apart those people may be, no matter\x01",
            "where life may take them, those bonds will always\x01",
            "exist in some way.'\x02\x03",

            "#1006FNot my words, by the way. They're just something\x01",
            "some old guy I know said to me a while back.\x02\x03",

            "And I happen to agree with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x10F,
        "#1444F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        (
            "#1011F#5PKevin was happy to entrust everything to you\x01",
            "without a second thought, right?\x02\x03",

            "You were talking like you knew what he was \x01",
            "thinking earlier, too. About how he was going\x01",
            "to tell us about his Stigma.\x02\x03",

            "#1012FThat's proof enough there's still a strong bond\x01",
            "between you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x10F,
        (
            "#1445F#12P...\x02\x03",

            "#1446FI wish I could be so confident.\x02\x03",

            "#1806FStill, I can understand why you\x01",
            "wanted to come with me now.\x02\x03",

            "I appreciate it, too. Thank you,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        "#1016F#5PYou're very welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x10F,
        (
            "#1446F#12PI do have one more question, though...\x02\x03",

            "It's something of a personal one, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        (
            "#1004F#5PHmm? Like what?\x02\x03",

            "#1006FI'll answer it if I can. This is a good chance\x01",
            "to get to know each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x10F,
        (
            "#1447F#12PAll right. Forgive me if this sounds blunt, but...\x02\x03",

            "#1448F...do people often tell you that you're too soft\x01",
            "for your own good?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #171
        0x101,
        "#1004F#5PWha...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_886D")

    ChrTalk(    #172
        0x10B,
        "#210F#6P(Heheh! Bingo.)\x02",
    )

    CloseMessageWindow()

    label("loc_886D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8891")

    ChrTalk(    #173
        0x102,
        "#1514F#6PHaha...\x02",
    )

    CloseMessageWindow()

    label("loc_8891")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88B7")

    ChrTalk(    #174
        0x105,
        "#1165F#6PHeehee...\x02",
    )

    CloseMessageWindow()

    label("loc_88B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88DC")

    ChrTalk(    #175
        0x107,
        "#067F#6PHeehee...\x02",
    )

    CloseMessageWindow()

    label("loc_88DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8902")

    ChrTalk(    #176
        0x103,
        "#1521F#6PHeehee...\x02",
    )

    CloseMessageWindow()

    label("loc_8902")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8922")

    ChrTalk(    #177
        0x106,
        "#051F#6PHeh.\x02",
    )

    CloseMessageWindow()

    label("loc_8922")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8943")

    ChrTalk(    #178
        0x104,
        "#1541F#6PHah.\x02",
    )

    CloseMessageWindow()

    label("loc_8943")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8968")

    ChrTalk(    #179
        0x108,
        "#071F#6PHahaha...\x02",
    )

    CloseMessageWindow()

    label("loc_8968")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_898A")

    ChrTalk(    #180
        0x10A,
        "#819F#6PAhaha!\x02",
    )

    CloseMessageWindow()

    label("loc_898A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89AD")

    ChrTalk(    #181
        0x10E,
        "#171F#6PHaha...\x02",
    )

    CloseMessageWindow()

    label("loc_89AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89CF")

    ChrTalk(    #182
        0x10D,
        "#275F#6PHeh...\x02",
    )

    CloseMessageWindow()

    label("loc_89CF")

    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_8C(0x101, 135, 400)
    Sleep(300)

    ChrTalk(    #183
        0x101,
        "#1019F#5PWh-What're you laughing for?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x10F,
        "#1447F#12PI think I have my answer.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Sleep(300)

    ChrTalk(    #185
        0x101,
        (
            "#1007F#5PAt least let me answer before making\x01",
            "up your mind...\x02\x03",

            "#1008FAhhh, screw it. Let's get going!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x10F,
        "#1448F#12PRight behind you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2A01)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_18_7582 end

    def Function_19_8AEA(): pass

    label("Function_19_8AEA")

    OP_8C(0xFE, 270, 400)
    Sleep(300)
    OP_8C(0xFE, 45, 400)
    Sleep(300)
    OP_8C(0xFE, 315, 400)
    Sleep(300)
    Return()

    # Function_19_8AEA end

    def Function_20_8B0F(): pass

    label("Function_20_8B0F")

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

    def lambda_8C1D():
        OP_6D(3650, 0, 44180, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_8C1D)

    def lambda_8C35():
        OP_67(0, 7530, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_8C35)

    def lambda_8C4D():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_8C4D)

    def lambda_8C5D():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_8C5D)

    def lambda_8C6D():
        OP_6E(241, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C6D)
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

    # Function_20_8B0F end

    def Function_21_8CA6(): pass

    label("Function_21_8CA6")

    ClearMapFlags(0x2000000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_8CC9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8CDA")

    label("loc_8CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_8CDA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8CDA")

    SetMapFlags(0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_8CFF"),
        (1, "loc_8D2E"),
        (2, "loc_8D5D"),
        (SWITCH_DEFAULT, "loc_8D8C"),
    )


    label("loc_8CFF")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP001._CH")
    Jump("loc_8D8C")

    label("loc_8D2E")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP002._CH")
    Jump("loc_8D8C")

    label("loc_8D5D")

    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_MAP003._CH")
    Jump("loc_8D8C")

    label("loc_8D8C")

    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8DC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_90C6")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_8DEC"),
        (1, "loc_8E18"),
        (2, "loc_8E59"),
        (SWITCH_DEFAULT, "loc_8EAD"),
    )


    label("loc_8DEC")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",          # 0
            "[Balstar Channel]\x01",      # 1
        )
    )

    Jump("loc_8EAD")

    label("loc_8E18")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",             # 0
            "[Balstar Channel]\x01",         # 1
            "[Saint-Croix Forest]\x01",      # 2
        )
    )

    Jump("loc_8EAD")

    label("loc_8E59")


    Menu(
        0,
        30,
        80,
        0,
        (
            "[Guild Lodge]\x01",             # 0
            "[Balstar Channel]\x01",         # 1
            "[Saint-Croix Forest]\x01",      # 2
            "[Grimsel Fortress]\x01",        # 3
        )
    )

    Jump("loc_8EAD")

    label("loc_8EAD")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8ED7"),
        (1, "loc_8F4E"),
        (2, "loc_8FC9"),
        (3, "loc_9047"),
        (SWITCH_DEFAULT, "loc_90C3"),
    )


    label("loc_8ED7")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #187
        "\x07\x05Travel to [Guild Lodge]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8F3B"),
        (1, "loc_8F48"),
        (SWITCH_DEFAULT, "loc_8F4B"),
    )


    label("loc_8F3B")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F4B")

    label("loc_8F48")

    Jump("loc_8F4B")

    label("loc_8F4B")

    Jump("loc_90C3")

    label("loc_8F4E")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #188
        "\x07\x05Travel to [Balstar Channel]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8FB6"),
        (1, "loc_8FC3"),
        (SWITCH_DEFAULT, "loc_8FC6"),
    )


    label("loc_8FB6")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8FC6")

    label("loc_8FC3")

    Jump("loc_8FC6")

    label("loc_8FC6")

    Jump("loc_90C3")

    label("loc_8FC9")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #189
        "\x07\x05Travel to [Saint-Croix Forest]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9034"),
        (1, "loc_9041"),
        (SWITCH_DEFAULT, "loc_9044"),
    )


    label("loc_9034")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9044")

    label("loc_9041")

    Jump("loc_9044")

    label("loc_9044")

    Jump("loc_90C3")

    label("loc_9047")

    SetChrName("")
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #190
        "\x07\x05Travel to [Grimsel Fortress]?\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        -1,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_90B0"),
        (1, "loc_90BD"),
        (SWITCH_DEFAULT, "loc_90C0"),
    )


    label("loc_90B0")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_90C0")

    label("loc_90BD")

    Jump("loc_90C0")

    label("loc_90C0")

    Jump("loc_90C3")

    label("loc_90C3")

    Jump("loc_8DC1")

    label("loc_90C6")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_90DF"),
        (1, "loc_9113"),
        (2, "loc_9147"),
        (3, "loc_917B"),
        (SWITCH_DEFAULT, "loc_91AF"),
    )


    label("loc_90DF")

    OP_C6(0x0, 0x0, -640000, 0, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_91AF")

    label("loc_9113")

    OP_C6(0x0, 0x0, -358000, -37000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_91AF")

    label("loc_9147")

    OP_C6(0x0, 0x0, -362000, -266000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_91AF")

    label("loc_917B")

    OP_C6(0x0, 0x0, -64000, -340000, 2000)
    OP_C6(0x0, 0x1, 2000, 2000, 2000)
    OP_C6(0x0, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    Jump("loc_91AF")

    label("loc_91AF")

    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_91D1"),
        (1, "loc_91DD"),
        (2, "loc_91E9"),
        (3, "loc_91F5"),
        (SWITCH_DEFAULT, "loc_9201"),
    )


    label("loc_91D1")

    NewScene("ED6_DT21/U5102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_9201")

    label("loc_91DD")

    NewScene("ED6_DT21/M5503   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_9201")

    label("loc_91E9")

    NewScene("ED6_DT21/M5507   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_9201")

    label("loc_91F5")

    NewScene("ED6_DT21/M5508   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_9201")

    label("loc_9201")

    Return()

    # Function_21_8CA6 end

    def Function_22_9202(): pass

    label("Function_22_9202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9213")
    Call(0, 2)
    Return()

    label("loc_9213")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_22_9202 end

    def Function_23_92F1(): pass

    label("Function_23_92F1")

    OP_DE(0x0, 0x4, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_23_92F1 end

    def Function_24_93CF(): pass

    label("Function_24_93CF")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_24_93CF end

    def Function_25_948B(): pass

    label("Function_25_948B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_949C")
    Call(0, 20)
    Return()

    label("loc_949C")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_25_948B end

    def Function_26_9558(): pass

    label("Function_26_9558")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9581")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_9575():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9575)

    label("loc_9581")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95AA")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_959E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_959E)

    label("loc_95AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95D3")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_95C7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_95C7)

    label("loc_95D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_95FC")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_95F0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_95F0)

    label("loc_95FC")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9628")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_9628")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_963F")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_963F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9656")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_9656")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_966D")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_966D")

    Return()

    # Function_26_9558 end

    def Function_27_966E(): pass

    label("Function_27_966E")


    def lambda_9674():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9674)

    def lambda_9686():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_9686)

    def lambda_9698():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_9698)

    def lambda_96AA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_96AA)
    Sleep(1000)
    Return()

    # Function_27_966E end

    def Function_28_96BC(): pass

    label("Function_28_96BC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #191
        "\x07\x05Le Locle Training Center\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_28_96BC end

    SaveToFile()

Try(main)
