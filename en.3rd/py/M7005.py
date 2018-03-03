from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Strange Man',                          # 9
        'Bennu',                                # 10
        'Sudorudo',                             # 11
        'Sudorudo',                             # 12
        'Sudorudo',                             # 13
        'Sudorudo',                             # 14
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
        "Function_3_8FD",          # 03, 3
        "Function_4_912",          # 04, 4
        "Function_5_92C",          # 05, 5
        "Function_6_946",          # 06, 6
        "Function_7_960",          # 07, 7
        "Function_8_971",          # 08, 8
        "Function_9_11A0",         # 09, 9
        "Function_10_11DE",        # 0A, 10
        "Function_11_1297",        # 0B, 11
        "Function_12_1350",        # 0C, 12
        "Function_13_1409",        # 0D, 13
        "Function_14_14C2",        # 0E, 14
        "Function_15_287E",        # 0F, 15
        "Function_16_28AC",        # 10, 16
        "Function_17_28DA",        # 11, 17
        "Function_18_2908",        # 12, 18
        "Function_19_2931",        # 13, 19
        "Function_20_2953",        # 14, 20
        "Function_21_2AAF",        # 15, 21
        "Function_22_2C1D",        # 16, 22
        "Function_23_2F11",        # 17, 23
        "Function_24_3049",        # 18, 24
        "Function_25_32CB",        # 19, 25
        "Function_26_33A9",        # 1A, 26
        "Function_27_3489",        # 1B, 27
        "Function_28_359F",        # 1C, 28
        "Function_29_35ED",        # 1D, 29
        "Function_30_36F4",        # 1E, 30
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
        "#1444F#6PThis isn't good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        "#1063F#6PNoticed it, too, huh?\x02",
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
        "#064F#6PNoticed what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10E,
        (
            "#172FDo you sense monsters? I can't feel anything\x01",
            "of the sort...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_668():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_668)
    Sleep(100)
    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #4
        0x109,
        (
            "#1067F#5PThat's normal. I doubt anyone who isn't part of\x01",
            "the church would recognize what's going on.\x02\x03",

            "#1063FIt's a peculiar kind of rotting smell... The scent\x01",
            "of the underworld.\x02\x03",

            "It's faint, but it's there, and it's coming from the\x01",
            "area up ahead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        (
            "#1445F#5PWhatever is lying in wait for us, it's going to be\x01",
            "unlike any of the other fiends we have fought up\x01",
            "till this point.\x02\x03",

            "#1443FWe're going to need to be exceptionally careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x107,
        "#065F#6PUh-oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10E,
        (
            "#176FThat's unfortunate...\x02\x03",

            "#178FStill, if we intend to proceed with our investigation,\x01",
            "we have no choice but to advance, whatever may\x01",
            "stand in our way.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x261C)
    OP_28(0x2A, 0x1, 0x8)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_2_356 end

    def Function_3_8FD(): pass

    label("Function_3_8FD")

    OP_8E(0xFE, 0xFFFFFAC4, 0xFFFFF060, 0x2B5C, 0x7D0, 0x0)
    Return()

    # Function_3_8FD end

    def Function_4_912(): pass

    label("Function_4_912")

    Sleep(300)
    OP_8E(0xFE, 0xE6, 0xFFFFF060, 0x2AF8, 0x7D0, 0x0)
    Return()

    # Function_4_912 end

    def Function_5_92C(): pass

    label("Function_5_92C")

    Sleep(800)
    OP_8E(0xFE, 0xFFFFFAA6, 0xFFFFF060, 0x2382, 0x7D0, 0x0)
    Return()

    # Function_5_92C end

    def Function_6_946(): pass

    label("Function_6_946")

    Sleep(1200)
    OP_8E(0xFE, 0x10E, 0xFFFFF060, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_6_946 end

    def Function_7_960(): pass

    label("Function_7_960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 5)), scpexpr(EXPR_END)), "loc_968")
    Return()

    label("loc_968")

    Call(0, 8)
    Call(0, 14)
    Return()

    # Function_7_960 end

    def Function_8_971(): pass

    label("Function_8_971")

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

    def lambda_9F7():
        OP_6D(1060, 0, 71500, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9F7)

    def lambda_A0F():
        OP_67(0, 5020, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_A0F)

    def lambda_A27():
        OP_6B(2860, 6000)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_A27)

    def lambda_A37():
        OP_6E(384, 6000)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_A37)
    Sleep(1000)
    SetChrPos(0x109, -1290, 0, 59520, 0)
    SetChrPos(0x10F, 50, 0, 58970, 0)
    SetChrPos(0x107, -1320, 0, 57630, 0)
    SetChrPos(0x10E, 30, 0, 57000, 0)
    Sleep(1000)

    def lambda_A95():
        OP_8E(0xFE, 0xFFFFFAE2, 0x0, 0x10162, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A95)
    Sleep(50)

    def lambda_AB5():
        OP_8E(0xFE, 0xAA, 0x0, 0x100A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_AB5)
    Sleep(50)

    def lambda_AD5():
        OP_8E(0xFE, 0xFFFFF9C0, 0x0, 0xFB72, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AD5)
    Sleep(100)

    def lambda_AF5():
        OP_8E(0xFE, 0xDC, 0x0, 0xFA96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_AF5)
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
        "#1441F#5PHere it comes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x109,
        "#1069F#6PRight on cue!\x02",
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

    def lambda_D4E():

        label("loc_D4E")

        OP_7C(0x50, 0x50, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_D4E")

    QueueWorkItem2(0x10F, 0, lambda_D4E)

    def lambda_D69():
        OP_6D(0, 0, 78100, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D69)

    def lambda_D81():
        OP_67(0, 4430, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D81)

    def lambda_D99():
        OP_6B(1900, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D99)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x109, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Sleep(1000)

    def lambda_DBE():
        OP_6D(0, 0, 77180, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DBE)

    def lambda_DD6():
        OP_67(0, 5710, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DD6)

    def lambda_DEE():
        OP_6B(2250, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DEE)
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

    def lambda_E3A():
        OP_6D(0, -700, 77000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E3A)

    def lambda_E52():
        OP_67(0, 2600, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E52)

    def lambda_E6A():
        OP_6B(3220, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E6A)

    def lambda_E7A():
        OP_6E(339, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_E7A)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #10
        0x107,
        "#065F#6PI've never seen anything like that before!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10E,
        "#172F#6PWh-What in Aidios' name is that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10F,
        (
            "#1446F#6POne of the seventy-seven devils that appear in the\x01",
            "Testaments. The spiritual coffin that guides the\x01",
            "souls of the dead and serves as Hades' ferryman...\x02\x03",

            "#1441FBennu, the Casket of Sorrow!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        (
            "#1065F#6PWho'd have thought the day would come when I'd\x01",
            "end up coming face to face with a genuine devil?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #14
        0x109,
        (
            "#1069F#6PBring it on! Let me show you what a servant of the\x01",
            "Goddess can do!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_1099():
        OP_6D(0, -400, 77950, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1099)

    def lambda_10B1():
        OP_67(0, 2260, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10B1)

    def lambda_10C9():
        OP_6B(3500, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_10C9)

    def lambda_10D9():
        OP_6E(360, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_10D9)
    PlayEffect(0x2, 0xFF, 0xFF, 0, 100, 75690, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_22(0x32E, 0x0, 0x64)

    def lambda_1123():

        label("loc_1123")

        OP_7C(0x50, 0x50, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1123")

    QueueWorkItem2(0x10F, 0, lambda_1123)
    Sleep(2000)

    def lambda_1143():
        OP_6D(0, -300, 77950, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1143)

    def lambda_115B():
        OP_67(0, 2130, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_115B)

    def lambda_1173():
        OP_6B(2540, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1173)

    def lambda_1183():
        OP_6E(358, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1183)
    WaitChrThread(0x109, 0x0)
    Battle(0x73, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_8_971 end

    def Function_9_11A0(): pass

    label("Function_9_11A0")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 0, -5000, 75400, 180)

    def lambda_11BC():

        label("loc_11BC")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_11BC")

    QueueWorkItem2(0xFE, 1, lambda_11BC)
    OP_8F(0xFE, 0x0, 0x3E8, 0x12688, 0x5DC, 0x0)
    Return()

    # Function_9_11A0 end

    def Function_10_11DE(): pass

    label("Function_10_11DE")

    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, -2800, 100, 73500, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_0D()
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2800, -3000, 73500, 180)

    def lambda_123A():

        label("loc_123A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_123A")

    QueueWorkItem2(0xFE, 1, lambda_123A)
    PlayEffect(0x1, 0x1, 0xFF, -2800, 100, 73500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_8F(0xFE, 0xFFFFF510, 0x0, 0x11F1C, 0x5DC, 0x0)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    Return()

    # Function_10_11DE end

    def Function_11_1297(): pass

    label("Function_11_1297")

    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x2, 0xFF, 2800, 100, 73500, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_0D()
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 2800, -3000, 73500, 180)

    def lambda_12F3():

        label("loc_12F3")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_12F3")

    QueueWorkItem2(0xFE, 1, lambda_12F3)
    PlayEffect(0x1, 0x3, 0xFF, 2800, 100, 73500, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_8F(0xFE, 0xAF0, 0x0, 0x11F1C, 0x5DC, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x3, 0x2)
    Return()

    # Function_11_1297 end

    def Function_12_1350(): pass

    label("Function_12_1350")

    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x4, 0xFF, -2800, 100, 78000, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_0D()
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2800, -3000, 78000, 180)

    def lambda_13AC():

        label("loc_13AC")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13AC")

    QueueWorkItem2(0xFE, 1, lambda_13AC)
    PlayEffect(0x1, 0x5, 0xFF, -2800, 100, 78000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_8F(0xFE, 0xFFFFF510, 0x0, 0x130B0, 0x5DC, 0x0)
    OP_82(0x4, 0x2)
    OP_82(0x5, 0x2)
    Return()

    # Function_12_1350 end

    def Function_13_1409(): pass

    label("Function_13_1409")

    Fade(500)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x6, 0xFF, 2800, 100, 78000, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_0D()
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 2800, -3000, 78000, 180)

    def lambda_1465():

        label("loc_1465")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1465")

    QueueWorkItem2(0xFE, 1, lambda_1465)
    PlayEffect(0x1, 0x7, 0xFF, 2800, 100, 78000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_8F(0xFE, 0xAF0, 0x0, 0x130B0, 0x5DC, 0x0)
    OP_82(0x6, 0x2)
    OP_82(0x7, 0x2)
    Return()

    # Function_13_1409 end

    def Function_14_14C2(): pass

    label("Function_14_14C2")

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
            "\x07\x05Ries learned the S-Craft\x01",
            "\x07\x02[Heavenly Strike]\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x21E, 0x0, 0x64)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #16
        "\x07\x05Set \x07\x02[Heavenly Strike]\x07\x05 as Ries' S-Break?\x18\x02",
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_159C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1603")

    Menu(
        1,
        -1,
        200,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_5F(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_15D7"),
        (SWITCH_DEFAULT, "loc_15EF"),
    )


    label("loc_15D7")

    OP_35(0xE, 0x11A)
    OP_BB(0xE, 0x6, 0x11A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1600")

    label("loc_15EF")

    OP_35(0xE, 0x11A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1600")

    label("loc_1600")

    Jump("loc_159C")

    label("loc_1603")

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

    def lambda_16CF():
        OP_6D(-500, 0, 76480, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_16CF)
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
        "#1070F#5PUgh... *pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10F,
        "#1445F#5PThat...was a real devil...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x107,
        "#562F#5PI-It was terrifying...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10E,
        (
            "#175F#5PThe thought that such fiends exist is...\x01",
            "I don't know what to say...\x02\x03",

            "Just what is this place?\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x10, 0, 0, 94050, 180)
    ClearChrFlags(0x10, 0x80)
    OP_20(0x7D0)

    NpcTalk(    #21
        0x10,
        "Man's Voice",
        (
            "\x07\x05#1PHaha... If that's the best you can do, your future\x01",
            "looks grim indeed.\x07\x00\x02",
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

    def lambda_1901():
        OP_6D(-1160, 0, 92580, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1901)

    def lambda_1919():
        OP_67(0, 5320, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1919)

    def lambda_1931():
        OP_6B(2400, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1931)
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

    def lambda_19AB():
        OP_6B(2150, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_19AB)
    SetChrFlags(0x109, 0x800)
    SetChrFlags(0x10F, 0x800)
    SetChrFlags(0x107, 0x800)
    SetChrFlags(0x107, 0x800)
    OP_0D()
    Sleep(500)

    ChrTalk(    #22
        0x109,
        "#1063F#2P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10F,
        "#1441F#2PIt's that man!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)

    def lambda_1A0F():
        OP_8E(0xFE, 0xFFFFFE98, 0x0, 0x15842, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1A0F)
    OP_6D(-1700, 300, 82800, 0)
    OP_67(0, 3880, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(314000, 0)
    OP_6E(355, 0)

    def lambda_1A67():
        OP_6B(3000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1A67)
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
            "#178F#6PIs he the one you said you saw when\x01",
            "you were first sent here?\x02\x03",

            "#177FWho are you?! Speak your name!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 0x2)
    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #25
        0x10,
        (
            "\x07\x05#1591FHeh...\x02\x03",

            "I believe common decency dictates that\x01",
            "one states their own name before asking\x01",
            "for another's, does it not?\x02\x03",

            "Or perhaps you were aware that I already\x01",
            "know yours, Captain Julia Schwarz?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0x10E,
        "#178F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x109,
        (
            "#1075F#6PWhoever you are, you've done your research.\x02\x03",

            "#1060FWhat do you want with us? Was that devil\x01",
            "we just fought your doing?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #28
        0x109,
        "#1069F#3SIs ALL of this your doing?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "\x07\x05#1591FHeh. Calm yourself, Kevin Graham.\x02\x03",

            "Your suffering is only just beginning.\x02\x03",

            "It's far too early for you to be losing\x01",
            "yourself to despair.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        "#1063F#6PWhat are you talking about...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10F,
        "#1441F#6P...\x02",
    )

    CloseMessageWindow()

    def lambda_1DF8():
        OP_6D(-1300, 300, 88700, 800)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1DF8)

    def lambda_1E10():
        OP_67(0, 3490, -10000, 800)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1E10)

    def lambda_1E28():
        OP_6B(2700, 1000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1E28)

    def lambda_1E38():
        OP_6C(338000, 800)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_1E38)

    def lambda_1E48():
        OP_6E(290, 800)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1E48)
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

    def lambda_1F1E():
        OP_7C(0xC8, 0xC8, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1F1E)
    Sleep(100)
    FadeToBright(100, 16777215)

    def lambda_1F44():
        OP_6D(-450, 200, 85130, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1F44)

    def lambda_1F5C():
        OP_67(0, 3000, -10000, 500)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1F5C)

    def lambda_1F74():
        OP_6B(3200, 2500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1F74)

    def lambda_1F84():
        OP_6C(0, 500)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_1F84)

    def lambda_1F94():
        OP_6E(295, 2500)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1F94)
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
        "#1804F#6PGah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x109,
        "#1069F#6PNow's not the time to be reckless, Ries!\x02",
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

    def lambda_206B():
        OP_6B(3350, 10000)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_206B)

    def lambda_207B():
        OP_6E(300, 10000)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_207B)

    ChrTalk(    #34
        0x10,
        (
            "\x07\x05#1591F#5PA templar sword of the Septian Church, I see.\x02\x03",

            "Your skills aren't bad, but they're still a far\x01",
            "cry from your sister's.\x07\x00\x02",
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
        "#1079F#6PYou know her?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10F,
        "#1802F#6PHow...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "\x07\x05#1591F#5PAll will be revealed in time.\x02\x03",

            "The banquet of despair in this fair land of \x01",
            "Phantasma is only just starting.\x02\x03",

            "My lord wishes to see you suffer--to writhe with\x01",
            "agony, to cry out fruitlessly for your suffering\x01",
            "to end... Do deliver, now, won't you?\x07\x00\x02",
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
        "#1069F#6PW-Wait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10E,
        "#177F#6PYou intend to flee from us?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        (
            "\x07\x05#1590F#5P...I shall tell you one thing before I depart.\x02\x03",

            "My name is Schwarzritter.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    NpcTalk(    #41
        0x10,
        "Schwarzritter",
        (
            "\x07\x05#1591F#5PI am a guardian of Phantasma and loyal servant\x01",
            "of its great lord.\x02\x03",

            "And with that, I bid you farewell.\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2489():
        OP_6D(570, 0, 90330, 1200)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2489)

    def lambda_24A1():
        OP_67(0, 5420, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_24A1)

    def lambda_24B9():
        OP_6B(2420, 1200)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_24B9)

    def lambda_24C9():
        OP_6C(45000, 1200)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_24C9)

    def lambda_24D9():
        OP_6E(365, 1200)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_24D9)
    WaitChrThread(0x109, 0x0)
    OP_43(0x109, 0x0, 0x0, 0xF)
    PlayEffect(0x1, 0x1, 0x10, 0, 500, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    def lambda_252A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_252A)
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
        "#1067F#5PBah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x107,
        "#065F#6PHe disappeared...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10F,
        "#1445F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10E,
        (
            "#176F#6PWe might not have learned much about him\x01",
            "through that encounter, but one thing seems\x01",
            "plain as day.\x02\x03",

            "#178FWe have enemies in this place...and it's not just\x01",
            "the fiends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x109,
        "#1065F#5P...Apparently.\x02",
    )

    CloseMessageWindow()

    def lambda_2701():
        OP_6D(570, 0, 88330, 1200)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2701)

    def lambda_2719():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2719)
    Sleep(100)

    def lambda_272C():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_272C)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #47
        0x109,
        (
            "#1063F#5PAnd what's more, it sounds like they're going\x01",
            "to be hell to deal with.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0xBB8)

    def lambda_27A3():
        OP_6B(3200, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_27A3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x261D)
    OP_44(0x109, 0x2)
    Sleep(3000)
    OP_AD(0x2400ED, 0x0, 0x0, 0x64)
    OP_F7(0x1, 0x0, 0x0)
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
            "[Save]\x01",              # 0
            "[Next Chapter]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2835")
    ShowSaveMenu()

    label("loc_2835")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_14_14C2 end

    def Function_15_287E(): pass

    label("Function_15_287E")

    SetChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 10)
    OP_8E(0xFE, 0xFFFFF93E, 0x0, 0x157F2, 0x1770, 0x0)
    ClearChrFlags(0x109, 0x1000)
    SetChrChipByIndex(0x109, 0)
    SetChrSubChip(0x109, 0)
    Return()

    # Function_15_287E end

    def Function_16_28AC(): pass

    label("Function_16_28AC")

    SetChrFlags(0x10F, 0x1000)
    SetChrChipByIndex(0x10F, 11)
    OP_8E(0xFE, 0x50, 0x0, 0x1572A, 0x1770, 0x0)
    ClearChrFlags(0x10F, 0x1000)
    SetChrChipByIndex(0x10F, 1)
    SetChrSubChip(0x10F, 0)
    Return()

    # Function_16_28AC end

    def Function_17_28DA(): pass

    label("Function_17_28DA")

    SetChrFlags(0x10E, 0x1000)
    SetChrChipByIndex(0x10E, 13)
    OP_8E(0xFE, 0x0, 0x0, 0x14FBE, 0x1770, 0x0)
    ClearChrFlags(0x10F, 0x1000)
    ClearChrFlags(0x10E, 0x1000)
    SetChrChipByIndex(0x10E, 3)
    Return()

    # Function_17_28DA end

    def Function_18_2908(): pass

    label("Function_18_2908")

    SetChrFlags(0x107, 0x1000)
    SetChrChipByIndex(0x107, 12)
    OP_8E(0xFE, 0xFFFFF86C, 0x0, 0x14F14, 0x1770, 0x0)
    ClearChrFlags(0x107, 0x1000)
    SetChrChipByIndex(0x107, 2)
    Return()

    # Function_18_2908 end

    def Function_19_2931(): pass

    label("Function_19_2931")

    SetChrChipByIndex(0x10, 16)
    OP_99(0x10, 0x9, 0xF, 0xDAC)
    SetChrChipByIndex(0x10, 17)
    OP_99(0x10, 0x0, 0x5, 0xDAC)
    OP_22(0x1F9, 0x0, 0x64)
    Return()

    # Function_19_2931 end

    def Function_20_2953(): pass

    label("Function_20_2953")

    SetChrFlags(0xFE, 0x4)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    SetChrFlags(0xFE, 0x1000)
    OP_22(0xCB, 0x0, 0x64)
    OP_8C(0xFE, 0, 0)
    SetChrChipByIndex(0xFE, 11)

    def lambda_297C():
        OP_8F(0xFE, 0xFFFFFED4, 0x0, 0x13E5C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_297C)
    WaitChrThread(0xFE, 0x1)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 2)
    WaitChrThread(0xFE, 0x1)

    def lambda_29AB():
        OP_96(0xFE, 0xFFFFFC18, 0x64, 0x14A78, 0x578, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_29AB)
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

    def lambda_2A88():
        OP_99(0xFE, 0x3, 0x5, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2A88)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_7D(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_20_2953 end

    def Function_21_2AAF(): pass

    label("Function_21_2AAF")

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

    def lambda_2B7B():
        OP_96(0xFE, 0xF0, 0x0, 0x1437A, 0x320, 0x1F40)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2B7B)
    SetChrChipByIndex(0xFE, 19)
    SetChrSubChip(0xFE, 0)
    Sleep(150)
    WaitChrThread(0xFE, 0x1)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 7)
    SetChrSubChip(0xFE, 0)

    def lambda_2BBC():
        OP_99(0xFE, 0x1, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2BBC)

    def lambda_2BCC():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_2BCC)
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

    # Function_21_2AAF end

    def Function_22_2C1D(): pass

    label("Function_22_2C1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 1)), scpexpr(EXPR_END)), "loc_2C25")
    Return()

    label("loc_2C25")

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

    def lambda_2CB4():
        OP_6D(1050, 4250, 132190, 5500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2CB4)

    def lambda_2CCC():
        OP_67(0, 6320, -10000, 5500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2CCC)

    def lambda_2CE4():
        OP_6B(3300, 5500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2CE4)

    def lambda_2CF4():
        OP_6C(45000, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2CF4)

    def lambda_2D04():
        OP_6E(253, 5500)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_2D04)
    Sleep(1000)

    def lambda_2D19():
        OP_8E(0xFE, 0xA, 0x109A, 0x1FE96, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2D19)
    Sleep(200)

    def lambda_2D39():
        OP_8E(0xFE, 0x398, 0x109A, 0x1F9A9, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2D39)
    Sleep(400)

    def lambda_2D59():
        OP_8E(0xFE, 0xFFFFFAF6, 0x109A, 0x1FA40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2D59)
    Sleep(700)

    def lambda_2D79():
        OP_8E(0xFE, 0xFFFFFE70, 0x109A, 0x1F4A9, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_2D79)
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
            "#178F#6PThis is the exit you noticed before, right,\x01",
            "Father? Or entrance, perhaps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x107,
        "#063FIt just like that magic circle at the base.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10F,
        (
            "#1445F...\x02\x03",

            "#1443FDo you think this will take us somewhere\x01",
            "completely new?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x109,
        (
            "#1065F#5PMost likely.\x02\x03",

            "#1063FIt's the only other route I've seen,\x01",
            "so we're just going to have to see where\x01",
            "it takes us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2701)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_22_2C1D end

    def Function_23_2F11(): pass

    label("Function_23_2F11")

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

    def lambda_2F9F():
        OP_6D(790, 4250, 133520, 9000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2F9F)

    def lambda_2FB7():
        OP_6B(2100, 9000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2FB7)

    def lambda_2FC7():
        OP_6C(135000, 9000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_2FC7)
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

    # Function_23_2F11 end

    def Function_24_3049(): pass

    label("Function_24_3049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3118")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(512)
    Sleep(500)
    Jump("loc_311B")

    label("loc_3118")

    TalkBegin(0xFF)

    label("loc_311B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #52
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3157")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_329A")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31B3"),
        (1, "loc_322E"),
        (2, "loc_325C"),
        (SWITCH_DEFAULT, "loc_328A"),
    )


    label("loc_31B3")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    Jump("loc_3297")

    label("loc_322E")

    OP_A9(0x15)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #53
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_3297")

    label("loc_325C")

    OP_A9(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #54
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_3297")

    label("loc_328A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3297")

    label("loc_3297")

    Jump("loc_3157")

    label("loc_329A")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32C7")
    OP_A2(0x2585)
    EventEnd(0x1)
    Jump("loc_32CA")

    label("loc_32C7")

    TalkEnd(0xFF)

    label("loc_32CA")

    Return()

    # Function_24_3049 end

    def Function_25_32CB(): pass

    label("Function_25_32CB")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_25_32CB end

    def Function_26_33A9(): pass

    label("Function_26_33A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33B9")
    Call(0, 23)

    label("loc_33B9")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_347F")
    NewScene("ED6_DT21/U4100   ._SN", 115, 0, 0)
    IdleLoop()
    Jump("loc_3488")

    label("loc_347F")

    NewScene("ED6_DT21/U4150   ._SN", 115, 0, 0)
    IdleLoop()

    label("loc_3488")

    Return()

    # Function_26_33A9 end

    def Function_27_3489(): pass

    label("Function_27_3489")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34B2")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_34A6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_34A6)

    label("loc_34B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34DB")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_34CF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_34CF)

    label("loc_34DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3504")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_34F8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_34F8)

    label("loc_3504")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_352D")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3521():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3521)

    label("loc_352D")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3559")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3559")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3570")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3570")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3587")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_3587")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_359E")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_359E")

    Return()

    # Function_27_3489 end

    def Function_28_359F(): pass

    label("Function_28_359F")


    def lambda_35A5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_35A5)

    def lambda_35B7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_35B7)

    def lambda_35C9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_35C9)

    def lambda_35DB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_35DB)
    Sleep(1000)
    Return()

    # Function_28_359F end

    def Function_29_35ED(): pass

    label("Function_29_35ED")

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

    def lambda_369D():
        OP_6D(10, 5100, -4150, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_369D)

    def lambda_36B5():
        OP_67(0, 11530, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_36B5)

    def lambda_36CD():
        OP_6C(20000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_36CD)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7006   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_35ED end

    def Function_30_36F4(): pass

    label("Function_30_36F4")

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

    def lambda_37B6():
        OP_6D(10, -3850, -4150, 7000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_37B6)

    def lambda_37CE():
        OP_67(0, 8500, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_37CE)

    def lambda_37E6():
        OP_6B(3400, 7000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_37E6)

    def lambda_37F6():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_37F6)
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

    # Function_30_36F4 end

    SaveToFile()

Try(main)
