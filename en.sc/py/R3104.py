from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3104   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3104.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60029",
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
        'Tratt Plains Road',                    # 9
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


    DeclNpc(
        X                   = 50,
        Z                   = -130,
        Y                   = -59690,
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


    DeclEvent(
        X                   = -2800,
        Y                   = -2000,
        Z                   = -54300,
        Range               = 2800,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFF3030,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -16800,
        Y                   = -5000,
        Z                   = -24500,
        Range               = 14800,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFFAB3C,
        Unknown_18          = 0x0,
        Unknown_1C          = 4,
    )

    DeclEvent(
        X                   = -2700,
        Y                   = -6100,
        Z                   = -8640,
        Range               = 2700,
        Unknown_10          = 0x2710,
        Unknown_14          = 0xFFFFECDC,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )


    ScpFunction(
        "Function_0_12A",          # 00, 0
        "Function_1_1D8",          # 01, 1
        "Function_2_344",          # 02, 2
        "Function_3_5B5",          # 03, 3
        "Function_4_689",          # 04, 4
        "Function_5_BD2",          # 05, 5
        "Function_6_CF3",          # 06, 6
        "Function_7_D78",          # 07, 7
        "Function_8_DFD",          # 08, 8
        "Function_9_E82",          # 09, 9
        "Function_10_F07",         # 0A, 10
        "Function_11_F8D",         # 0B, 11
        "Function_12_101A",        # 0C, 12
        "Function_13_11E3",        # 0D, 13
        "Function_14_1249",        # 0E, 14
        "Function_15_12AF",        # 0F, 15
        "Function_16_1315",        # 10, 16
    )


    def Function_0_12A(): pass

    label("Function_0_12A")

    OP_A3(0x1580)
    OP_A3(0x1581)
    OP_A3(0x1582)
    OP_A3(0x1583)
    OP_A3(0x1584)
    OP_A3(0x1585)
    OP_A3(0x1586)
    OP_A3(0x1587)
    OP_A3(0x1588)
    OP_A3(0x1589)
    OP_A3(0x158A)
    OP_A3(0x158B)
    OP_A3(0x158C)
    OP_A3(0x158D)
    OP_A3(0x158E)
    OP_A3(0x158F)
    OP_A3(0x1590)
    OP_A3(0x1591)
    OP_A3(0x1592)
    OP_A3(0x1593)
    OP_A3(0x1594)
    OP_A3(0x1EB5)
    OP_A3(0x1EB6)
    OP_A3(0x1EB7)
    OP_A3(0x1EB8)
    OP_A3(0x1EB9)
    OP_A3(0x1EBA)
    OP_A3(0x1EBB)
    OP_A3(0x1EBC)
    OP_A3(0x1EBD)
    OP_A3(0x1EBE)
    OP_A3(0x1EBF)
    OP_A3(0x1EC0)
    OP_A3(0x1EC1)
    OP_A3(0x1EC2)
    OP_A3(0x1EC3)
    OP_A3(0x1EC4)
    OP_A3(0x1EC5)
    OP_A3(0x1EC6)
    OP_A3(0x1EC7)
    OP_A3(0x1EC8)
    OP_A3(0x1EC9)
    OP_A3(0x1ECA)
    OP_A3(0x1ECB)
    OP_A3(0x1ECC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1C7")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)
    Jump("loc_1D7")

    label("loc_1C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D7")
    Event(0, 12)

    label("loc_1D7")

    Return()

    # Function_0_12A end

    def Function_1_1D8(): pass

    label("Function_1_1D8")

    OP_16(0x2, 0xFA0, 0xFFFE0048, 0xFFFE13D0, 0x230031)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_204")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_204")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_216")
    OP_10(0x0, 0x0)
    OP_10(0x2, 0x1)

    label("loc_216")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_225")
    Jump("loc_275")

    label("loc_225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_275")
    LoadEffect(0x0, "map\\\\mp086_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 0, 6000, -8100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_275")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28E")
    OP_10(0x1, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_294")

    label("loc_28E")

    OP_10(0x1, 0x1)
    OP_10(0x3, 0x0)

    label("loc_294")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_343")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x1C), scpexpr(EXPR_PUSH_LONG, 0x5B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_343")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_343")
    OP_CE(0x0, (scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2F2")
    OP_28(0x6E, 0x1, 0x40)
    Jump("loc_343")

    label("loc_2F2")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_307")
    OP_28(0x6E, 0x1, 0x20)
    Jump("loc_343")

    label("loc_307")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31C")
    OP_28(0x6E, 0x1, 0x10)
    Jump("loc_343")

    label("loc_31C")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_331")
    OP_28(0x6E, 0x1, 0x8)
    Jump("loc_343")

    label("loc_331")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_343")
    OP_28(0x6E, 0x1, 0x4)

    label("loc_343")

    Return()

    # Function_1_1D8 end

    def Function_2_344(): pass

    label("Function_2_344")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_523")
    OP_6D(310, -60, -23970, 0)
    OP_67(0, 9550, -10000, 0)
    OP_6B(3990, 0)
    OP_6C(45000, 0)
    OP_6E(298, 0)
    SetChrPos(0x101, 900, -70, -55000, 0)
    SetChrPos(0x102, -400, -160, -55410, 0)
    SetChrPos(0x108, 720, -80, -56490, 0)
    SetChrPos(0xF9, -570, -130, -56740, 0)

    def lambda_3D5():
        OP_6D(730, -60, -45850, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D5)
    OP_C8(0x200, 0x46, "C_PLAC20._CH", 0x0, 0x3E8)
    OP_DE("Carnelia Tower")
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_421():
        OP_8E(0xFE, 0x47E, 0xFFFFFFCE, 0xFFFF47D2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_421)

    def lambda_43C():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFFB0, 0xFFFF46B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_43C)

    def lambda_457():
        OP_8E(0xFE, 0x4F6, 0xFFFFFFC4, 0xFFFF428C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_457)

    def lambda_472():
        OP_8E(0xFE, 0xFFFFFEB6, 0xFFFFFF92, 0xFFFF40A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_472)
    WaitChrThread(0x101, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-120, -90, -48500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)
    SetChrPos(0x0, -120, -90, -48500, 0)
    SetChrPos(0x1, -120, -90, -48500, 0)
    SetChrPos(0x2, -120, -90, -48500, 0)
    SetChrPos(0x3, -120, -90, -48500, 0)
    OP_A2(0x1E0C)
    Jump("loc_5A4")

    label("loc_523")

    OP_6D(-120, -90, -48500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -120, -90, -48500, 0)
    SetChrPos(0x1, -120, -90, -48500, 0)
    SetChrPos(0x2, -120, -90, -48500, 0)
    SetChrPos(0x3, -120, -90, -48500, 0)

    label("loc_5A4")

    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_344 end

    def Function_3_5B5(): pass

    label("Function_3_5B5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C7")
    Return()

    label("loc_5C7")

    EventBegin(0x1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Return to the Arseille?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Return]\x01",            # 0
            "[Don't Return]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_668")
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0301   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_688")

    label("loc_668")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_688")

    Return()

    # Function_3_5B5 end

    def Function_4_689(): pass

    label("Function_4_689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_696")
    Return()

    label("loc_696")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BB")
    Call(0, 10)
    Call(0, 11)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_6BB")

    Fade(1000)
    OP_6D(-250, 2650, -14410, 0)
    OP_67(0, 2730, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(9000, 0)
    OP_6E(572, 0)
    SetChrPos(0x101, 900, 250, -20540, 0)
    SetChrPos(0x102, -520, 250, -20720, 0)
    SetChrPos(0x108, 800, -90, -22200, 0)
    SetChrPos(0xF9, -570, -90, -22350, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #1
        0x101,
        (
            "#1002F#2PJust like the Esmelas Tower...\x02\x03",

            "Is this going to connect\x01",
            "to that weird place too?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_84A")

    ChrTalk(    #2
        0x106,
        (
            "#057F#5PThat weird place, that...'shadow' tower's\x01",
            "gotta be the real form of this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        "#1042F#5PYes... I think that's all but certain.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0B")

    label("loc_84A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FD")

    ChrTalk(    #4
        0x103,
        (
            "#022F#5PAs 'weird' as it may seem to us,\x01",
            "I suspect the 'shadow tower' is\x01",
            "the real form of these places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        "#1042F#5PYes... I think that's all but certain.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0B")

    label("loc_8FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AA")

    ChrTalk(    #6
        0x109,
        (
            "#1063F#5PActually, weird as it is, I think that\x01",
            "'shadow tower' is what these things\x01",
            "actually ARE.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        "#1042F#5PYes... I think that's all but certain.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0B")

    label("loc_9AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A63")

    ChrTalk(    #8
        0x105,
        (
            "#043F#5PTerrible as they are, I cannot help\x01",
            "but think the 'shadow' towers are\x01",
            "the true forms of the towers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        "#1042F#5PYes... I think that's all but certain.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0B")

    label("loc_A63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B0B")

    ChrTalk(    #10
        0x107,
        (
            "#065F#5PIt's scary, but I think the 'shadow\x01",
            "tower' is what the tower's really\x01",
            "supposed to be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        "#1042F#5PYes... I think that's all but certain.\x02",
    )

    CloseMessageWindow()

    label("loc_B0B")


    ChrTalk(    #12
        0x108,
        (
            "#070FNo matter what it is, I doubt our\x01",
            "task will be straightforward.\x02\x03",

            "Stay alert, everyone.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B72():
        OP_69(0x0, 0x7D0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_B72)

    def lambda_B80():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B80)

    def lambda_B98():
        OP_6B(3250, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_B98)

    def lambda_BA8():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_BA8)

    def lambda_BB8():
        OP_6E(262, 2000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_BB8)
    OP_A2(0x1E0D)
    WaitChrThread(0x0, 0x0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_4_689 end

    def Function_5_BD2(): pass

    label("Function_5_BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CF2")
    EventBegin(0x0)
    Fade(500)
    ClearMapFlags(0x1)
    OP_6D(-250, 2650, -14410, 0)
    OP_67(0, 2730, -10000, 0)
    OP_6B(3540, 0)
    OP_6C(9000, 0)
    OP_6E(403, 0)
    OP_6D(290, 3850, -6790, 0)
    OP_67(0, 2730, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(9000, 0)
    OP_6E(403, 0)
    SetChrPos(0x101, 620, 3850, -11000, 0)
    SetChrPos(0x102, -750, 3850, -11000, 0)
    SetChrPos(0x108, 550, 3450, -12660, 0)
    SetChrPos(0xF9, -1000, 3450, -12540, 0)
    OP_0D()
    OP_43(0x101, 0x0, 0x0, 0x6)
    Sleep(300)
    OP_43(0x102, 0x0, 0x0, 0x7)
    Sleep(300)
    OP_43(0x108, 0x0, 0x0, 0x8)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x0, 0x9)
    WaitChrThread(0x3, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/C3600   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_CF2")

    Return()

    # Function_5_BD2 end

    def Function_6_CF3(): pass

    label("Function_6_CF3")

    OP_91(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_D38():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D38)

    def lambda_D52():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D52)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_6_CF3 end

    def Function_7_D78(): pass

    label("Function_7_D78")

    OP_91(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_DBD():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DBD)

    def lambda_DD7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DD7)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_7_D78 end

    def Function_8_DFD(): pass

    label("Function_8_DFD")

    OP_91(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_E42():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E42)

    def lambda_E5C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E5C)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_8_DFD end

    def Function_9_E82(): pass

    label("Function_9_E82")

    OP_91(0xFE, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x1)
    OP_7D(0x0, 0xFE, 0x32, 0x1F4)
    OP_22(0x99, 0x0, 0x64)
    SetChrFlags(0xFE, 0x4)
    OP_91(0xFE, 0x0, 0x1F4, 0x0, 0x0, 0x0)

    def lambda_EC7():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EC7)

    def lambda_EE1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_EE1)
    WaitChrThread(0xFE, 0x1)
    OP_91(0xFE, 0x0, 0x9C4, 0x0, 0x1388, 0x0)
    Return()

    # Function_9_E82 end

    def Function_10_F07(): pass

    label("Function_10_F07")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F80"),
        (1, "loc_F86"),
        (SWITCH_DEFAULT, "loc_F8C"),
    )


    label("loc_F80")

    OP_A2(0x1200)
    Jump("loc_F8C")

    label("loc_F86")

    OP_A2(0x1201)
    Jump("loc_F8C")

    label("loc_F8C")

    Return()

    # Function_10_F07 end

    def Function_11_F8D(): pass

    label("Function_11_F8D")

    FadeToDark(0, 0, -1)
    OP_6D(55450, 4000, 13070, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_11_F8D end

    def Function_12_101A(): pass

    label("Function_12_101A")

    EventBegin(0x0)
    OP_6D(-250, 2650, -14410, 0)
    OP_67(0, 2730, -10000, 0)
    OP_6B(3540, 0)
    OP_6C(9000, 0)
    OP_6E(403, 0)
    OP_6D(290, 3850, -6790, 0)
    OP_67(0, 2730, -10000, 0)
    OP_6B(2670, 0)
    OP_6C(9000, 0)
    OP_6E(403, 0)
    SetChrPos(0x101, 500, 4400, -7730, 180)
    SetChrPos(0x102, -500, 4400, -7730, 180)
    SetChrPos(0xF8, 500, 4400, -7730, 180)
    SetChrPos(0xF9, -500, 4400, -7730, 180)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    OP_43(0x101, 0x0, 0x0, 0xD)
    Sleep(800)
    OP_43(0x102, 0x0, 0x0, 0xE)
    Sleep(800)
    OP_43(0xF8, 0x0, 0x0, 0xF)
    Sleep(800)
    OP_43(0xF9, 0x0, 0x0, 0x10)
    WaitChrThread(0xF9, 0x0)
    Fade(500)
    OP_6D(-120, 3850, -10670, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -120, 3850, -10670, 180)
    SetChrPos(0x1, -120, 3850, -10670, 180)
    SetChrPos(0x2, -120, 3850, -10670, 180)
    SetChrPos(0x3, -120, 3850, -10670, 180)
    OP_0D()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_12_101A end

    def Function_13_11E3(): pass

    label("Function_13_11E3")

    OP_22(0x99, 0x0, 0x64)

    def lambda_11EE():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11EE)

    def lambda_1208():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1208)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_1229():
        OP_8F(0xFE, 0x1F4, 0xFA0, 0xFFFFD6FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1229)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_13_11E3 end

    def Function_14_1249(): pass

    label("Function_14_1249")

    OP_22(0x99, 0x0, 0x64)

    def lambda_1254():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1254)

    def lambda_126E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_126E)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_128F():
        OP_8F(0xFE, 0xFFFFFE0C, 0xFA0, 0xFFFFD6FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_128F)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_14_1249 end

    def Function_15_12AF(): pass

    label("Function_15_12AF")

    OP_22(0x99, 0x0, 0x64)

    def lambda_12BA():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12BA)

    def lambda_12D4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12D4)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_12F5():
        OP_8F(0xFE, 0x1F4, 0xE10, 0xFFFFDAE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12F5)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_15_12AF end

    def Function_16_1315(): pass

    label("Function_16_1315")

    OP_22(0x99, 0x0, 0x64)

    def lambda_1320():
        OP_9E(0xFE, 0x0, 0x64, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1320)

    def lambda_133A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_133A)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1)
    WaitChrThread(0xFE, 0x1)

    def lambda_135B():
        OP_8F(0xFE, 0xFFFFFE0C, 0xE10, 0xFFFFDAE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_135B)
    WaitChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_16_1315 end

    SaveToFile()

Try(main)
