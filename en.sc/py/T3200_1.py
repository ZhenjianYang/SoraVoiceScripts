from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3200_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3200_1 ._SN',
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
        "Function_1_1AA",          # 01, 1
        "Function_2_1D3",          # 02, 2
        "Function_3_1E8",          # 03, 3
        "Function_4_4E1",          # 04, 4
        "Function_5_51E",          # 05, 5
        "Function_6_547",          # 06, 6
        "Function_7_570",          # 07, 7
        "Function_8_599",          # 08, 8
        "Function_9_5EA",          # 09, 9
        "Function_10_710",         # 0A, 10
        "Function_11_B31",         # 0B, 11
        "Function_12_1A26",        # 0C, 12
        "Function_13_2755",        # 0D, 13
        "Function_14_37EF",        # 0E, 14
        "Function_15_4533",        # 0F, 15
        "Function_16_45D6",        # 10, 16
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_22(0x1C7, 0x1, 0x64)
    SetChrPos(0x17, 67620, 3420, 25770, 170)
    SetChrPos(0x18, 61980, 3020, 26800, 125)
    SetChrPos(0x19, 62800, 3020, 25140, 125)
    SetChrPos(0x1A, 61950, 3020, 23550, 125)
    SetChrPos(0x1B, 73010, 3020, 25590, 215)
    SetChrPos(0x1C, 67620, 3020, 25770, 170)
    SetChrChipByIndex(0x101, 19)
    SetChrChipByIndex(0x107, 24)
    Sleep(2000)
    FadeToBright(1000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_176")
    SetChrChipByIndex(0x106, 21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15C")
    SetChrChipByIndex(0x105, 23)
    Call(1, 11)

    label("loc_15C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_173")
    SetChrChipByIndex(0x104, 22)
    Call(1, 12)

    label("loc_173")

    Jump("loc_1A9")

    label("loc_176")

    SetChrChipByIndex(0x103, 20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_192")
    SetChrChipByIndex(0x105, 23)
    Call(1, 13)

    label("loc_192")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A9")
    SetChrChipByIndex(0x104, 22)
    Call(1, 14)

    label("loc_1A9")

    Return()

    # Function_0_AA end

    def Function_1_1AA(): pass

    label("Function_1_1AA")

    OP_8E(0x17, 0xFC12, 0xD5C, 0x6626, 0x3E8, 0x0)
    OP_8E(0x17, 0xE48E, 0xD5C, 0x6F7C, 0x3E8, 0x0)
    Return()

    # Function_1_1AA end

    def Function_2_1D3(): pass

    label("Function_2_1D3")

    OP_8E(0x17, 0xE48E, 0xFB3, 0x6F7C, 0x1388, 0x0)
    Return()

    # Function_2_1D3 end

    def Function_3_1E8(): pass

    label("Function_3_1E8")

    OP_4A(0x17, 255)
    OP_20(0x7D0)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    TurnDirection(0x18, 0x101, 0)
    TurnDirection(0x19, 0x101, 0)
    TurnDirection(0x1A, 0x101, 0)
    TurnDirection(0x1C, 0x101, 0)
    TurnDirection(0x18, 0x101, 0)

    def lambda_2C7():
        TurnDirection(0x17, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2C7)

    def lambda_2D5():
        OP_96(0x18, 0x1022A, 0xFB3, 0x6450, 0x578, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2D5)

    def lambda_2F3():
        OP_96(0x19, 0xF550, 0xFB3, 0x6234, 0x578, 0x7D0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2F3)

    def lambda_311():
        OP_96(0x1A, 0xF1FE, 0xFB3, 0x5BFE, 0x578, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_311)

    def lambda_32F():
        OP_96(0x1C, 0x10824, 0xFB3, 0x64AA, 0x578, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_32F)
    OP_96(0x1B, 0x11D32, 0xFB3, 0x63F6, 0x578, 0x7D0)
    OP_63(0x17)
    OP_63(0x18)
    OP_63(0x19)
    OP_63(0x1A)
    OP_63(0x1B)
    OP_63(0x1C)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_1D(0x29)
    Sleep(400)

    ChrTalk(    #0
        0x101,
        "#444F#2P*cough* *cough*!!\x02",
    )

    CloseMessageWindow()
    OP_23(0x1C7)
    SetChrChipByIndex(0x17, 28)
    SetChrChipByIndex(0x18, 26)
    SetChrChipByIndex(0x19, 26)
    SetChrChipByIndex(0x1A, 12)
    SetChrChipByIndex(0x1B, 12)
    SetChrChipByIndex(0x1C, 12)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_4B(0x17, 255)
    OP_43(0x17, 0x0, 0x1, 0x2)

    def lambda_44B():
        OP_8E(0x18, 0xDEF8, 0xFB3, 0x5B04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_44B)
    Sleep(40)

    def lambda_46B():
        OP_8E(0x19, 0xDEF8, 0xFB3, 0x5B04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_46B)
    Sleep(70)

    def lambda_48B():
        OP_8E(0x1A, 0xDEF8, 0xFB3, 0x5B04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_48B)
    Sleep(100)

    def lambda_4AB():
        OP_8E(0x1B, 0xDEF8, 0xFB3, 0x5B04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4AB)
    Sleep(40)

    def lambda_4CB():
        OP_8E(0x1C, 0xDEF8, 0xFB3, 0x5B04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_4CB)
    Return()

    # Function_3_1E8 end

    def Function_4_4E1(): pass

    label("Function_4_4E1")

    OP_8E(0x17, 0xED30, 0xFB3, 0x65A4, 0xFA0, 0x0)
    OP_8E(0x17, 0xE010, 0xFB3, 0x67C0, 0xFA0, 0x0)
    OP_8E(0x17, 0xD6A6, 0xFB3, 0x67C0, 0xFA0, 0x0)
    Return()

    # Function_4_4E1 end

    def Function_5_51E(): pass

    label("Function_5_51E")

    OP_8E(0x18, 0xE02E, 0xFB3, 0x6B12, 0xFA0, 0x0)
    OP_8E(0x18, 0xD656, 0xFB3, 0x6B12, 0xFA0, 0x0)
    Return()

    # Function_5_51E end

    def Function_6_547(): pass

    label("Function_6_547")

    OP_8E(0x19, 0xDFDE, 0xFB3, 0x5866, 0xFA0, 0x0)
    OP_8E(0x19, 0xCAA8, 0xFB3, 0x5596, 0xFA0, 0x0)
    Return()

    # Function_6_547 end

    def Function_7_570(): pass

    label("Function_7_570")

    OP_8E(0x1A, 0xE402, 0xFB3, 0x5190, 0xFA0, 0x0)
    OP_8E(0x1A, 0xCCA6, 0xFB3, 0x456A, 0xFA0, 0x0)
    Return()

    # Function_7_570 end

    def Function_8_599(): pass

    label("Function_8_599")

    OP_8E(0x1B, 0x108D8, 0xEEC, 0x619E, 0xFA0, 0x0)
    OP_8E(0x1B, 0xF64A, 0xF50, 0x632E, 0xFA0, 0x0)
    OP_8E(0x1B, 0xE182, 0xFB3, 0x65AE, 0xFA0, 0x0)
    OP_8E(0x1B, 0xD6B0, 0xFB3, 0x65AE, 0xFA0, 0x0)
    Return()

    # Function_8_599 end

    def Function_9_5EA(): pass

    label("Function_9_5EA")

    OP_8E(0x1C, 0xF8E8, 0xEEC, 0x5D0C, 0xFA0, 0x0)
    OP_8E(0x1C, 0xF244, 0xEEC, 0x5456, 0xFA0, 0x0)
    SetChrSubChip(0x1C, 1)
    OP_96(0x1C, 0xF62C, 0x3E8, 0x4C86, 0x64, 0xFA0)
    PlayEffect(0x1, 0x0, 0xFF, 63220, 1000, 19590, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_22(0xE4, 0x0, 0x64)

    def lambda_66E():
        OP_9E(0xFE, 0x1E, 0x0, 0x320, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_66E)
    Sleep(800)
    OP_8C(0x1C, 300, 0)
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x1C, 11)
    SetChrSubChip(0x1C, 2)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x1C, 0xF15E, 0x960, 0x4FC4, 0x9C4, 0x1388)
    SetChrChipByIndex(0x1C, 11)
    SetChrSubChip(0x1C, 6)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x1C, 0xEAA6, 0xEEC, 0x5492, 0x9C4, 0x1388)
    SetChrChipByIndex(0x1C, 12)
    SetChrSubChip(0x1C, 0)
    OP_22(0x81, 0x0, 0x64)
    OP_8E(0x1C, 0xD034, 0xFB3, 0x64A0, 0xFA0, 0x0)
    Return()

    # Function_9_5EA end

    def Function_10_710(): pass

    label("Function_10_710")

    OP_44(0x17, 0x0)
    LoadEffect(0x1, "map\\\\sibuki0.eff")
    OP_EB(0x8F, 0x5)
    OP_EB(0x72, 0x5)
    OP_EB(0x74, 0x1)
    Fade(200)
    OP_6D(67620, 4500, 23820, 0)
    OP_67(0, 8700, -10000, 0)
    OP_6E(262, 0)
    OP_6C(350000, 0)
    OP_0D()

    def lambda_770():
        OP_8E(0xFE, 0x10176, 0xD5C, 0x64A0, 0x28A, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_770)
    Sleep(200)

    def lambda_790():

        label("loc_790")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_790")

    QueueWorkItem2(0x101, 3, lambda_790)
    SetChrFlags(0x101, 0x1000)

    def lambda_7A6():
        OP_8E(0xFE, 0x1066C, 0x3E8, 0x5744, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A6)

    ChrTalk(    #1 op#A op#5
        0x101,
        "#372F#3S#12A#5PHeeey!\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #2 op#A op#5
        0x101,
        "#372F#3S#17A#5PWaaait!!\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    WaitChrThread(0x17, 0x0)
    OP_20(0x7D0)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    ClearChrFlags(0x19, 0x80)

    def lambda_8C5():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_8C5)

    def lambda_8D3():
        OP_96(0xFE, 0x10176, 0xEEC, 0x64A0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8D3)

    def lambda_8F1():
        OP_96(0xFE, 0xF550, 0xEEC, 0x6234, 0x578, 0xBB8)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8F1)
    Sleep(50)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)

    def lambda_923():
        OP_96(0xFE, 0xF21C, 0xEEC, 0x68B0, 0x578, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_923)

    def lambda_941():
        OP_96(0xFE, 0x11D32, 0xEEC, 0x63F6, 0x578, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_941)

    def lambda_95F():
        OP_96(0xFE, 0x10824, 0xEEC, 0x64AA, 0x578, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_95F)
    Sleep(50)
    ClearChrFlags(0x1A, 0x80)

    def lambda_987():
        OP_96(0xFE, 0xF1FE, 0xEEC, 0x5BFE, 0x578, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_987)
    WaitChrThread(0x1A, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_1D(0x29)
    Sleep(400)
    OP_63(0x17)
    OP_63(0x18)
    OP_63(0x19)
    OP_63(0x1A)
    OP_63(0x1B)
    OP_63(0x1C)
    SetChrPos(0xF7, 63100, 1000, 17560, 0)
    SetChrFlags(0xF8, 0x8)
    SetChrFlags(0xF9, 0x8)

    ChrTalk(    #3
        0x101,
        "#444F#5P*cough* *cough*!!\x02",
    )

    CloseMessageWindow()
    OP_1D(0x29)
    OP_23(0x1C7)

    def lambda_A19():
        OP_6D(66470, 4500, 24570, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_A19)

    def lambda_A31():
        OP_6C(302000, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_A31)
    SetChrChipByIndex(0x17, 28)
    SetChrChipByIndex(0x18, 26)
    SetChrChipByIndex(0x19, 26)
    SetChrChipByIndex(0x1A, 12)
    SetChrChipByIndex(0x1B, 12)
    SetChrChipByIndex(0x1C, 12)
    SetChrSubChip(0x17, 0)
    SetChrSubChip(0x18, 0)
    SetChrSubChip(0x19, 0)
    SetChrSubChip(0x1A, 0)
    SetChrSubChip(0x1B, 0)
    SetChrSubChip(0x1C, 0)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x17, 0x1, 0x1, 0x4)
    OP_43(0x18, 0x1, 0x1, 0x5)
    OP_43(0x19, 0x1, 0x1, 0x6)
    OP_43(0x1A, 0x1, 0x1, 0x7)
    OP_43(0x1B, 0x1, 0x1, 0x8)
    OP_43(0x1C, 0x1, 0x1, 0x9)
    OP_22(0x81, 0x0, 0x64)
    Sleep(300)
    OP_22(0x81, 0x0, 0x64)
    Sleep(300)
    OP_22(0x81, 0x0, 0x64)
    WaitChrThread(0xF7, 0x0)
    Sleep(500)
    Return()

    # Function_10_710 end

    def Function_11_B31(): pass

    label("Function_11_B31")

    SetChrPos(0x101, 66830, 1000, 19670, 155)
    SetChrPos(0x106, 64610, 1000, 16420, 200)
    SetChrPos(0x107, 66280, 1000, 18830, 110)
    SetChrPos(0x105, 67940, 1000, 19460, 200)
    Call(1, 15)

    ChrTalk(    #4
        0x101,
        (
            "#377F#6PAhhh, it's so relaxing...\x02\x03",

            "Yup, outdoor baths are the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x105,
        "#1416F#4PYes, the wind feels wonderful.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #6
        0x101,
        "#370F#6PKloe, have you been to this bath before?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #7
        0x105,
        (
            "#1410F#4PNo, this is my first time in an outdoor bath.\x02\x03",

            "#1415FWhen I came here publicly before,\x01",
            "I just used the indoors area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#370F#6PAh, got'cha. So you have been here before.\x02\x03",

            "#442FStill, this beats the indoor bath hands down.\x01",
            "Looking up at the blue sky like this is\x01",
            "really nice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x107,
        (
            "#395F#3PHeehee, that's right, last time we went\x01",
            "was at night.\x02\x03",

            "#396FIt's nice to get in during the day too, though.\x02\x03",

            "Since the air's a bit chilly, the hot water\x01",
            "feels woooonderful.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E17():
        TurnDirection(0x105, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E17)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #10
        0x101,
        (
            "#370F#4PHaha. Sounds like you're a real bath connoisseur.\x01",
            "Just what I'd expect from a local.\x02\x03",

            "So which do you prefer, Tita?\x01",
            "A daytime bath or night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x107,
        (
            "#390F#3PI like both...\x02\x03",

            "#396FAh, but season-wise, I like it best\x01",
            "when it's snowing!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #12
        0x101,
        (
            "#374F#4PS-Snow?!\x02\x03",

            "That's, like, in the middle of winter.\x01",
            "Wouldn't you freeze your butt off outside?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x107,
        (
            "#396F#3POh, it's fine in the bath.\x02\x03",

            "#395FThe snow's falling all around,\x01",
            "but you're all snugly warm...\x02\x03",

            "I kinda like that feeling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        "#1416F#4PHow lovely. A bath in the snow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#371F#4PYeah, that does sound pretty good.\x01",
            "I'd love to do that once.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10A5():
        OP_6D(65670, 1000, 18470, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10A5)
    TurnDirection(0x106, 0x101, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #16
        0x106,
        (
            "#1425F#3PHey, don't get too caught up in talking.\x02\x03",

            "Especially you, Estelle.\x01",
            "Remember our main job.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1131():
        TurnDirection(0x101, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1131)
    Sleep(350)

    def lambda_1144():
        TurnDirection(0x107, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1144)
    Sleep(100)
    OP_8C(0x105, 200, 400)

    ChrTalk(    #17
        0x101,
        (
            "#445F#4PY-Yeah, I get that, Agate, but...\x02\x03",

            "#444F#4PWhy did you leave your bandana on...?\x02\x03",

            "Honestly, the way you look\x01",
            "is kinda stand-offish.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #18
        0x107,
        "#395F#4PAhaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x106,
        (
            "#1422F#3PWhether I stand off or stand in,\x01",
            "it's got nothin' to do with you.\x02\x03",

            "I don't do anything without this on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#442F#4PWell, I guess everyone's free to do as\x01",
            "they want, but...\x02\x03",

            "...\x02\x03",

            "#374FYou don't wash your face with that on,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x106,
        (
            "#1426F#3P#3SGah! Use common sense, will you!#2S\x02\x03",

            "Of course I take it off then!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#377F#4PPhew! Thank goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x107,
        (
            "#395F#4PHeehee... Y-Yeah.\x02\x03",

            "He does take it off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x106,
        (
            "#1424F#3PA-Are you two idiots?!\x02\x03",

            "What the hell do you think I am?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#378F#4PHmmm, I dunno, Agate.\x01",
            "It seems really plausible for you.\x02\x03",

            "You seem like the type to do any\x01",
            "crazy thing you set your mind to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x106,
        (
            "#1427F#3PUh, you know, that and this are...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#370F#4PHuh?\x02\x03",

            "Why're you so quiet all of a sudden?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        (
            "#1422F#3PHmph...\x02\x03",

            "#1420FLooks like they're here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #29
        0x107,
        "#393F#4PAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x105,
        "#1412F#4POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#374F#4PTh-The peeping tom's here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x106,
        (
            "#1425F#3P(Estelle, you see that brush to the north?)\x02\x03",

            "(Check it out SUBTLY so they don't notice.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#445F#4P(G-Got it...)\x02",
    )

    CloseMessageWindow()
    OP_43(0x17, 0x0, 0x0, 0x2)
    ClearChrFlags(0x17, 0x80)
    Call(1, 16)
    Sleep(1000)

    ChrTalk(    #34
        0x101,
        "#445F#2P(I-It does look like something's there.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x106,
        "#1425F#2P(Yeah, most likely that's our 'peeping tom.')\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrPos(0x101, 66830, 1000, 19670, 200)
    SetChrPos(0x107, 66280, 1000, 18830, 200)
    SetChrPos(0x105, 67940, 1000, 19460, 200)
    SetChrPos(0x106, 64610, 1000, 16420, 200)
    TurnDirection(0x106, 0x101, 0)
    OP_6D(65670, 1000, 18470, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(335000, 0)
    OP_0D()

    ChrTalk(    #36
        0x105,
        (
            "#1413F(But, what should we do?)\x02\x03",

            "(Even if we wanted to try to catch him,\x01",
            "we can't lay a finger on him from here.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#445F#4P(Yeah, someone needs to get\x01",
            "out first and go around.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x106,
        (
            "#1425F#3P(Looks like that's our only choice.)\x02\x03",

            "(All right, Estelle and I will go behind him.)\x02\x03",

            "(Princess, you two draw the enemy's attention.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x105,
        "#1412F(Yes, understood.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x107,
        "#398F#4P(Y-Yes!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#445F#4P(Well, then, let's...)\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x17, 400)

    ChrTalk(    #42
        0x101,
        "#374F#4P(...Wait, wh-what?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x106,
        "#1421F#3P(What is it?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#374F#4P(Look! They're gonna run!)\x02",
    )

    CloseMessageWindow()

    def lambda_19A2():
        TurnDirection(0x106, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_19A2)

    def lambda_19B0():
        TurnDirection(0x105, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_19B0)
    TurnDirection(0x107, 0x17, 400)
    OP_59()
    Call(1, 10)

    ChrTalk(    #45
        0x106,
        "#1423F#2PEstelle! After 'em!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x3)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #46
        0x101,
        "#372F#2PG-Got it!!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/R3101   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_11_B31 end

    def Function_12_1A26(): pass

    label("Function_12_1A26")

    SetChrPos(0x101, 66830, 1000, 19670, 155)
    SetChrPos(0x106, 64610, 1000, 16420, 200)
    SetChrPos(0x107, 66280, 1000, 18830, 110)
    SetChrPos(0x104, 67940, 1000, 19460, 200)
    Call(1, 15)

    ChrTalk(    #47
        0x101,
        (
            "#377F#6PAhhh, it's so relaxing...\x02\x03",

            "Yup, outdoor baths are the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x104,
        (
            "#1401F#4PHeh, I agree.\x02\x03",

            "I was also most charmed by the sights here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#442F#6POh, right, you stayed here, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x104,
        (
            "#1400F#4PIndeed, I soaked up quite a bit of Elmo's charms\x01",
            "after the birthday celebrations.\x02\x03",

            "I invited Schera as well,\x01",
            "but sadly she was busy...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_1BFC():
        TurnDirection(0x107, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1BFC)
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #51
        0x101,
        "#374F#6PWhoa! You invited Schera?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x107,
        (
            "#393F#3PUm, um...\x02\x03",

            "Olivier?\x02\x03",

            "Do, um, do you and Schera have\x01",
            "a special kind of relationship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x104,
        (
            "#1401F#4PHa ha! I leave it to your imagination.\x02\x03",

            "However, fear not.\x01",
            "Now I am yours alone, little Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x107,
        "#394F#3PH-Huh?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 0, 400)

    ChrTalk(    #55
        0x106,
        "#1425F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#443F#6PHey, Olivier.\x02\x03",

            "The scary big brother over there's\x01",
            "glaring at you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 200, 400)

    ChrTalk(    #57
        0x104,
        (
            "#1403F#4PMmm, yes. I can feel his hot gaze\x01",
            "upon my being most keenly.\x02\x03",

            "#1401FOh! Perhaps he is lonely. Agate, would you\x01",
            "like to join the conversation?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E22():
        OP_6D(65670, 1000, 18470, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E22)
    TurnDirection(0x106, 0x101, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #58
        0x106,
        (
            "#1422F#3P...Whatever.\x01",
            "Don't forget the reason we came here.\x02\x03",

            "#1420FDon't let your guard down.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1EA9():
        OP_8C(0x101, 200, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1EA9)
    Sleep(350)
    OP_8C(0x107, 200, 400)

    ChrTalk(    #59
        0x101,
        (
            "#445F#4PY-Yeah, I get that, Agate, but...\x02\x03",

            "#444F#4PWhy did you leave your bandana on...?\x02\x03",

            "Honestly, the way you look\x01",
            "is kinda stand-offish.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x107,
        "#395F#4PAhaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x106,
        (
            "#1422F#3PWhether I stand off or stand in,\x01",
            "it's got nothin' to do with you.\x02\x03",

            "I don't do anything without this on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x104,
        (
            "#1404F#4PIt's true that everyone's free\x01",
            "to do as they please, but...\x02\x03",

            "...\x02\x03",

            "#1403FDo you wash your hair with that on?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x106,
        (
            "#1426F#3P#3SGah! Use common sense, will you!#2S\x02\x03",

            "Of course I take it off then!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#377F#4PPhew! Thank goodness.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x107,
        (
            "#395F#4PHeehee... Y-Yeah.\x02\x03",

            "He does take it off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x106,
        (
            "#1424F#3PA-Are you two idiots?!\x02\x03",

            "What the hell do you think I am?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#378F#4PHmmm, I dunno, Agate.\x01",
            "It seems really plausible for you.\x02\x03",

            "You seem like the type to do any\x01",
            "crazy thing you set your mind to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x106,
        (
            "#1427F#3PUh, you know, that and this are...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#370F#4PHuh?\x02\x03",

            "Why're you so quiet all of a sudden?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x106,
        (
            "#1422F#3PHmph...\x02\x03",

            "#1420FLooks like they're here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #71
        0x107,
        "#393F#4PAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#374F#4PTh-The peeping tom's here?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x106,
        (
            "#1425F#3P(Estelle, you see that brush to the north?)\x02\x03",

            "(Check it out SUBTLY so they don't notice.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#445F(G-Got it...)\x02",
    )

    CloseMessageWindow()
    OP_43(0x17, 0x0, 0x0, 0x2)
    ClearChrFlags(0x17, 0x80)
    Call(1, 16)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        "#445F#2P(I-It does look like something's there.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x106,
        "#1425F#2P(Yeah, most likely that's our 'peeping tom.')\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrPos(0x101, 66830, 1000, 19670, 200)
    SetChrPos(0x107, 66280, 1000, 18830, 200)
    SetChrPos(0x104, 67940, 1000, 19460, 200)
    SetChrPos(0x106, 64610, 1000, 16420, 200)
    TurnDirection(0x106, 0x101, 0)
    OP_6D(65670, 1000, 18470, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(335000, 0)
    OP_0D()

    ChrTalk(    #77
        0x104,
        (
            "#1402F#4P(But, what should we do?)\x02\x03",

            "(Even if we wanted to try to catch him,\x01",
            "we can't lay a finger on him from here.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#445F#4P(Yeah, someone needs to get\x01",
            "out first and go around.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x106,
        (
            "#1425F#3P(Looks like that's our only choice.)\x02\x03",

            "(All right, Estelle and I will go behind him.)\x02\x03",

            "(Olivier, you two draw the enemy's attention.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x107,
        "#398F#4P(Y-Yes!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x104,
        "#1400F(Heh, understood.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#445F#4P(Well, then, let's...)\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x17, 400)

    ChrTalk(    #83
        0x101,
        "#374F#4P(...Wait, wh-what?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x106,
        "#1421F#3P(What is it?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#374F#4P(Look! They're gonna run!)\x02",
    )

    CloseMessageWindow()

    def lambda_26D1():
        TurnDirection(0x106, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_26D1)

    def lambda_26DF():
        TurnDirection(0x104, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_26DF)
    TurnDirection(0x107, 0x17, 400)
    OP_59()
    Call(1, 10)

    ChrTalk(    #86
        0x106,
        "#1423F#2PEstelle! After 'em!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x3)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #87
        0x101,
        "#372F#2PG-Got it!!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/R3101   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1A26 end

    def Function_13_2755(): pass

    label("Function_13_2755")

    SetChrPos(0x101, 66830, 1000, 19670, 155)
    SetChrPos(0x103, 65900, 1000, 18260, 108)
    SetChrPos(0x107, 66310, 1000, 19250, 153)
    SetChrPos(0x105, 68340, 1000, 19480, 200)
    Call(1, 15)

    ChrTalk(    #88
        0x101,
        (
            "#377F#6PAhhh, it's so relaxing...\x02\x03",

            "Yup, outdoor baths are the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x105,
        "#1416F#4PYes, the wind feels wonderful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x103,
        (
            "#1391F#3PHeehee. It truly is paradise.\x02\x03",

            "If I just had a drink, it'd be perfect.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 200, 400)

    ChrTalk(    #91
        0x101,
        (
            "#370F#4PHey, Schera. It doesn't matter much, but... \x02\x03",

            "Aren't you gonna let your hair down?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28D5():
        OP_8C(0x107, 200, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_28D5)
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #92
        0x103,
        (
            "#1390F#3PMmm, I think not. This way I can don my\x01",
            "clothes and jump out quickly, no?\x02\x03",

            "If I let it down, it'll take time to tie it\x01",
            "back up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#442F#4POh, good point. Who knows when the\x01",
            "criminal might show up, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 155, 400)

    ChrTalk(    #94
        0x107,
        (
            "#395FBut, thanks to that criminal we can\x01",
            "all go into the bath together.\x02\x03",

            "Heehee. I know it's a case, but I'm\x01",
            "a little thankful.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 300, 400)

    ChrTalk(    #95
        0x105,
        (
            "#1410F#4PI get what you mean.\x02\x03",

            "Being together like this really makes\x01",
            "it feel like a vacation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #96
        0x101,
        (
            "#371FGiven that we've got four people, would that make\x01",
            "this a family trip, with parent and child?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x103,
        (
            "#1393F#3PParent or child in this group... I guess\x01",
            "that would make me Tita's mother?\x02\x03",

            "#1395FHow cruel, Estelle.\x01",
            "At least make us four sisters.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2BC2():
        OP_8C(0x101, 200, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BC2)
    OP_8C(0x107, 200, 400)

    ChrTalk(    #98
        0x107,
        "#390F#7POh. Well, that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x105,
        (
            "#1411F#4PHeehee...\x02\x03",

            "#1410FYou know, thinking about it, this is\x01",
            "the first time it's just been women.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C5D():
        OP_8C(0x101, 108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C5D)
    Sleep(100)

    def lambda_2C70():
        OP_8C(0x103, 108, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2C70)
    OP_8C(0x107, 108, 400)

    ChrTalk(    #100
        0x101,
        (
            "#370F#6PAh, now that you mention it, yeah.\x01",
            "Olivier's not here today...\x02\x03",

            "#443FIf he knew he was missing this, I'm sure\x01",
            "he'd run all the way back to Erebonia\x01",
            "crying his eyes out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x107,
        "#395F#6PAhaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x105,
        "#1415F#4PI... I could totally picture it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x103,
        (
            "#1396F#3PWell, let's keep it our little secret. I'd\x01",
            "rather not break hearts needlessly.\x02\x03",

            "It seems like Olivier really does\x01",
            "like these hot springs, anyway.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 200, 400)

    ChrTalk(    #104
        0x101,
        "#370F#4P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #105
        0x107,
        "#390FWhat is it, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#443F#4PHuh...? Uh, nothing...\x02\x03",

            "#442FBut, since it's come up, I guess I'll ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x107,
        "#393FHm?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 200, 400)

    ChrTalk(    #108
        0x101,
        "#378F#4PUm, Schera. Can I ask you a question?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)

    ChrTalk(    #109
        0x103,
        "#1393F#3POh, what's this all of a sudden?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#442F#4PUm, is there reeeeeally nothing going on\x01",
            "between you and Olivier?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2F97():
        TurnDirection(0x105, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2F97)
    Sleep(150)
    TurnDirection(0x107, 0x103, 400)

    ChrTalk(    #111
        0x105,
        "#1414F#4POh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        "#1393F#3PNothing... You mean like 'that'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#441F#4PY-Yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x103,
        (
            "#1391F#3PYou idiot. Of course there isn't.\x02\x03",

            "He's a drinking partner, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#378F#4PReally?\x02\x03",

            "Sometimes the way you two talk feels\x01",
            "like you're sharing a secret.\x02\x03",

            "It really feels like you understand each other,\x01",
            "so yeah, I'm curious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x107,
        "#396F#7P(*ba-dump* *ba-dump* *ba-dump*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#1396F#3PAhh, I see...\x02\x03",

            "So that's why this came up all of a sudden.\x02\x03",

            "Unfortunately, that's a work thing.\x01",
            "There are...circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        "#370F#4PCircumstances?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x103,
        (
            "#1390F#3PYes, but I'll explain it another time.\x02\x03",

            "This isn't the time to get sidetracked on\x01",
            "other things.\x02\x03",

            "We're here to investigate, so we need to\x01",
            "focus on the task at hand and be a bit more\x01",
            "aware of our surroundings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#379F#4PAhh, you're dodging the subject.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 300, 400)

    ChrTalk(    #121
        0x105,
        (
            "#1412F#4PBut, Estelle...\x02\x03",

            "...It seems Schera is right.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_3354():
        TurnDirection(0x103, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3354)
    Sleep(150)

    def lambda_3367():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3367)
    Sleep(150)
    OP_8C(0x107, 108, 400)

    ChrTalk(    #122
        0x101,
        "#374F#6PWhoa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x107,
        "#393F#3PAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x103,
        "#1392F#3P(Is the peeping tom here?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x105,
        "#1412F#4P(...Inside the brush on the north side.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#445F(Understood, the north side brush...)\x02",
    )

    CloseMessageWindow()
    OP_43(0x17, 0x0, 0x0, 0x2)
    ClearChrFlags(0x17, 0x80)
    Call(1, 16)
    Sleep(1000)

    ChrTalk(    #127
        0x101,
        "#445F#2P(I-It does look like something's there.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x103,
        "#1392F#2P(Perhaps it's our 'peeping tom.')\x02",
    )

    CloseMessageWindow()
    OP_59()
    SetChrPos(0x101, 66830, 1000, 19670, 155)
    SetChrPos(0x103, 65900, 1000, 18260, 108)
    SetChrPos(0x107, 66310, 1000, 19250, 153)
    SetChrPos(0x105, 68340, 1000, 19480, 200)
    Fade(1000)
    OP_6D(66760, 1000, 19250, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(335000, 0)
    OP_0D()

    ChrTalk(    #129
        0x105,
        (
            "#1413F#4P(But, what should we do?)\x02\x03",

            "(Even if we wanted to try to catch him,\x01",
            "we can't lay a finger on him from here.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#445F#6P(Yeah, someone needs to get\x01",
            "out first and go around.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x103,
        (
            "#1392F#3P(Estelle and I will go around behind him.)\x02\x03",

            "(Princess, Tita, draw the enemy's attention.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x105,
        "#1412F#4P(Yes, understood.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x107,
        "#398F#7P(Y-Yes!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        "#445F#6P(Well, then, let's...)\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x17, 400)

    ChrTalk(    #135
        0x101,
        "#374F#4P(...Wait, wh-what?!)\x02",
    )

    CloseMessageWindow()

    def lambda_36F3():
        OP_8C(0x103, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_36F3)
    Sleep(150)

    def lambda_3706():
        OP_8C(0x105, 300, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3706)
    Sleep(150)
    OP_8C(0x107, 0, 400)

    ChrTalk(    #136
        0x103,
        "#1393F#3P(What is it?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#374F#4P(Look! They're gonna run!)\x02",
    )

    CloseMessageWindow()

    def lambda_3765():
        OP_8C(0x105, 350, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3765)

    def lambda_3773():
        TurnDirection(0x103, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3773)
    TurnDirection(0x107, 0x17, 400)
    WaitChrThread(0x105, 0x1)
    OP_59()
    Call(1, 10)

    ChrTalk(    #138
        0x103,
        "#1394F#2PEstelle! After them!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x3)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #139
        0x101,
        "#372F#2PG-Got it!!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/R3101   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2755 end

    def Function_14_37EF(): pass

    label("Function_14_37EF")

    SetChrPos(0x101, 66830, 1000, 19670, 155)
    SetChrPos(0x103, 65900, 1000, 18260, 108)
    SetChrPos(0x107, 66310, 1000, 19250, 153)
    SetChrPos(0x104, 68340, 1000, 19480, 200)
    Call(1, 15)

    ChrTalk(    #140
        0x101,
        (
            "#377F#6PAhhh, it's so relaxing...\x02\x03",

            "Yup, outdoor baths are the best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x103,
        (
            "#1391F#3PIt truly is paradise.\x02\x03",

            "If I just had a drink, it'd be perfect.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 200, 400)

    ChrTalk(    #142
        0x101,
        (
            "#370F#4PHey, Schera. It doesn't matter much, but... \x02\x03",

            "Aren't you gonna let your hair down?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_393A():
        OP_8C(0x107, 200, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_393A)
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #143
        0x103,
        (
            "#1390F#3PMmm, I think not. This way I can don my\x01",
            "clothes and jump out quickly, no?\x02\x03",

            "If I let it down, it'll take time to tie it\x01",
            "back up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#442F#4POh, good point. Who knows when the\x01",
            "criminal might show up, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x104,
        (
            "#1404F#4PStill, it's a pity.\x02\x03",

            "I am sure Schera washing her\x01",
            "hair would be most charming.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 108, 400)

    ChrTalk(    #146
        0x103,
        "#1396F#3PYou'll have to get that another time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x104,
        (
            "#1401F#4PHeh, I see.\x02\x03",

            "Well, then, perhaps for a next chance I shall\x01",
            "invite you to a top class spa in my homeland.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#370F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #149
        0x107,
        "#390FWhat is it, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        (
            "#443F#4PHuh...? Uh, nothing...\x02\x03",

            "#442FIt's just...a little...suspicious, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x107,
        "#393FHuh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #152
        0x103,
        (
            "#1393F#3PSuspicious...?\x02\x03",

            "Do you mean me and Olivier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#441F#4PY-Yeah...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 200, 400)

    ChrTalk(    #154
        0x103,
        (
            "#1391F#3PYou idiot. There's nothing.\x02\x03",

            "He's a drinking partner, that's all.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #155
        0x104,
        (
            "#1401F#4PI...am afraid I shall have to humbly\x01",
            "refrain from accepting that title.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#378F#4PReally?\x02\x03",

            "Sometimes the way you two talk feels\x01",
            "like you're sharing a secret.\x02\x03",

            "It really feels like you understand each other,\x01",
            "so yeah, I'm curious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x107,
        "#396F#7P(*ba-dump* *ba-dump* *ba-dump*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x103,
        (
            "#1396F#3PAhh, I see...\x02\x03",

            "So that's why this came up all of a sudden.\x02\x03",

            "Unfortunately, that's a work thing.\x01",
            "There are...circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#370F#4PCircumstances?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x103,
        (
            "#1390F#3PYes, but I'll explain it another time.\x02\x03",

            "This isn't the time to get sidetracked on\x01",
            "other things.\x02\x03",

            "We're here to investigate, so we need to\x01",
            "focus on the task at hand and be a bit more\x01",
            "aware of our surroundings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#379F#4PAhh, you're dodging the subject.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x104,
        (
            "#1401F#4PHeh, however, it seems...coincidence is\x01",
            "a fearsome thing.\x02\x03",

            "We really MUST be on our guard.\x01",
            "Right now, in fact.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_405A():
        TurnDirection(0x103, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_405A)
    Sleep(150)

    def lambda_406D():
        OP_8C(0x101, 108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_406D)
    Sleep(150)
    OP_8C(0x107, 108, 400)

    ChrTalk(    #163
        0x101,
        "#374F#6PWhoa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x107,
        "#393F#3PAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x103,
        "#1392F#6P(Is the peeping tom here?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x104,
        (
            "#1402F#4P(You see that brush to the north,\x01",
            "right, Estelle?)\x02\x03",

            "(Check it, but move very carefully so\x01",
            "you're not noticed.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        "#445F#6P(G-Got it...)\x02",
    )

    CloseMessageWindow()
    OP_43(0x17, 0x0, 0x0, 0x2)
    ClearChrFlags(0x17, 0x80)
    Call(1, 16)
    Sleep(1000)

    ChrTalk(    #168
        0x101,
        "#445F#2P(I-It does look like something's there.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x103,
        "#1392F#2P(Perhaps it's our 'peeping tom.')\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrPos(0x101, 66830, 1000, 19670, 155)
    SetChrPos(0x103, 65900, 1000, 18260, 108)
    SetChrPos(0x107, 66310, 1000, 19250, 153)
    SetChrPos(0x104, 68340, 1000, 19480, 200)
    OP_6D(66760, 1000, 19250, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(335000, 0)
    OP_0D()

    ChrTalk(    #170
        0x104,
        (
            "#1402F#4P(Now, then, what shall we do...)\x02\x03",

            "(Even if we wanted to try and apprehend him,\x01",
            "we cannot lay a finger on him from here.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        (
            "#445F#6P(Yeah, someone needs to get\x01",
            "out first and go around.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x103,
        (
            "#1392F#3P(Estelle and I will go around behind him.)\x02\x03",

            "(Olivier, Tita, draw the enemy's attention.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x107,
        "#398F#7P(O-Okay!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x104,
        "#1400F#4P(Heh, understood.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#445F#6P(Well, then, let's...)\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x17, 400)

    ChrTalk(    #176
        0x101,
        "#374F#4P(...Wait, wh-what?!)\x02",
    )

    CloseMessageWindow()

    def lambda_4437():
        OP_8C(0x103, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4437)
    Sleep(150)

    def lambda_444A():
        OP_8C(0x104, 300, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_444A)
    Sleep(150)
    OP_8C(0x107, 0, 400)

    ChrTalk(    #177
        0x103,
        "#1393F#3P(What is it?!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        "#374F#4P(Look! They're gonna run!)\x02",
    )

    CloseMessageWindow()

    def lambda_44A9():
        OP_8C(0x104, 350, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_44A9)

    def lambda_44B7():
        TurnDirection(0x103, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_44B7)
    TurnDirection(0x107, 0x17, 400)
    WaitChrThread(0x104, 0x1)
    OP_59()
    Call(1, 10)

    ChrTalk(    #179
        0x103,
        "#1394F#2PEstelle! After them!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x3)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #180
        0x101,
        "#372F#2PG-Got it!!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/R3101   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_14_37EF end

    def Function_15_4533(): pass

    label("Function_15_4533")

    OP_6D(65820, 2000, 7860, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(80000, 0)
    OP_6E(246, 0)

    def lambda_4576():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4576)
    OP_6D(65820, 2000, 17860, 6000)
    Fade(2000)
    OP_22(0xA2, 0x0, 0x64)
    OP_6D(66760, 1000, 19250, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(335000, 0)
    OP_0D()
    Sleep(1000)
    Return()

    # Function_15_4533 end

    def Function_16_45D6(): pass

    label("Function_16_45D6")


    def lambda_45DC():
        OP_6D(67620, 4000, 23820, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_45DC)

    def lambda_45F4():
        OP_67(0, 3370, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_45F4)

    def lambda_460C():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_460C)

    def lambda_461C():
        OP_6C(350000, 3000)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_461C)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    Return()

    # Function_16_45D6 end

    SaveToFile()

Try(main)
