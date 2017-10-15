from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5317_1 ._SN',
        MapName             = 'Other',
        Location            = 'C5317.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C5317   ._SN',
            'ED6_DT21/C5317_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_3DE6",         # 03, 3
        "Function_4_3E1F",         # 04, 4
        "Function_5_3E7B",         # 05, 5
        "Function_6_3EBF",         # 06, 6
        "Function_7_3EEF",         # 07, 7
        "Function_8_3F1F",         # 08, 8
        "Function_9_3F40",         # 09, 9
        "Function_10_3F77",        # 0A, 10
        "Function_11_3FBD",        # 0B, 11
        "Function_12_4003",        # 0C, 12
        "Function_13_403A",        # 0D, 13
        "Function_14_4080",        # 0E, 14
        "Function_15_40C6",        # 0F, 15
        "Function_16_40F3",        # 10, 16
        "Function_17_4120",        # 11, 17
        "Function_18_421E",        # 12, 18
        "Function_19_4258",        # 13, 19
        "Function_20_4292",        # 14, 20
        "Function_21_42CC",        # 15, 21
        "Function_22_4306",        # 16, 22
        "Function_23_4340",        # 17, 23
        "Function_24_437A",        # 18, 24
        "Function_25_43B4",        # 19, 25
        "Function_26_43EE",        # 1A, 26
        "Function_27_441E",        # 1B, 27
        "Function_28_4458",        # 1C, 28
        "Function_29_4492",        # 1D, 29
        "Function_30_44CC",        # 1E, 30
        "Function_31_4506",        # 1F, 31
        "Function_32_4540",        # 20, 32
        "Function_33_457A",        # 21, 33
        "Function_34_45B4",        # 22, 34
        "Function_35_45EE",        # 23, 35
        "Function_36_4628",        # 24, 36
        "Function_37_4662",        # 25, 37
        "Function_38_4697",        # 26, 38
        "Function_39_46D1",        # 27, 39
        "Function_40_470B",        # 28, 40
        "Function_41_4740",        # 29, 41
        "Function_42_4775",        # 2A, 42
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    OP_C4(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9")
    Call(0, 33)
    Call(0, 34)

    label("loc_C9")

    OP_D2(0x2601E2, 0x2601E7, 0x0)
    OP_D2(0x2601EC, 0x2601F1, 0x1)
    OP_D2(0x2601ED, 0x2601F2, 0x2)
    OP_D2(0x270110, 0x270120, 0x3)
    OP_D2(0x27034E, 0x27035E, 0x6)
    OP_D2(0x270019, 0x27001D, 0x7)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_136"),
        (5, "loc_143"),
        (3, "loc_150"),
        (4, "loc_15D"),
        (6, "loc_16A"),
        (7, "loc_177"),
        (8, "loc_184"),
        (10, "loc_191"),
        (14, "loc_19E"),
        (15, "loc_1AB"),
        (SWITCH_DEFAULT, "loc_1B8"),
    )


    label("loc_136")

    OP_D2(0x701D0, 0x701DC, 0xB)
    Jump("loc_1B8")

    label("loc_143")

    OP_D2(0x70218, 0x70224, 0xB)
    Jump("loc_1B8")

    label("loc_150")

    OP_D2(0x701E8, 0x701F4, 0xB)
    Jump("loc_1B8")

    label("loc_15D")

    OP_D2(0x27036E, 0x27037B, 0xB)
    Jump("loc_1B8")

    label("loc_16A")

    OP_D2(0x70230, 0x7023C, 0xB)
    Jump("loc_1B8")

    label("loc_177")

    OP_D2(0x70248, 0x70254, 0xB)
    Jump("loc_1B8")

    label("loc_184")

    OP_D2(0x270176, 0x270183, 0xB)
    Jump("loc_1B8")

    label("loc_191")

    OP_D2(0x702B4, 0x702BB, 0xB)
    Jump("loc_1B8")

    label("loc_19E")

    OP_D2(0x2702D6, 0x2702E0, 0xB)
    Jump("loc_1B8")

    label("loc_1AB")

    OP_D2(0x2702C2, 0x2702CC, 0xB)
    Jump("loc_1B8")

    label("loc_1B8")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1E9"),
        (5, "loc_1F6"),
        (3, "loc_203"),
        (4, "loc_210"),
        (6, "loc_21D"),
        (7, "loc_22A"),
        (8, "loc_237"),
        (10, "loc_244"),
        (14, "loc_251"),
        (15, "loc_25E"),
        (SWITCH_DEFAULT, "loc_26B"),
    )


    label("loc_1E9")

    OP_D2(0x701D0, 0x701DC, 0xD)
    Jump("loc_26B")

    label("loc_1F6")

    OP_D2(0x70218, 0x70224, 0xD)
    Jump("loc_26B")

    label("loc_203")

    OP_D2(0x701E8, 0x701F4, 0xD)
    Jump("loc_26B")

    label("loc_210")

    OP_D2(0x27036E, 0x27037B, 0xD)
    Jump("loc_26B")

    label("loc_21D")

    OP_D2(0x70230, 0x7023C, 0xD)
    Jump("loc_26B")

    label("loc_22A")

    OP_D2(0x70248, 0x70254, 0xD)
    Jump("loc_26B")

    label("loc_237")

    OP_D2(0x270176, 0x270183, 0xD)
    Jump("loc_26B")

    label("loc_244")

    OP_D2(0x702B4, 0x702BB, 0xD)
    Jump("loc_26B")

    label("loc_251")

    OP_D2(0x2702D6, 0x2702E0, 0xD)
    Jump("loc_26B")

    label("loc_25E")

    OP_D2(0x2702C2, 0x2702CC, 0xD)
    Jump("loc_26B")

    label("loc_26B")

    OP_D2(0x270292, 0x27029C, 0xF)
    OP_D2(0x270296, 0x2702A0, 0x10)
    OP_D2(0x2601E6, 0x2601EB, 0x11)
    OP_D2(0x2701D3, 0x2701D8, 0x12)
    OP_D2(0x270445, 0x270447, 0x13)
    OP_D2(0x2701D2, 0x2701D7, 0x14)
    OP_D2(0x270444, 0x270446, 0x15)
    OP_D2(0x70142, 0x70146, 0x16)
    OP_D2(0x2701F9, 0x2701FE, 0x17)
    OP_D2(0x2703BC, 0x2703BE, 0x18)
    OP_D2(0x2701FA, 0x2701FF, 0x19)
    OP_D2(0x2703BD, 0x2703BF, 0x1A)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32C")
    OP_D2(0x2700A0, 0x2700A4, 0x1B)
    OP_D2(0x2700A1, 0x2700A5, 0x1C)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_360")
    OP_D2(0x270398, 0x27039C, 0x1B)
    OP_D2(0x270399, 0x27039D, 0x1C)
    OP_A2(0x3)
    Jump("loc_374")

    label("loc_360")

    OP_D2(0x270398, 0x27039C, 0x1D)
    OP_D2(0x270399, 0x27039D, 0x1E)

    label("loc_374")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_37E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B2")
    OP_D2(0x70020, 0x70028, 0x1B)
    OP_D2(0x70021, 0x70029, 0x1C)
    OP_A2(0x4)
    Jump("loc_3ED")

    label("loc_3B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D9")
    OP_D2(0x70020, 0x70028, 0x1D)
    OP_D2(0x70021, 0x70029, 0x1E)
    OP_A2(0x5)
    Jump("loc_3ED")

    label("loc_3D9")

    OP_D2(0x70020, 0x70028, 0x1F)
    OP_D2(0x70021, 0x70029, 0x20)

    label("loc_3ED")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_46A")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_428")
    OP_D2(0x70030, 0x70038, 0x1D)
    OP_D2(0x70031, 0x70039, 0x1E)
    Jump("loc_460")

    label("loc_428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44C")
    OP_D2(0x70030, 0x70038, 0x1F)
    OP_D2(0x70031, 0x70039, 0x20)
    Jump("loc_460")

    label("loc_44C")

    OP_D2(0x70030, 0x70038, 0x21)
    OP_D2(0x70031, 0x70039, 0x22)

    label("loc_460")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_46A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4DD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49B")
    OP_D2(0x70050, 0x70058, 0x1F)
    OP_D2(0x70051, 0x70059, 0x20)
    Jump("loc_4D3")

    label("loc_49B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BF")
    OP_D2(0x70050, 0x70058, 0x21)
    OP_D2(0x70051, 0x70059, 0x22)
    Jump("loc_4D3")

    label("loc_4BF")

    OP_D2(0x70050, 0x70058, 0x23)
    OP_D2(0x70051, 0x70059, 0x24)

    label("loc_4D3")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_4DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_518")
    OP_D2(0x70060, 0x70068, 0x21)
    OP_D2(0x70061, 0x70069, 0x22)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_564")

    label("loc_518")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_546")
    OP_D2(0x70060, 0x70068, 0x23)
    OP_D2(0x70061, 0x70069, 0x24)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_564")

    label("loc_546")

    OP_D2(0x70060, 0x70068, 0x25)
    OP_D2(0x70061, 0x70069, 0x26)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_564")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_56E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5D1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A9")
    OP_D2(0x70070, 0x70078, 0x23)
    OP_D2(0x70071, 0x70079, 0x24)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5C7")

    label("loc_5A9")

    OP_D2(0x70070, 0x70078, 0x25)
    OP_D2(0x70071, 0x70079, 0x26)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C7")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5D1")

    SetChrChipByIndex(0x11, 28)
    SetChrChipByIndex(0x12, 30)
    SetChrChipByIndex(0x13, 32)
    SetChrChipByIndex(0x14, 34)
    SetChrChipByIndex(0x15, 36)
    SetChrChipByIndex(0x16, 38)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 2)
    SetChrPos(0x8, 7430, 2590, 0, 270)
    SetChrFlags(0x8, 0x800)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -8090, 200, 12500, 315)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x800)
    SetChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 7)
    SetChrChipByIndex(0x9, 0)
    OP_72(0x1, 0x4)
    OP_A1(0x20, 0x1)
    SetChrPos(0x20, -3000, 200, 10000, 145)
    OP_6F(0x1, 1150)
    OP_70(0x1, 0x47E)
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x88, 0x0)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0xF8, 11)
    SetChrChipByIndex(0xF9, 13)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrPos(0x101, -240, 3130, -560, 90)
    SetChrPos(0x102, 230, 3040, 550, 90)
    SetChrPos(0xF8, -1310, 3200, -1020, 90)
    SetChrPos(0xF9, -1350, 3200, 1030, 90)
    OP_6D(-9600, 10910, -80, 0)
    OP_67(0, 5020, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(90000, 0)
    OP_6E(516, 0)
    OP_79(0x12, 0x2)
    OP_79(0x13, 0x2)
    OP_79(0x14, 0x2)
    OP_7B()
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_6D(5750, 2580, 0, 0)
    OP_67(0, 4490, -10000, 0)
    OP_6B(2370, 0)
    OP_6C(90000, 0)
    OP_6E(446, 0)
    ClearChrFlags(0x9, 0x800)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 17)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#1156FWh...at? No...absurd.\x02\x03",

            "The Aureole is...gone?\x02\x03",

            "#1157FThis is impossible... IMPOSSIBLE!\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "battle\\\\mgaria0.eff")
    LoadEffect(0x1, "map\\\\mp049_22.eff")

    def lambda_81E():
        OP_6D(7750, 2580, 0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81E)

    def lambda_836():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_836)

    def lambda_846():

        label("loc_846")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_846")

    QueueWorkItem2(0x8, 0, lambda_846)
    Sleep(300)
    OP_99(0x8, 0x2, 0x0, 0x3E8)
    OP_44(0x8, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x8, 16)
    SetChrSubChip(0x8, 0)
    PlayEffect(0x0, 0x0, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(500)
    OP_99(0x8, 0x0, 0x4, 0x7D0)
    OP_22(0xD8, 0x0, 0x64)
    OP_99(0x8, 0x5, 0x9, 0x7D0)
    OP_82(0x0, 0x2)
    Sleep(300)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x8, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_922():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_922)
    WaitChrThread(0x8, 0x1)
    OP_83(0x1, 0x2)
    OP_82(0x0, 0x2)
    SetChrFlags(0x8, 0x80)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_964")

    ChrTalk(    #1
        0x109,
        "#1063FTch!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A65")

    label("loc_964")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_983")

    ChrTalk(    #2
        0x107,
        "#065FAh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A65")

    label("loc_983")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A2")

    ChrTalk(    #3
        0x10F,
        "#173FOh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A65")

    label("loc_9A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C2")

    ChrTalk(    #4
        0x105,
        "#1162FAh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A65")

    label("loc_9C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E4")

    ChrTalk(    #5
        0x10B,
        "#213FYipes!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A65")

    label("loc_9E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A04")

    ChrTalk(    #6
        0x104,
        "#032FTch!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A65")

    label("loc_A04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A25")

    ChrTalk(    #7
        0x108,
        "#072FHmph!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A65")

    label("loc_A25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A47")

    ChrTalk(    #8
        0x103,
        "#022FBlast!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A65")

    label("loc_A47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A65")

    ChrTalk(    #9
        0x106,
        "#054FDamn!\x02",
    )

    CloseMessageWindow()

    label("loc_A65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A8D")

    ChrTalk(    #10
        0x110,
        "#276FHe got away.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF9")

    label("loc_A8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ABB")

    ChrTalk(    #11
        0x106,
        "#054FHe got away! Argh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF9")

    label("loc_ABB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF1")

    ChrTalk(    #12
        0x103,
        "#024FHe got away! Blast it all!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF9")

    label("loc_AF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B1A")

    ChrTalk(    #13
        0x108,
        "#076FHe's escaped.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF9")

    label("loc_B1A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B43")

    ChrTalk(    #14
        0x104,
        "#032FHe's escaped!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF9")

    label("loc_B43")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B74")

    ChrTalk(    #15
        0x10B,
        "#216FOh, he got away! Foo!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF9")

    label("loc_B74")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA0")

    ChrTalk(    #16
        0x105,
        "#1163FNo, he escaped!\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF9")

    label("loc_BA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BCF")

    ChrTalk(    #17
        0x10F,
        "#175FSo, he's escaped...\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF9")

    label("loc_BCF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BF9")

    ChrTalk(    #18
        0x107,
        "#065FAww, he got away!\x02",
    )

    CloseMessageWindow()

    label("loc_BF9")


    ChrTalk(    #19
        0x101,
        (
            "#1022F#5POh, who cares about that idiot!\x02\x03",

            "#1020FWay more importantly...!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Fade(500)
    OP_6D(-4450, 3150, 1350, 0)
    OP_67(0, 4490, -10000, 0)
    OP_6B(2370, 0)
    OP_6C(20000, 0)
    OP_6E(446, 0)
    SetChrPos(0x102, -540, 3200, 40, 90)

    def lambda_CCD():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CCD)
    Sleep(50)

    def lambda_CE0():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CE0)
    Sleep(50)

    def lambda_CF3():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_CF3)
    Sleep(50)
    TurnDirection(0xF8, 0x9, 400)
    OP_0D()
    Sleep(500)

    ChrTalk(    #20
        0x102,
        "#1046F#4P#3SLOEWE!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_43(0x102, 0x1, 0x1, 0x4)
    Sleep(500)
    OP_43(0x101, 0x1, 0x1, 0x5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DA0")
    Sleep(800)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D73")
    OP_43(0xF9, 0x1, 0x1, 0x7)
    Jump("loc_D7A")

    label("loc_D73")

    OP_43(0xF8, 0x1, 0x1, 0x6)

    label("loc_D7A")

    Sleep(1000)

    ChrTalk(    #21
        0x109,
        "#1063F#6P...\x02",
    )

    CloseMessageWindow()
    OP_43(0x109, 0x1, 0x1, 0x8)
    Sleep(1500)
    Jump("loc_DBD")

    label("loc_DA0")

    Sleep(800)
    OP_43(0xF9, 0x1, 0x1, 0x7)
    Sleep(400)
    OP_43(0xF8, 0x1, 0x1, 0x6)
    Sleep(1000)

    label("loc_DBD")

    Fade(500)
    OP_6D(-8550, 200, 12720, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(20000, 0)
    OP_6E(334, 0)
    OP_0D()
    WaitChrThread(0x102, 0x1)
    Sleep(500)

    ChrTalk(    #22
        0x102,
        (
            "#1046F#6PLoewe! Stay with us!\x02\x03",

            "Just...wait a second!\x01",
            "We'll fix you up!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    Sleep(100)
    OP_1D(0x72)
    Sleep(500)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    def lambda_E9D():
        OP_6B(2200, 50000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E9D)
    Sleep(500)

    ChrTalk(    #23
        0x9,
        (
            "#121F#6P#40WThere's...no need...\x02\x03",

            "#40WYou...know perfectly well, these aren't\x01",
            "the sort of wounds you 'fix up'...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        (
            "#1059F#6PNo... No, please, no!\x02\x03",

            "Loewe, I can't lose you like Karin!\x02\x03",

            "That's just... No, I can't!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "#121F#6P#40WHah... Come on, chin up.\x02\x03",

            "#40WHeh, you look like...the crybaby you\x01",
            "were when you were a kid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#1059F#6PThat's right!\x01",
            "I'm a weak, naive crybaby!\x02\x03",

            "I still need you, Loewe!\x02\x03",

            "So...come on! Stay awake!\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(500)

    ChrTalk(    #27
        0x9,
        (
            "#124F#6P#40W...Just like a little kid...\x02\x03",

            "#40WListen...Joshua...\x02\x03",

            "#40WIf you find this...unacceptable...\x01",
            "then take a lesson from me.\x01",
            "Don't end up like this...\x02\x03",

            "#40WDon't die to...protect what's important.\x02\x03",

            "#40WLive... Live to protect it...instead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        "#1044F#6PLoewe...!\x02",
    )

    CloseMessageWindow()
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(500)

    ChrTalk(    #29
        0x9,
        "#121F#6P#40WEstelle...I must ask you one last favor...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        "#1025F#2POf... Of course. Anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x9,
        (
            "#121F#6P#40WHe likes to act tough, but he's...\x01",
            "pretty tenderhearted deep down...\x02\x03",

            "#40WNow that he's truly free of his curse...\x01",
            "he needs to become a better man.\x02\x03",

            "#124F#40WSo...please.\x02\x03",

            "#40WPromise...me that you'll keep helping him...\x02\x03",

            "#40WTake care of...our little brother, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1016F#2PHeehee... I was gonna do THAT no\x01",
            "matter what you said.\x02\x03",

            "#1025FBut...don't worry, Loewe.\x02\x03",

            "I swear to you, he'll always have\x01",
            "a home with us.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(250)
    Sleep(500)

    ChrTalk(    #33
        0x9,
        "#124F#6P#40WThank you...\x02",
    )

    CloseMessageWindow()
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(500)

    ChrTalk(    #34
        0x9,
        (
            "#1431F#6P#40WHah... At least I finally understand.\x02\x03",

            "#50WWhy Karin...could #60Wsmile like that...at the end.\x02\x03",

            "#1430F#70WKarin...you were just as...as content...\x01",
            "#80Wweren't...y...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(400)
    Sleep(1000)

    ChrTalk(    #35
        0x9,
        "#2P#40W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        "#1044F#6PL-Loewe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        "#2P#40W...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        (
            "#1054F#6PC'mon. This isn't funny.\x02\x03",

            "You can hear me...right...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        "#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#1059F#6PCome on! COME ON!\x02\x03",

            "It all finally ended!\x02\x03",

            "We could finally, FINALLY be together again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        "#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        "#1057F#6PPlease...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #43
        0x102,
        "#1059F#6P#3SPLEASE, ANSWER ME!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    def lambda_1667():

        label("loc_1667")

        OP_9E(0xFE, 0xA, 0x0, 0x12C, 0x7D0)
        OP_48()
        Jump("loc_1667")

    QueueWorkItem2(0x102, 3, lambda_1667)

    ChrTalk(    #44
        0x101,
        "#1026F#2PJoshua...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16BB")

    ChrTalk(    #45
        0x10B,
        "#417F#2P*sniffle*\x02",
    )

    CloseMessageWindow()

    label("loc_16BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16E7")

    ChrTalk(    #46
        0x10F,
        "#175FAidios, take him...\x02",
    )

    CloseMessageWindow()

    label("loc_16E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1711")

    ChrTalk(    #47
        0x105,
        "#1169F#2POh, Joshua...\x02",
    )

    CloseMessageWindow()

    label("loc_1711")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1738")

    ChrTalk(    #48
        0x107,
        "#562F#2PJoshuaaa...\x02",
    )

    CloseMessageWindow()

    label("loc_1738")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1772")

    ChrTalk(    #49
        0x103,
        "#522F#2POh, Joshua...it's all right...\x02",
    )

    CloseMessageWindow()

    label("loc_1772")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_179D")

    ChrTalk(    #50
        0x104,
        "#032F#2POh, my heart...\x02",
    )

    CloseMessageWindow()

    label("loc_179D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F0")

    ChrTalk(    #51
        0x106,
        (
            "#552F#2PWell...guess you get away with\x01",
            "that win on me, partner.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_180C")

    ChrTalk(    #52
        0x110,
        "#276F...\x02",
    )

    CloseMessageWindow()

    label("loc_180C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1860")

    ChrTalk(    #53
        0x108,
        (
            "#572F#2P...May his karma guide him to reward\x01",
            "in his next life...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1860")

    OP_44(0x102, 0x3)
    SetChrChipByIndex(0xB, 19)
    SetChrChipByIndex(0xA, 21)
    SetChrChipByIndex(0xC, 22)
    SetChrChipByIndex(0xD, 24)
    SetChrChipByIndex(0xE, 26)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18C2")
    SetChrPos(0xB, -18830, 250, -1230, 45)

    NpcTalk(    #54
        0xB,
        "Woman's Voice",
        "#2PHello there!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1945")

    label("loc_18C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1907")
    SetChrPos(0xB, -18830, 250, -1230, 45)

    NpcTalk(    #55
        0xB,
        "Man's Voice",
        "#2PTHERE you are!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1945")

    label("loc_1907")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1945")
    SetChrPos(0xB, -18830, 250, -1230, 45)

    NpcTalk(    #56
        0xB,
        "Girl's Voice",
        "#2PEveryone!\x02",
    )

    CloseMessageWindow()

    label("loc_1945")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1988")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19C6")

    label("loc_1988")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19AF")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_19C6")

    label("loc_19AF")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_19C6")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F2")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A30")

    label("loc_19F2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A19")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A30")

    label("loc_1A19")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1A30")

    Sleep(1000)

    def lambda_1A3B():
        OP_6D(-9880, 200, 9120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A3B)

    def lambda_1A53():
        OP_67(0, 4580, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A53)

    def lambda_1A6B():
        OP_6B(2700, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1A6B)

    def lambda_1A7B():
        OP_6E(392, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1A7B)

    def lambda_1A8B():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A8B)
    Sleep(100)

    def lambda_1A9E():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1A9E)
    Sleep(100)

    def lambda_1AB1():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1AB1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ACE")
    OP_43(0xB, 0x1, 0x1, 0x12)

    label("loc_1ACE")

    Sleep(600)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AE8")
    OP_43(0xA, 0x1, 0x1, 0x13)

    label("loc_1AE8")

    Sleep(350)
    OP_43(0x12, 0x1, 0x1, 0x15)
    Sleep(230)
    OP_43(0x11, 0x1, 0x1, 0x14)
    Sleep(280)
    OP_43(0x13, 0x1, 0x1, 0x16)
    Sleep(230)
    OP_43(0x14, 0x1, 0x1, 0x17)
    Sleep(250)
    OP_43(0x15, 0x1, 0x1, 0x18)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B3E")
    OP_43(0x16, 0x1, 0x1, 0x19)

    label("loc_1B3E")

    Sleep(600)
    OP_43(0xC, 0x1, 0x1, 0x1A)
    Sleep(250)
    OP_43(0xE, 0x1, 0x1, 0x1B)
    Sleep(200)
    OP_43(0xD, 0x1, 0x1, 0x1C)
    WaitChrThread(0x12, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1B82")
    SetChrPos(0x17, -11990, 200, 6140, 0)
    Jump("loc_1B93")

    label("loc_1B82")

    SetChrPos(0x17, -11310, 200, 5080, 0)

    label("loc_1B93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1BAE")
    SetChrPos(0x18, -11990, 200, 6140, 0)
    Jump("loc_1BDA")

    label("loc_1BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1BC9")
    SetChrPos(0x18, -11310, 200, 5080, 0)
    Jump("loc_1BDA")

    label("loc_1BC9")

    SetChrPos(0x18, -12640, 200, 7450, 0)

    label("loc_1BDA")


    ChrTalk(    #57
        0x101,
        "#1004F#4PAh!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2023")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CC2")

    ChrTalk(    #58
        0x105,
        "#1163FJulia...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xB,
        "#170FGoddess be praised, you're all safe.\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xB, 0, 400)
    Sleep(500)

    ChrTalk(    #60
        0xB,
        "#173FWait, that's...Loewe? Is he--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x105,
        "#1169F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xB,
        "#175FAh. I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E36")

    label("loc_1CC2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D8F")

    ChrTalk(    #63
        0x110,
        "#270FCaptain...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xB,
        "#170FGoddess be praised, you're all safe.\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xB, 0, 400)
    Sleep(500)

    ChrTalk(    #65
        0xB,
        "#173FWait, that's...Loewe? Is he--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1003FYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xB,
        "#175FAh. I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E36")

    label("loc_1D8F")


    ChrTalk(    #68
        0xB,
        "#170FGoddess be praised, you're all safe.\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xB, 0, 400)
    Sleep(500)

    ChrTalk(    #69
        0xB,
        "#173FWait, that's...Loewe? Is he--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        "#1003FYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xB,
        "#175FAh. I see.\x02",
    )

    CloseMessageWindow()

    label("loc_1E36")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EDA")

    ChrTalk(    #72
        0xA,
        (
            "#272FAfter you descended, we were swarmed\x01",
            "by those archaism beasts.\x02\x03",

            "#270FIt was only Loewe intervening on that\x01",
            "dragon of his which saved us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2020")

    label("loc_1EDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F73")

    ChrTalk(    #73
        0x17,
        (
            "#1167FWe were nearly overwhelmed by the\x01",
            "archaisms after you went down...\x02\x03",

            "#1162FWe were only saved by Loewe calling\x01",
            "in his dragon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2020")

    label("loc_1F73")


    ChrTalk(    #74
        0x18,
        (
            "#026FAfter you went down, we were swarmed\x01",
            "by archaisms.\x02\x03",

            "#022FJust when they had us backed into a\x01",
            "corner, he brought in that metal dragon\x01",
            "of his and turned the tables.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2020")

    Jump("loc_2387")

    label("loc_2023")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_220D")

    ChrTalk(    #75
        0x10F,
        "#173FMajor!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        "#270FEveryone's in one piece.\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #77
        0xA,
        "#273FIs Loewe...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        "#1003FYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xA,
        "#276FDamn it all...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_215D")

    ChrTalk(    #80
        0x17,
        (
            "#1167FWe were nearly overwhelmed by the\x01",
            "archaisms after you went down...\x02\x03",

            "#1162FWe were only saved by Loewe calling\x01",
            "in his dragon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_220A")

    label("loc_215D")


    ChrTalk(    #81
        0x18,
        (
            "#026FAfter you went down, we were swarmed\x01",
            "by archaisms.\x02\x03",

            "#022FJust when they had us backed into a\x01",
            "corner, he brought in that metal dragon\x01",
            "of his and turned the tables.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_220A")

    Jump("loc_2387")

    label("loc_220D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2387")

    ChrTalk(    #82
        0x101,
        "#1025FEveryone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x17,
        "#1162FIs everyone all right?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2282")
    OP_8C(0x11, 0, 400)
    Jump("loc_2289")

    label("loc_2282")

    OP_8C(0x12, 0, 400)

    label("loc_2289")

    Sleep(500)

    ChrTalk(    #84
        0x17,
        (
            "#1164FWait...\x02\x03",

            "#1163FEstelle, Loewe isn't...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#1003FYeah...he is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x18,
        (
            "#026FAfter you went down, we were swarmed\x01",
            "by archaisms.\x02\x03",

            "#022FJust when they had us backed into a\x01",
            "corner, he brought in that metal dragon\x01",
            "of his and turned the tables.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2387")


    ChrTalk(    #87
        0x101,
        (
            "#1025F#4PI see...\x01",
            "Yeah, that sounds like him, all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xC,
        (
            "#102F#5PIf I may... What happened to\x01",
            "Weissmann and the Aureole?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1015F#4POh, right...\x02\x03",

            "#1007FYeah, the Aureole disappeared somewhere.\x02\x03",

            "Weissmann's also gone, but...he really\x01",
            "lost it when the Aureole disappeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xC,
        (
            "#103F#5PIt...disappeared?\x02\x03",

            "#104FWell. That could be bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        "#1004F#4PUh. Define 'bad.'\x02",
    )

    CloseMessageWindow()
    OP_43(0x9, 0x3, 0x1, 0x3)
    OP_22(0x85, 0x1, 0x50)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #92
        0x101,
        (
            "#1020F#4PPLEASE tell me this shaking isn't\x01",
            "involved in the 'bad'!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xC,
        (
            "#104F#5PThe Aureole was the main source of\x01",
            "power for the city.\x02\x03",

            "#102FYou've removed the city's power source.\x01",
            "There's nothing keeping it afloat any longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2658")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2696")

    label("loc_2658")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267F")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2696")

    label("loc_267F")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2696")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26BD")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_26FB")

    label("loc_26BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26E4")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_26FB")

    label("loc_26E4")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_26FB")

    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D7")
    OP_62(0x14, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_27EE")

    label("loc_27D7")

    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_27EE")

    Sleep(50)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_281A")
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2858")

    label("loc_281A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2841")
    OP_62(0x15, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_2858")

    label("loc_2841")

    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_2858")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28A4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_288D")
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_28A4")

    label("loc_288D")

    OP_62(0x16, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_28A4")

    Sleep(1000)

    def lambda_28AF():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_28AF)
    Sleep(50)
    TurnDirection(0xA, 0xC, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28FD")

    ChrTalk(    #94
        0x10F,
        "#173F#4PYes, that seems rather bad!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2926")

    label("loc_28FD")


    ChrTalk(    #95
        0xB,
        "#173F#4PYes, that seems rather bad!\x02",
    )

    CloseMessageWindow()

    label("loc_2926")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_296E")

    ChrTalk(    #96
        0x110,
        "#272F#4PWe should return to the Arseille at once.\x02",
    )

    CloseMessageWindow()
    Jump("loc_29A5")

    label("loc_296E")


    ChrTalk(    #97
        0xA,
        "#272F#6PWe should return to the Arseille at once.\x02",
    )

    CloseMessageWindow()

    label("loc_29A5")


    ChrTalk(    #98
        0xC,
        (
            "#104F#5PA good idea.\x02\x03",

            "#102FI don't think everything will shut down all\x01",
            "at once, but it would be best if we hurry.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)
    Sleep(300)

    ChrTalk(    #99
        0xC,
        "#102F#5PKyle, Don, is the Bobcat airworthy?\x02",
    )

    CloseMessageWindow()

    def lambda_2A5F():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2A5F)
    Sleep(100)
    TurnDirection(0xE, 0xC, 400)

    ChrTalk(    #100
        0xE,
        (
            "#200F#5PShould be airworthy enough to save\x01",
            "our skins, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xD,
        "#490F#5PWe'll lift off as soon as we get back.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BA9")

    def lambda_2B00():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2B00)

    def lambda_2B0E():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2B0E)
    Sleep(50)

    def lambda_2B21():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2B21)

    def lambda_2B2F():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2B2F)
    Sleep(50)

    def lambda_2B42():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2B42)

    def lambda_2B50():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2B50)
    Sleep(50)

    def lambda_2B63():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2B63)

    def lambda_2B71():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2B71)
    Sleep(50)

    def lambda_2B84():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2B84)

    def lambda_2B92():
        TurnDirection(0xFE, 0x10F, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2B92)
    Sleep(50)
    OP_8C(0xA, 180, 400)
    Jump("loc_2C55")

    label("loc_2BA9")


    def lambda_2BAF():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2BAF)

    def lambda_2BBD():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2BBD)
    Sleep(50)

    def lambda_2BD0():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2BD0)

    def lambda_2BDE():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2BDE)
    Sleep(50)

    def lambda_2BF1():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2BF1)

    def lambda_2BFF():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2BFF)
    Sleep(50)

    def lambda_2C12():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2C12)

    def lambda_2C20():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2C20)
    Sleep(50)

    def lambda_2C33():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2C33)

    def lambda_2C41():
        TurnDirection(0xFE, 0xB, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2C41)
    Sleep(50)
    OP_8C(0xA, 180, 400)

    label("loc_2C55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D2E")

    ChrTalk(    #102
        0xB,
        (
            "#177F#4PAll right, then.\x01",
            "Everyone, let's go!\x02\x03",

            "There was a transfer gate near the elevator!\x02\x03",

            "We should use that to leave the pillar! Stay\x01",
            "in lines so we don't lose sight of each other!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F2B")

    label("loc_2D2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E2D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D78")

    ChrTalk(    #103
        0x10F,
        "#177FAll right. Let's move, everyone!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DA3")

    label("loc_2D78")


    ChrTalk(    #104
        0xB,
        "#177FAll right. Let's move, everyone!\x02",
    )

    CloseMessageWindow()

    label("loc_2DA3")


    ChrTalk(    #105
        0xA,
        (
            "#271FThere was a transfer gate near the elevator!\x02\x03",

            "That seems like the best exit. We should\x01",
            "stay in lines to avoid losing anyone!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F2B")

    label("loc_2E2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E77")

    ChrTalk(    #106
        0x10F,
        "#177FAll right. Let's move, everyone!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EA2")

    label("loc_2E77")


    ChrTalk(    #107
        0xB,
        "#177FAll right. Let's move, everyone!\x02",
    )

    CloseMessageWindow()

    label("loc_2EA2")


    ChrTalk(    #108
        0x17,
        (
            "#1162FI believe I saw a transfer gate near the elevator.\x02\x03",

            "We should form into lines to stay together\x01",
            "and use it to exit the pillar!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F2B")

    Sleep(300)

    def lambda_2F36():
        OP_6D(-20380, 200, 3160, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F36)

    def lambda_2F4E():
        OP_67(0, 5690, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F4E)

    def lambda_2F66():
        OP_6B(3390, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F66)

    def lambda_2F76():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2F76)

    def lambda_2F86():
        OP_6E(456, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F86)
    Sleep(300)
    OP_43(0xD, 0x0, 0x1, 0x27)
    Sleep(200)
    OP_43(0xE, 0x0, 0x1, 0x26)
    Sleep(200)
    OP_43(0xC, 0x0, 0x1, 0x25)
    Sleep(400)
    OP_43(0x16, 0x0, 0x1, 0x24)
    Sleep(100)
    OP_43(0x15, 0x0, 0x1, 0x23)
    Sleep(150)
    OP_43(0x14, 0x0, 0x1, 0x22)
    Sleep(180)
    OP_43(0x12, 0x0, 0x1, 0x20)
    Sleep(200)
    OP_43(0x13, 0x0, 0x1, 0x21)
    Sleep(250)
    OP_43(0x11, 0x0, 0x1, 0x1F)
    Sleep(250)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3016")
    OP_43(0xB, 0x0, 0x1, 0x1D)

    label("loc_3016")

    Sleep(350)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3030")
    OP_43(0xA, 0x0, 0x1, 0x1E)

    label("loc_3030")

    Sleep(100)
    OP_43(0xF8, 0x0, 0x1, 0x28)
    Sleep(300)
    OP_43(0xF9, 0x0, 0x1, 0x29)
    WaitChrThread(0x101, 0x0)
    Sleep(2000)
    Fade(1000)
    OP_6D(-8029, 200, 11880, 0)
    OP_67(0, 5760, -10000, 0)
    OP_6B(1960, 0)
    OP_6C(21000, 0)
    OP_6E(411, 0)
    OP_0D()
    Sleep(500)
    OP_8C(0x101, 315, 400)
    Sleep(500)

    ChrTalk(    #109
        0x102,
        "#1057F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#1027F#4PJoshua...um...\x02\x03",

            "I know you...don't want to leave him\x01",
            "behind, but we have to hurry...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x102,
        (
            "#1057F#6P...Sorry, Estelle...\x02\x03",

            "You just...go on ahead.\x02\x03",

            "Don't... Don't worry about me... Go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#1002F#4P. . .\x02",
    )

    CloseMessageWindow()

    def lambda_3197():
        OP_6D(-9030, 200, 13460, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3197)

    def lambda_31AF():
        OP_6B(2300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_31AF)
    OP_8E(0x101, 0xFFFFDBFC, 0xC8, 0x2FDA, 0x5DC, 0x0)
    WaitChrThread(0x101, 0x0)
    Fade(250)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x800)
    SetChrSubChip(0x102, 6)
    OP_0D()
    Sleep(500)
    OP_99(0x102, 0x6, 0xD, 0x5DC)
    Sleep(500)
    OP_99(0x102, 0xE, 0xF, 0x5DC)
    OP_22(0xA5, 0x0, 0x64)
    OP_99(0x102, 0x10, 0x1A, 0x5DC)

    ChrTalk(    #113
        0x102,
        "#1044F#6PAh!\x02",
    )

    CloseMessageWindow()
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(150)
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(500)

    ChrTalk(    #114
        0x101,
        (
            "#1023F#7PGET IT TOGETHER, JOSHUA!\x02\x03",

            "Were you listening to a damn thing Loewe\x01",
            "said?!\x02\x03",

            "Didn't he tell you to live?\x01",
            "To protect what's important to you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x102,
        "#1042F#6P#3SHe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1023F#7PI don't know about you, but I sure\x01",
            "was listening!\x02\x03",

            "And I promised him I'd stay with\x01",
            "you and help you! I promised YOU\x01",
            "the same once, too!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #117
        0x101,
        (
            "#1014F#7P#3SIf you think I'm just going to turn my\x01",
            "back on that, you've got another thing\x01",
            "coming!\x02",
        )
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #118
        0x102,
        (
            "#1057F#6PEstelle...\x02\x03",

            "#1035FSorry... I really am a weakling.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x102, 29)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x2)
    ClearChrFlags(0x102, 0x800)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)

    def lambda_349C():
        OP_8F(0xFE, 0xFFFFDD14, 0xC8, 0x2E86, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_349C)
    OP_8C(0x102, 135, 0)
    OP_0D()
    OP_8C(0x102, 45, 300)
    Sleep(500)
    SetChrFlags(0x102, 0x2)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 2)
    OP_99(0x102, 0x0, 0x2, 0x3E8)
    Sleep(500)
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    OP_99(0x102, 0x3, 0x4, 0x3E8)
    SetChrSubChip(0x9, 10)
    OP_0D()
    Sleep(500)
    OP_99(0x102, 0x5, 0x8, 0x3E8)
    Sleep(500)
    OP_99(0x102, 0x8, 0xB, 0x5DC)
    Sleep(500)
    OP_99(0x102, 0xC, 0xE, 0x5DC)
    Sleep(500)

    ChrTalk(    #119
        0x101,
        "#1004F#7POh! The sword...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x102, 17)
    OP_0D()
    Sleep(500)
    OP_99(0x102, 0x11, 0x13, 0x3E8)
    Sleep(500)

    ChrTalk(    #120
        0x102,
        (
            "#1035F#6PLoewe...I'll hold on to this.\x02\x03",

            "#1041FI'll deliver it to Hamel.\x01",
            "To Karin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        "#1025F#7PJoshua...!\x02",
    )

    CloseMessageWindow()

    def lambda_35E2():
        OP_6D(-9140, 200, 12720, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_35E2)

    def lambda_35FA():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_35FA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3707")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3693")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3637")
    OP_43(0xA, 0x0, 0x1, 0xB)
    Jump("loc_3656")

    label("loc_3637")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_364F")
    OP_43(0xB, 0x0, 0x1, 0xA)
    Jump("loc_3656")

    label("loc_364F")

    OP_43(0xB, 0x0, 0x1, 0xA)

    label("loc_3656")

    Sleep(300)
    OP_43(0xF9, 0x0, 0x1, 0x9)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3678")
    WaitChrThread(0xA, 0x0)
    Jump("loc_368B")

    label("loc_3678")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_368B")
    WaitChrThread(0xB, 0x0)

    label("loc_368B")

    WaitChrThread(0xF9, 0x0)
    Jump("loc_3704")

    label("loc_3693")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36AB")
    OP_43(0xA, 0x0, 0x1, 0xE)
    Jump("loc_36CA")

    label("loc_36AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36C3")
    OP_43(0xB, 0x0, 0x1, 0xD)
    Jump("loc_36CA")

    label("loc_36C3")

    OP_43(0xB, 0x0, 0x1, 0xD)

    label("loc_36CA")

    Sleep(300)
    OP_43(0xF8, 0x0, 0x1, 0xC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36EC")
    WaitChrThread(0xA, 0x0)
    Jump("loc_36FF")

    label("loc_36EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36FF")
    WaitChrThread(0xB, 0x0)

    label("loc_36FF")

    WaitChrThread(0xF8, 0x0)

    label("loc_3704")

    Jump("loc_3778")

    label("loc_3707")

    ClearChrFlags(0xF8, 0x80)
    ClearChrFlags(0xF9, 0x80)
    SetChrPos(0xF8, -21540, 200, 4840, 45)
    SetChrPos(0xF9, -21540, 200, 4840, 45)

    def lambda_3739():
        OP_8F(0xFE, 0xFFFFD47C, 0xC8, 0x26FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3739)
    Sleep(300)

    def lambda_3759():
        OP_8F(0xFE, 0xFFFFD116, 0xC8, 0x2AA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3759)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)

    label("loc_3778")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37A7")

    ChrTalk(    #122
        0x107,
        "#065F#5PEstelle! Joshua!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3919")

    label("loc_37A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37DB")

    ChrTalk(    #123
        0x10B,
        "#214F#5PHEY! JOSHUA! ESTELLE!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3919")

    label("loc_37DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_380B")

    ChrTalk(    #124
        0x105,
        "#1163F#5PEstelle! Joshua!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3919")

    label("loc_380B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_383A")

    ChrTalk(    #125
        0x103,
        "#024F#5PEstelle! Joshua!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3919")

    label("loc_383A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3869")

    ChrTalk(    #126
        0x104,
        "#530F#5PEstelle, Joshua!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3919")

    label("loc_3869")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_389D")

    ChrTalk(    #127
        0x106,
        "#054F#5PHey, Estelle! Joshua!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3919")

    label("loc_389D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38CC")

    ChrTalk(    #128
        0x108,
        "#076F#1PEstelle! Joshua!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3919")

    label("loc_38CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38F8")

    ChrTalk(    #129
        0x10F,
        "#177FEstelle, Joshua!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3919")

    label("loc_38F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3919")

    ChrTalk(    #130
        0x110,
        "#271FYou two!\x02",
    )

    CloseMessageWindow()

    label("loc_3919")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39A7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_396E")

    ChrTalk(    #131
        0xB,
        (
            "#177F#5PThere's no time to waste!\x01",
            "Please, hurry!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39A4")

    label("loc_396E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A4")

    ChrTalk(    #132
        0xA,
        "#271F#5PThis is no time to dawdle!\x02",
    )

    CloseMessageWindow()

    label("loc_39A4")

    Jump("loc_3BD7")

    label("loc_39A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39DD")

    ChrTalk(    #133
        0x110,
        "#271FThis is no time to dawdle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BD7")

    label("loc_39DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A21")

    ChrTalk(    #134
        0x10F,
        (
            "#177FThere's no time to waste!\x01",
            "Please, hurry!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD7")

    label("loc_3A21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A5F")

    ChrTalk(    #135
        0x108,
        "#076F#1PCome! We have no time to waste!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BD7")

    label("loc_3A5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AA8")

    ChrTalk(    #136
        0x106,
        (
            "#054F#5PWe ain't got time!\x01",
            "Get your asses in gear!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD7")

    label("loc_3AA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AF8")

    ChrTalk(    #137
        0x104,
        (
            "#530F#5PCome, friends!\x01",
            "This is no time for introspection!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD7")

    label("loc_3AF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B39")

    ChrTalk(    #138
        0x103,
        (
            "#024F#5PCome on, you two!\x01",
            "There's no time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD7")

    label("loc_3B39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B87")

    ChrTalk(    #139
        0x105,
        (
            "#1163F#5PI'm sorry, but there's no time!\x01",
            "Please, hurry!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD7")

    label("loc_3B87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BD7")

    ChrTalk(    #140
        0x10B,
        (
            "#214F#5PGet it in gear already!\x01",
            "We don't have time to waste!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD7")

    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)

    def lambda_3BEC():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BEC)
    Sleep(100)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    OP_8C(0x102, 135, 0)
    OP_8C(0x102, 225, 400)

    ChrTalk(    #141
        0x101,
        "#1002F#4PAh, right!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C40")
    OP_A2(0x6)

    label("loc_3C40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C51")
    OP_A2(0x6)

    label("loc_3C51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C62")
    OP_A2(0x6)

    label("loc_3C62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C73")
    OP_A2(0x6)

    label("loc_3C73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C84")
    OP_A2(0x6)

    label("loc_3C84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C95")
    OP_A2(0x6)

    label("loc_3C95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CA6")
    OP_A2(0x6)

    label("loc_3CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD4")

    ChrTalk(    #142
        0x102,
        "#1035F#4PRight, we're coming.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CFE")

    label("loc_3CD4")


    ChrTalk(    #143
        0x102,
        "#1035F#4PI'm sorry... I'm going now.\x02",
    )

    CloseMessageWindow()

    label("loc_3CFE")


    def lambda_3D04():
        OP_6D(-8119, 200, 13830, 1800)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D04)
    OP_8C(0x102, 135, 300)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 2)
    SetChrSubChip(0x102, 17)

    def lambda_3D32():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D32)
    OP_99(0x102, 0x11, 0x13, 0x3E8)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #144
        0x102,
        (
            "#1035F#6P(...)\x02\x03",

            "#1041F#6P(Rest well with Karin...Loewe.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_24(0x85, 0x46)
    Sleep(200)
    OP_24(0x85, 0x3C)
    Sleep(200)
    OP_24(0x85, 0x32)
    Sleep(200)
    OP_24(0x85, 0x28)
    Sleep(200)
    OP_24(0x85, 0x1E)
    Sleep(200)
    OP_24(0x85, 0x14)
    Sleep(200)
    OP_24(0x85, 0xA)
    Sleep(200)
    OP_23(0x85)
    OP_21()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5300   ._SN", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_2_AC end

    def Function_3_3DE6(): pass

    label("Function_3_3DE6")

    OP_7C(0x46, 0x46, 0x3E8, 0x3E8)
    Sleep(1000)

    label("loc_3DFC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E1E")
    OP_7C(0x28, 0x28, 0x3E8, 0x3E8)
    Sleep(1800)
    Jump("loc_3DFC")

    label("loc_3E1E")

    Return()

    # Function_3_3DE6 end

    def Function_4_3E1F(): pass

    label("Function_4_3E1F")

    OP_8E(0xFE, 0xFFFFFAB0, 0xC80, 0x3C, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFE340, 0xC8, 0x12C, 0x1770, 0x0)
    OP_8E(0xFE, 0xFFFFDA94, 0xC8, 0x3264, 0x1770, 0x0)
    OP_8C(0xFE, 45, 600)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 1)
    SetChrSubChip(0xFE, 0)
    OP_99(0xFE, 0x0, 0x3, 0x9C4)
    Return()

    # Function_4_3E1F end

    def Function_5_3E7B(): pass

    label("Function_5_3E7B")

    OP_8E(0xFE, 0xFFFFFAB0, 0xC80, 0x3C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFE340, 0xC8, 0x12C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFDEEA, 0xC8, 0x26FC, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_5_3E7B end

    def Function_6_3EBF(): pass

    label("Function_6_3EBF")

    OP_8E(0xFE, 0xFFFFE11A, 0xC8, 0xFFFFFC86, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFDF76, 0xC8, 0x209E, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_6_3EBF end

    def Function_7_3EEF(): pass

    label("Function_7_3EEF")

    OP_8E(0xFE, 0xFFFFE3A4, 0xC8, 0x49C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFE3A4, 0xC8, 0x2526, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_7_3EEF end

    def Function_8_3F1F(): pass

    label("Function_8_3F1F")

    OP_8C(0xFE, 253, 600)
    OP_8F(0xFE, 0xFFFFB1E0, 0x64, 0x384, 0x1388, 0x0)
    SetChrFlags(0x109, 0x80)
    Return()

    # Function_8_3F1F end

    def Function_9_3F40(): pass

    label("Function_9_3F40")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -21540, 200, 4840, 45)

    def lambda_3F5C():
        OP_8F(0xFE, 0xFFFFD116, 0xC8, 0x2AA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F5C)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_9_3F40 end

    def Function_10_3F77(): pass

    label("Function_10_3F77")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -21540, 200, 4840, 45)
    SetChrChipByIndex(0xB, 19)

    def lambda_3F98():
        OP_8F(0xFE, 0xFFFFD47C, 0xC8, 0x26FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3F98)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 18)
    SetChrSubChip(0xB, 0)
    Return()

    # Function_10_3F77 end

    def Function_11_3FBD(): pass

    label("Function_11_3FBD")

    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -21540, 200, 4840, 45)
    SetChrChipByIndex(0xA, 21)

    def lambda_3FDE():
        OP_8F(0xFE, 0xFFFFD47C, 0xC8, 0x26FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3FDE)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 20)
    SetChrSubChip(0xA, 0)
    Return()

    # Function_11_3FBD end

    def Function_12_4003(): pass

    label("Function_12_4003")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -21540, 200, 4840, 45)

    def lambda_401F():
        OP_8F(0xFE, 0xFFFFD47C, 0xC8, 0x26FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_401F)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_12_4003 end

    def Function_13_403A(): pass

    label("Function_13_403A")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -21540, 200, 4840, 45)
    SetChrChipByIndex(0xB, 19)

    def lambda_405B():
        OP_8F(0xFE, 0xFFFFD116, 0xC8, 0x2AA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_405B)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 18)
    SetChrSubChip(0xB, 0)
    Return()

    # Function_13_403A end

    def Function_14_4080(): pass

    label("Function_14_4080")

    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -21540, 200, 4840, 45)
    SetChrChipByIndex(0xA, 21)

    def lambda_40A1():
        OP_8F(0xFE, 0xFFFFD116, 0xC8, 0x2AA8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_40A1)
    WaitChrThread(0xA, 0x1)
    SetChrChipByIndex(0xA, 20)
    SetChrSubChip(0xA, 0)
    Return()

    # Function_14_4080 end

    def Function_15_40C6(): pass

    label("Function_15_40C6")

    SetChrPos(0xFE, -7380, 200, 5270, 0)
    OP_8E(0xFE, 0xFFFFEF0C, 0xC8, 0x3656, 0x1388, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_15_40C6 end

    def Function_16_40F3(): pass

    label("Function_16_40F3")

    SetChrPos(0xFE, -7380, 200, 5270, 0)
    OP_8E(0xFE, 0xFFFFEA84, 0xC8, 0x385E, 0x1388, 0x0)
    TurnDirection(0xFE, 0x9, 0)
    Return()

    # Function_16_40F3 end

    def Function_17_4120(): pass

    label("Function_17_4120")

    Sleep(500)
    SetChrPos(0xF8, -7380, 200, 5270, 0)
    SetChrPos(0xF9, -7380, 200, 5270, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4196")
    OP_8E(0xF9, 0xFFFFE6EC, 0xC8, 0x3A20, 0x1388, 0x0)
    TurnDirection(0xF9, 0x9, 400)
    SetChrFlags(0x109, 0x80)
    SetChrPos(0x109, -50000, -50000, -50000, 0)
    Jump("loc_41C7")

    label("loc_4196")

    OP_8E(0xF8, 0xFFFFE6EC, 0xC8, 0x3A20, 0x1388, 0x0)
    TurnDirection(0xF8, 0x9, 400)
    SetChrFlags(0x109, 0x80)
    SetChrPos(0x109, -50000, -50000, -50000, 0)

    label("loc_41C7")

    Jump("loc_421D")

    label("loc_41CA")


    def lambda_41D0():
        OP_8E(0xFE, 0xFFFFE6EC, 0xC8, 0x3A20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_41D0)
    Sleep(500)

    def lambda_41F0():
        OP_8E(0xFE, 0xFFFFF20E, 0xC8, 0x3426, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_41F0)
    WaitChrThread(0xF9, 0x1)
    TurnDirection(0xF9, 0x9, 400)
    WaitChrThread(0xF8, 0x1)
    TurnDirection(0xF8, 0x9, 400)

    label("loc_421D")

    Return()

    # Function_17_4120 end

    def Function_18_421E(): pass

    label("Function_18_421E")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -21630, 200, -350, 45)
    OP_8E(0xFE, 0xFFFFD6CA, 0xC8, 0x1D4C, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 18)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_18_421E end

    def Function_19_4258(): pass

    label("Function_19_4258")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -21260, 200, 2100, 45)
    OP_8E(0xFE, 0xFFFFD33C, 0xC8, 0x2238, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 20)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_19_4258 end

    def Function_20_4292(): pass

    label("Function_20_4292")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -21630, 200, -350, 45)
    OP_8E(0xFE, 0xFFFFD12A, 0xC8, 0x17FC, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_20_4292 end

    def Function_21_42CC(): pass

    label("Function_21_42CC")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -21630, 200, -350, 45)
    OP_8E(0xFE, 0xFFFFD3D2, 0xC8, 0x13D8, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 29)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_21_42CC end

    def Function_22_4306(): pass

    label("Function_22_4306")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -21630, 200, -350, 45)
    OP_8E(0xFE, 0xFFFFCEA0, 0xC8, 0x1D1A, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 31)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_22_4306 end

    def Function_23_4340(): pass

    label("Function_23_4340")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -21910, 200, 280, 45)
    OP_8E(0xFE, 0xFFFFCA90, 0xC8, 0x1CFC, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 33)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_23_4340 end

    def Function_24_437A(): pass

    label("Function_24_437A")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -21630, 200, -350, 45)
    OP_8E(0xFE, 0xFFFFCF0E, 0xC8, 0xE74, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 35)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_24_437A end

    def Function_25_43B4(): pass

    label("Function_25_43B4")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -21910, 200, 280, 45)
    OP_8E(0xFE, 0xFFFFC63A, 0xC8, 0x177A, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 37)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_25_43B4 end

    def Function_26_43EE(): pass

    label("Function_26_43EE")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -21630, 200, -350, 45)
    OP_8E(0xFE, 0xFFFFCD1A, 0xC8, 0x16C6, 0x1388, 0x0)
    Return()

    # Function_26_43EE end

    def Function_27_441E(): pass

    label("Function_27_441E")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -21910, 200, 280, 45)
    OP_8E(0xFE, 0xFFFFCAFE, 0xC8, 0xEEC, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 25)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_27_441E end

    def Function_28_4458(): pass

    label("Function_28_4458")

    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -21630, 200, -350, 45)
    OP_8E(0xFE, 0xFFFFC73E, 0xC8, 0x10F4, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 23)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_28_4458 end

    def Function_29_4492(): pass

    label("Function_29_4492")

    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 19)
    OP_8E(0xFE, 0xFFFFACE0, 0xC8, 0xFFFFFE0C, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF2810, 0xC8, 0xFFFFFE0C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_4492 end

    def Function_30_44CC(): pass

    label("Function_30_44CC")

    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 21)
    OP_8E(0xFE, 0xFFFFAC40, 0xC8, 0x4BA, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF2770, 0xC8, 0x4BA, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_30_44CC end

    def Function_31_4506(): pass

    label("Function_31_4506")

    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 28)
    OP_8E(0xFE, 0xFFFFA7A4, 0xC8, 0x29E, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF27CA, 0xC8, 0xFFFFFF24, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_31_4506 end

    def Function_32_4540(): pass

    label("Function_32_4540")

    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 30)
    OP_8E(0xFE, 0xFFFFAC9A, 0xC8, 0xFFFFFF60, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF2608, 0xC8, 0xFFFFFD9E, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_32_4540 end

    def Function_33_457A(): pass

    label("Function_33_457A")

    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 32)
    OP_8E(0xFE, 0xFFFFAA92, 0xC8, 0x640, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF27CA, 0xC8, 0x226, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_33_457A end

    def Function_34_45B4(): pass

    label("Function_34_45B4")

    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 34)
    OP_8E(0xFE, 0xFFFFA86C, 0xC8, 0x550, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF268A, 0xC8, 0x41A, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_34_45B4 end

    def Function_35_45EE(): pass

    label("Function_35_45EE")

    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 36)
    OP_8E(0xFE, 0xFFFFA7E0, 0xC8, 0xFFFFFF38, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF26C6, 0xC8, 0x5BE, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_35_45EE end

    def Function_36_4628(): pass

    label("Function_36_4628")

    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 38)
    OP_8E(0xFE, 0xFFFFA614, 0xC8, 0x3AC, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF291E, 0xC8, 0x8A2, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_36_4628 end

    def Function_37_4662(): pass

    label("Function_37_4662")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xFFFFA4CA, 0xB4, 0xFFFFFD8A, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF25EA, 0xC8, 0x44C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_37_4662 end

    def Function_38_4697(): pass

    label("Function_38_4697")

    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 26)
    OP_8E(0xFE, 0xFFFFA57E, 0xBE, 0x1D6, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF272A, 0xC8, 0xFFFFF7F4, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_38_4697 end

    def Function_39_46D1(): pass

    label("Function_39_46D1")

    OP_8C(0xFE, 270, 400)
    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0xFFFFA39E, 0xAA, 0x3E8, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF25CC, 0xC8, 0xFFFFFB8C, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_39_46D1 end

    def Function_40_470B(): pass

    label("Function_40_470B")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xFFFFA7B8, 0xC8, 0xFFFFFAE2, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF26D0, 0xC8, 0xFFFFFAE2, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_40_470B end

    def Function_41_4740(): pass

    label("Function_41_4740")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xFFFFAB1E, 0xC8, 0x244, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFF264E, 0xC8, 0x244, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_41_4740 end

    def Function_42_4775(): pass

    label("Function_42_4775")

    OP_24(0x144, 0x5A)
    Sleep(300)
    OP_24(0x144, 0x50)
    Sleep(300)
    OP_24(0x144, 0x46)
    Sleep(300)
    OP_24(0x144, 0x3C)
    Sleep(300)
    OP_24(0x144, 0x32)
    Sleep(300)
    OP_24(0x144, 0x28)
    Sleep(300)
    OP_24(0x144, 0x1E)
    Sleep(300)
    OP_24(0x144, 0x14)
    Sleep(300)
    OP_23(0x144)
    Return()

    # Function_42_4775 end

    SaveToFile()

Try(main)
