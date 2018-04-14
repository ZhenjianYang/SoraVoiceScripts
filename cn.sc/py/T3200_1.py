from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        "Function_1_192",          # 01, 1
        "Function_2_1BB",          # 02, 2
        "Function_3_1D0",          # 03, 3
        "Function_4_4C0",          # 04, 4
        "Function_5_4FD",          # 05, 5
        "Function_6_526",          # 06, 6
        "Function_7_54F",          # 07, 7
        "Function_8_578",          # 08, 8
        "Function_9_5C9",          # 09, 9
        "Function_10_6EF",         # 0A, 10
        "Function_11_B0A",         # 0B, 11
        "Function_12_17DF",        # 0C, 12
        "Function_13_2395",        # 0D, 13
        "Function_14_30EB",        # 0E, 14
        "Function_15_3B7E",        # 0F, 15
        "Function_16_3C21",        # 10, 16
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    OP_22(0x1C7, 0x1, 0x64)
    SetChrPos(0x17, 67620, 3420, 25770, 170)
    SetChrPos(0x18, 61980, 3020, 26800, 125)
    SetChrPos(0x19, 62800, 3020, 25140, 125)
    SetChrPos(0x1A, 61950, 3020, 23550, 125)
    SetChrPos(0x1B, 73010, 3020, 25590, 215)
    SetChrPos(0x1C, 67620, 3020, 25770, 170)
    SetChrChipByIndex(0x101, 19)
    SetChrChipByIndex(0x107, 24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_15E")
    SetChrChipByIndex(0x106, 21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_144")
    SetChrChipByIndex(0x105, 23)
    Call(1, 11)

    label("loc_144")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15B")
    SetChrChipByIndex(0x104, 22)
    Call(1, 12)

    label("loc_15B")

    Jump("loc_191")

    label("loc_15E")

    SetChrChipByIndex(0x103, 20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17A")
    SetChrChipByIndex(0x105, 23)
    Call(1, 13)

    label("loc_17A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_191")
    SetChrChipByIndex(0x104, 22)
    Call(1, 14)

    label("loc_191")

    Return()

    # Function_0_AA end

    def Function_1_192(): pass

    label("Function_1_192")

    OP_8E(0x17, 0xFC12, 0xD5C, 0x6626, 0x3E8, 0x0)
    OP_8E(0x17, 0xE48E, 0xD5C, 0x6F7C, 0x3E8, 0x0)
    Return()

    # Function_1_192 end

    def Function_2_1BB(): pass

    label("Function_2_1BB")

    OP_8E(0x17, 0xE48E, 0xFB3, 0x6F7C, 0x1388, 0x0)
    Return()

    # Function_2_1BB end

    def Function_3_1D0(): pass

    label("Function_3_1D0")

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

    def lambda_2AF():
        TurnDirection(0x17, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2AF)

    def lambda_2BD():
        OP_96(0x18, 0x1022A, 0xFB3, 0x6450, 0x578, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2BD)

    def lambda_2DB():
        OP_96(0x19, 0xF550, 0xFB3, 0x6234, 0x578, 0x7D0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2DB)

    def lambda_2F9():
        OP_96(0x1A, 0xF1FE, 0xFB3, 0x5BFE, 0x578, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2F9)

    def lambda_317():
        OP_96(0x1C, 0x10824, 0xFB3, 0x64AA, 0x578, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_317)
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
        "#444F#2P哈哈！！\x02",
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

    def lambda_42A():
        OP_8E(0x18, 0xDEF8, 0xFB3, 0x5B04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_42A)
    Sleep(40)

    def lambda_44A():
        OP_8E(0x19, 0xDEF8, 0xFB3, 0x5B04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_44A)
    Sleep(70)

    def lambda_46A():
        OP_8E(0x1A, 0xDEF8, 0xFB3, 0x5B04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_46A)
    Sleep(100)

    def lambda_48A():
        OP_8E(0x1B, 0xDEF8, 0xFB3, 0x5B04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_48A)
    Sleep(40)

    def lambda_4AA():
        OP_8E(0x1C, 0xDEF8, 0xFB3, 0x5B04, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_4AA)
    Return()

    # Function_3_1D0 end

    def Function_4_4C0(): pass

    label("Function_4_4C0")

    OP_8E(0x17, 0xED30, 0xFB3, 0x65A4, 0xFA0, 0x0)
    OP_8E(0x17, 0xE010, 0xFB3, 0x67C0, 0xFA0, 0x0)
    OP_8E(0x17, 0xD6A6, 0xFB3, 0x67C0, 0xFA0, 0x0)
    Return()

    # Function_4_4C0 end

    def Function_5_4FD(): pass

    label("Function_5_4FD")

    OP_8E(0x18, 0xE02E, 0xFB3, 0x6B12, 0xFA0, 0x0)
    OP_8E(0x18, 0xD656, 0xFB3, 0x6B12, 0xFA0, 0x0)
    Return()

    # Function_5_4FD end

    def Function_6_526(): pass

    label("Function_6_526")

    OP_8E(0x19, 0xDFDE, 0xFB3, 0x5866, 0xFA0, 0x0)
    OP_8E(0x19, 0xCAA8, 0xFB3, 0x5596, 0xFA0, 0x0)
    Return()

    # Function_6_526 end

    def Function_7_54F(): pass

    label("Function_7_54F")

    OP_8E(0x1A, 0xE402, 0xFB3, 0x5190, 0xFA0, 0x0)
    OP_8E(0x1A, 0xCCA6, 0xFB3, 0x456A, 0xFA0, 0x0)
    Return()

    # Function_7_54F end

    def Function_8_578(): pass

    label("Function_8_578")

    OP_8E(0x1B, 0x108D8, 0xEEC, 0x619E, 0xFA0, 0x0)
    OP_8E(0x1B, 0xF64A, 0xF50, 0x632E, 0xFA0, 0x0)
    OP_8E(0x1B, 0xE182, 0xFB3, 0x65AE, 0xFA0, 0x0)
    OP_8E(0x1B, 0xD6B0, 0xFB3, 0x65AE, 0xFA0, 0x0)
    Return()

    # Function_8_578 end

    def Function_9_5C9(): pass

    label("Function_9_5C9")

    OP_8E(0x1C, 0xF8E8, 0xEEC, 0x5D0C, 0xFA0, 0x0)
    OP_8E(0x1C, 0xF244, 0xEEC, 0x5456, 0xFA0, 0x0)
    SetChrSubChip(0x1C, 1)
    OP_96(0x1C, 0xF62C, 0x3E8, 0x4C86, 0x64, 0xFA0)
    PlayEffect(0x1, 0x0, 0xFF, 63220, 1000, 19590, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_22(0xE4, 0x0, 0x64)

    def lambda_64D():
        OP_9E(0xFE, 0x1E, 0x0, 0x320, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1C, 3, lambda_64D)
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

    # Function_9_5C9 end

    def Function_10_6EF(): pass

    label("Function_10_6EF")

    OP_44(0x17, 0x0)
    LoadEffect(0x1, "map\\\\sibuki0.eff")
    Fade(200)
    OP_6D(67620, 4500, 23820, 0)
    OP_67(0, 8700, -10000, 0)
    OP_6E(262, 0)
    OP_6C(350000, 0)
    OP_0D()

    def lambda_746():
        OP_8E(0xFE, 0x10176, 0xD5C, 0x64A0, 0x28A, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_746)
    Sleep(200)

    def lambda_766():

        label("loc_766")

        TurnDirection(0xFE, 0x17, 0)
        OP_48()
        Jump("loc_766")

    QueueWorkItem2(0x101, 3, lambda_766)
    SetChrFlags(0x101, 0x1000)

    def lambda_77C():
        OP_8E(0xFE, 0x1066C, 0x3E8, 0x5744, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77C)

    ChrTalk(    #1 op#A op#5
        0x101,
        "#372F#3S#12A#5P喂────！\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #2 op#A op#5
        0x101,
        "#372F#3S#17A#5P你给我等等──！！\x05\x02",
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

    def lambda_8AB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_8AB)

    def lambda_8B9():
        OP_96(0xFE, 0x10176, 0xEEC, 0x64A0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8B9)

    def lambda_8D7():
        OP_96(0xFE, 0xF550, 0xEEC, 0x6234, 0x578, 0xBB8)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_8D7)
    Sleep(50)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)

    def lambda_909():
        OP_96(0xFE, 0xF21C, 0xEEC, 0x68B0, 0x578, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_909)

    def lambda_927():
        OP_96(0xFE, 0x11D32, 0xEEC, 0x63F6, 0x578, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_927)

    def lambda_945():
        OP_96(0xFE, 0x10824, 0xEEC, 0x64AA, 0x578, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_945)
    Sleep(50)
    ClearChrFlags(0x1A, 0x80)

    def lambda_96D():
        OP_96(0xFE, 0xF1FE, 0xEEC, 0x5BFE, 0x578, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_96D)
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
        "#444F#2P哎？\x02",
    )

    CloseMessageWindow()
    OP_1D(0x29)
    OP_23(0x1C7)

    def lambda_9F2():
        OP_6D(66470, 4500, 24570, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_9F2)

    def lambda_A0A():
        OP_6C(302000, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_A0A)
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

    # Function_10_6EF end

    def Function_11_B0A(): pass

    label("Function_11_B0A")

    SetChrPos(0x101, 66830, 1000, 19670, 155)
    SetChrPos(0x106, 64610, 1000, 16420, 200)
    SetChrPos(0x107, 66280, 1000, 18830, 110)
    SetChrPos(0x105, 67940, 1000, 19460, 200)
    Call(1, 15)

    ChrTalk(    #4
        0x101,
        (
            "#377F#1P啊～真惬意～\x02\x03",

            "嗯，还是\x01",
            "露天浴令人心情舒畅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x105,
        "#1416F#2P嗯，这风也很舒服。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #6
        0x101,
        (
            "#370F#1P科洛丝以前\x01",
            "在这里洗过澡吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #7
        0x105,
        (
            "#1410F#2P不，这是我的第一次露天浴。\x02\x03",

            "#1415F以前因公来这里的时候\x01",
            "只是洗过室内浴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#370F#2P哦，这样啊。\x01",
            "就是说你以前来过这里喽。\x02\x03",

            "#442F呼，不过说起来\x01",
            "一边看着蓝天一边洗澡的\x01",
            "感觉真不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x107,
        (
            "#395F#1P嘿嘿，确实，\x01",
            "上回是晚上呢。\x02\x03",

            "#396F现在已经是晌午了，\x01",
            "不过一早来洗的话也很舒服哦。\x02\x03",

            "外边的空气比较凉，\x01",
            "也更能感觉到澡堂的温暖。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D39():
        TurnDirection(0x105, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D39)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #10
        0x101,
        (
            "#370F#2P不愧是土生土长的孩子，知道得真清楚啊。\x02\x03",

            "顺便问一下，提妲最喜欢\x01",
            "什么时候来洗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x107,
        (
            "#390F#1P嗯，早晚我都\x01",
            "很喜欢……\x02\x03",

            "#396F啊，不过论季节的话，\x01",
            "下雪的时候最好啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #12
        0x101,
        (
            "#374F#2P下、下雪！？\x02\x03",

            "那是隆冬吧。\x01",
            "赤身裸体的不冷？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x107,
        (
            "#396F#1P只要泡在热水里就没问题哦。\x02\x03",

            "#395F周围都在下雪，\x01",
            "可只有自己的身体是暖洋洋的……\x02\x03",

            "那种不可思议的感觉\x01",
            "总觉得很喜欢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        (
            "#1416F#2P真美妙啊。\x01",
            "雪中的露天浴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#371F#2P嗯嗯，真想\x01",
            "尝试一回啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F1F():
        OP_6D(65670, 1000, 18470, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F1F)
    TurnDirection(0x106, 0x101, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #16
        0x106,
        (
            "#1425F#1P喂，聊天是可以，\x01",
            "不过别太入迷了。\x02\x03",

            "尤其是艾丝蒂尔，\x01",
            "你可是在执行任务啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F9A():
        TurnDirection(0x101, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F9A)
    Sleep(350)

    def lambda_FAD():
        TurnDirection(0x107, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_FAD)
    Sleep(100)
    OP_8C(0x105, 200, 400)

    ChrTalk(    #17
        0x101,
        (
            "#445F#2P嗯、嗯……\x01",
            "知道了，不过阿加特……\x02\x03",

            "#444F#2P你、你为什么要\x01",
            "披着一块印花大手巾。\x02\x03",

            "老实说你那个样子\x01",
            "特别惹人注目。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #18
        0x107,
        "#395F#1P这、这个么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x106,
        (
            "#1422F#1P什么注目不注目的\x01",
            "我才不在乎。\x02\x03",

            "没这东西的话\x01",
            "我就提不起精神。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#442F#2P嗯，虽说这属于\x01",
            "个人的自由……\x02\x03",

            "………………………………\x01",
            "………………………………\x02\x03",

            "#374F不过你不会连洗头时\x01",
            "都扎着头巾吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x106,
        (
            "#1426F#1P#3S啊──！\x01",
            "你用常识考虑一下啊，常识！#2S\x02\x03",

            "那种时候\x01",
            "当然要拿下来了！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#377F#2P哈……还好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x107,
        (
            "#395F#1P嘿嘿……\x01",
            "是、是吗。\x02\x03",

            "果然还是会摘下来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x106,
        (
            "#1424F#1P你、你们都是傻瓜吗！？\x02\x03",

            "把我当成是\x01",
            "什么人了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#378F#2P嗯～我觉得阿加特\x01",
            "有可能会这么做啊。\x02\x03",

            "你是属于只要下了决定，就无论\x01",
            "多冒失的事情都做得出来的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x106,
        (
            "#1427F#1P我说啊，这根本就是\x01",
            "两码事…………………\x02\x03",

            "……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#370F#2P？？？\x02\x03",

            "怎么了？\x01",
            "突然沉默下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x106,
        (
            "#1422F#1P呼…………\x02\x03",

            "#1420F看来敌人\x01",
            "开始登场了。\x02",
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
        "#393F#1P啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x105,
        "#1412F#2P莫非……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#374F#2P偷、偷窥色魔来了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x106,
        (
            "#1425F#1P（艾丝蒂尔，\x01",
            "　你能看到北边的草丛吗？）\x02\x03",

            "（以不会被察觉的方式\x01",
            "　偷偷地查看一下情况。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#445F#2P（嗯、嗯……）\x02",
    )

    CloseMessageWindow()
    OP_43(0x17, 0x0, 0x0, 0x2)
    ClearChrFlags(0x17, 0x80)
    Call(1, 16)
    Sleep(1000)

    ChrTalk(    #34
        0x101,
        "#445F#2P（确、确实有什么东西在呢。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x106,
        (
            "#1425F#2P（嗯，那个恐怕就是\x01",
            "　我们要逮的『偷窥犯』了。）\x02",
        )
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
            "#1413F（可是应该怎么做呢？）\x02\x03",

            "（就算想抓，\x01",
            "　从这里也没办法出手啊。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#445F#2P（嗯，需要有人先出来\x01",
            "　从背后绕过去。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x106,
        (
            "#1425F#1P（只能这么办了。）\x02\x03",

            "（好，我和艾丝蒂尔\x01",
            "　绕到那家伙的背后去。）\x02\x03",

            "（公主你们就在\x01",
            "　这里吸引敌人的注意。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x105,
        "#1412F（嗯，明白了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x107,
        "#398F#1P（嗯、嗯！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#445F#2P（那么，赶快……）\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x17, 400)

    ChrTalk(    #42
        0x101,
        "#374F#2P（……咦，奇、奇怪！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x106,
        "#1421F#1P（怎么了！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        (
            "#374F#2P（你、你看！\x01",
            "　那家伙要逃跑了！）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_175C():
        TurnDirection(0x106, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_175C)

    def lambda_176A():
        TurnDirection(0x105, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_176A)
    TurnDirection(0x107, 0x17, 400)
    OP_59()
    Call(1, 10)

    ChrTalk(    #45
        0x106,
        "#1423F#2P艾丝蒂尔！　追！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x3)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #46
        0x101,
        "#372F#2P明、明白！！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/R3101   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_11_B0A end

    def Function_12_17DF(): pass

    label("Function_12_17DF")

    SetChrPos(0x101, 66830, 1000, 19670, 155)
    SetChrPos(0x106, 64610, 1000, 16420, 200)
    SetChrPos(0x107, 66280, 1000, 18830, 110)
    SetChrPos(0x104, 67940, 1000, 19460, 200)
    Call(1, 15)

    ChrTalk(    #47
        0x101,
        (
            "#377F#1P啊～真惬意～\x02\x03",

            "嗯，还是\x01",
            "露天浴令人心情舒畅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x104,
        (
            "#1401F#2P呵呵，我有同感。\x02\x03",

            "我也完全被这种\x01",
            "雅趣给迷住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#442F#1P对了，奥利维尔也\x01",
            "曾经在这里住过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x104,
        (
            "#1400F#2P嗯，诞辰庆典后\x01",
            "我在这里好好地享受了一阵子。\x02\x03",

            "我也约了雪拉，\x01",
            "不过不凑巧，她好像很忙……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_196B():
        TurnDirection(0x107, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_196B)
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #51
        0x101,
        (
            "#374F#1P咦！？\x01",
            "你约了雪拉姐？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x107,
        (
            "#393F#1P啊，那个那个……\x02\x03",

            "雪拉姐和\x01",
            "奥利维尔先生……\x02\x03",

            "莫非是\x01",
            "那种关系吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x104,
        (
            "#1401F#2P呵呵，这就任凭你想象吧。\x02\x03",

            "不过你放心好了。\x01",
            "现在我只对提妲一心一意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x107,
        "#394F#1P啊、啊啊……！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x106, 0, 400)

    ChrTalk(    #55
        0x106,
        "#1425F……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#443F#1P喂喂，奥利维尔。\x02\x03",

            "对面有个可怕的哥哥\x01",
            "在朝这边看哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 200, 400)

    ChrTalk(    #57
        0x104,
        (
            "#1403F#2P哦，对了。\x02\x03",

            "#1401F哈哈，阿加特。\x01",
            "你不参加谈话吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B12():
        OP_6D(65670, 1000, 18470, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B12)
    TurnDirection(0x106, 0x101, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #58
        0x106,
        (
            "#1422F#1P算了，先不管这些……\x01",
            "可别忘了我们来这里的目的。\x02\x03",

            "#1420F别放松警惕啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B8A():
        OP_8C(0x101, 200, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B8A)
    Sleep(350)
    OP_8C(0x107, 200, 400)

    ChrTalk(    #59
        0x101,
        (
            "#445F#2P嗯、嗯……\x01",
            "知道了，不过阿加特……\x02\x03",

            "#444F#2P你、你为什么要\x01",
            "披着一块印花大手巾。\x02\x03",

            "老实说你那个样子\x01",
            "特别惹人注目。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x107,
        "#395F#1P这、这个么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x106,
        (
            "#1422F#1P什么注目啊闭目的\x01",
            "我可不管。\x02\x03",

            "没这东西的话\x01",
            "我就提不起精神。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x104,
        (
            "#1404F#2P呼，个人的习惯倒是\x01",
            "不便干涉……\x02\x03",

            "…………………………………\x01",
            "…………………………………\x02\x03",

            "#1403F不过想不到他会披着\x01",
            "印花大手巾洗头呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x106,
        (
            "#1426F#1P#3S啊──！\x01",
            "你用常识考虑一下啊，常识！#2S\x02\x03",

            "那种时候\x01",
            "当然要拿下来了！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#377F#2P哦……太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x107,
        (
            "#395F#1P嘿嘿……\x01",
            "是、是啊。\x02\x03",

            "还是会拿下来的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x106,
        (
            "#1424F#1P都、都是傻瓜！？\x02\x03",

            "你们以为我是\x01",
            "什么人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#378F#2P嗯～我觉得阿加特\x01",
            "有可能会这么做啊。\x02\x03",

            "你是属于只要下了决定，就无论\x01",
            "多冒失的事情都做得出来的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x106,
        (
            "#1427F#1P我说啊，这根本就是\x01",
            "两码事…………………\x02\x03",

            "……………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#370F#2P？？？\x02\x03",

            "怎么了？\x01",
            "突然沉默下来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x106,
        (
            "#1422F#1P呼…………\x02\x03",

            "#1420F看来敌人\x01",
            "开始登场了。\x02",
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
        "#393F#1P啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#374F#2P偷、偷窥色魔来了！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x106,
        (
            "#1425F#1P（艾丝蒂尔，\x01",
            "　你能看到北边的草丛吗？）\x02\x03",

            "（以不会被察觉的方式\x01",
            "　偷偷地查看一下情况。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#445F（嗯、嗯……）\x02",
    )

    CloseMessageWindow()
    OP_43(0x17, 0x0, 0x0, 0x2)
    ClearChrFlags(0x17, 0x80)
    Call(1, 16)
    Sleep(1000)

    ChrTalk(    #75
        0x101,
        "#445F#2P（确、确实有什么东西在呢。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x106,
        (
            "#1425F#2P（嗯，那个恐怕就是\x01",
            "　我们要逮的『偷窥犯』了。）\x02",
        )
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
            "#1402F#2P（那接下来该怎么办呢？）\x02\x03",

            "（就算想抓，\x01",
            "　介入起来非常困难吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#445F#2P（嗯，需要有人先出来\x01",
            "　从背后绕过去。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x106,
        (
            "#1425F#1P（只能这么办了。）\x02\x03",

            "（好，我和艾丝蒂尔\x01",
            "　绕到那家伙的背后去。）\x02\x03",

            "（奥利维尔你们在这里\x01",
            "　这里吸引敌人的注意。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x107,
        "#398F#1P（嗯、嗯！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x104,
        "#1400F（嗯，明白了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#445F#2P（那么，赶快……）\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x17, 400)

    ChrTalk(    #83
        0x101,
        "#374F#2P（……咦，奇、奇怪！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x106,
        "#1421F#1P（怎么了！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#374F#2P（你、你看！\x01",
            "　那家伙要逃跑了！）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2312():
        TurnDirection(0x106, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2312)

    def lambda_2320():
        TurnDirection(0x104, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2320)
    TurnDirection(0x107, 0x17, 400)
    OP_59()
    Call(1, 10)

    ChrTalk(    #86
        0x106,
        "#1423F#2P艾丝蒂尔！　追！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x3)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #87
        0x101,
        "#372F#2P明、明白！！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/R3101   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_12_17DF end

    def Function_13_2395(): pass

    label("Function_13_2395")

    SetChrPos(0x101, 66830, 1000, 19670, 155)
    SetChrPos(0x103, 65900, 1000, 18260, 108)
    SetChrPos(0x107, 66310, 1000, 19250, 153)
    SetChrPos(0x105, 68340, 1000, 19480, 200)
    Call(1, 15)

    ChrTalk(    #88
        0x101,
        (
            "#377F#1P啊～真惬意～\x02\x03",

            "嗯，还是\x01",
            "露天浴令人心情舒畅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x105,
        "#1416F#2P风真令人感到舒服啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x103,
        (
            "#1391F#1P呵呵，真像仙境一般。\x02\x03",

            "要是能再来上一杯\x01",
            "就没的说了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 200, 400)

    ChrTalk(    #91
        0x101,
        (
            "#370F那倒是无所谓，不过雪拉姐，\x02\x03",

            "你的头发没放下来？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_24C1():
        OP_8C(0x107, 200, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_24C1)
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #92
        0x103,
        (
            "#1390F#1P这样的话只要穿上\x01",
            "衣服就能立即飞奔到外面了。\x02\x03",

            "一旦解开再\x01",
            "绕起来就要花很久了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#442F嗯，确实不知道\x01",
            "罪犯什么时候会来。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 155, 400)

    ChrTalk(    #94
        0x107,
        (
            "#395F不过也因为那个罪犯\x01",
            "我们大家才能在一起洗个澡啊。\x02\x03",

            "嘿嘿，虽然对方不是好人，\x01",
            "不过还是有点心存感激。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 300, 400)

    ChrTalk(    #95
        0x105,
        (
            "#1410F#2P呵呵，我明白你的心情。\x02\x03",

            "总觉得这样一来\x01",
            "就像是来旅行的一样。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #96
        0x101,
        (
            "#371F又是4个人，就好像和睦的\x01",
            "家庭旅行一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x103,
        (
            "#1393F#1P这种情况下的话……\x01",
            "难道说我是提妲的妈妈？\x02\x03",

            "#1395F至少希望你说成是４姐妹啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_26B2():
        OP_8C(0x101, 200, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26B2)
    OP_8C(0x107, 200, 400)

    ChrTalk(    #98
        0x107,
        "#390F啊，那就这样好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x105,
        (
            "#1411F#2P嘻嘻……\x02\x03",

            "#1410F不过，想想看的话\x01",
            "洗澡成员都是女性还是第一次呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2732():
        OP_8C(0x101, 108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2732)
    Sleep(100)

    def lambda_2745():
        OP_8C(0x103, 108, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2745)
    OP_8C(0x107, 108, 400)

    ChrTalk(    #100
        0x101,
        (
            "#370F#1P嗯，这么说起来确实如此呢。\x01",
            "今天奥利维尔也不在……\x02\x03",

            "#443F嗯，如果让那家伙知道的话\x01",
            "一定会哭着喊不甘心的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x107,
        "#395F#1P这、这个么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x105,
        "#1415F#2P完、完全可以想象。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x103,
        (
            "#1396F#1P算了，就对他保密吧。\x01",
            "可不想给他增添不必要的记恨。\x02\x03",

            "奥利维尔好像也\x01",
            "非常中意这个温泉呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 200, 400)

    ChrTalk(    #104
        0x101,
        "#370F…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #105
        0x107,
        "#390F#1P姐姐，你怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        (
            "#443F#2P咦……？\x01",
            "不，没什么……\x02\x03",

            "#442F我只是在想，难得有机会，\x01",
            "是不是要问问看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x107,
        "#393F？？？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 200, 400)

    ChrTalk(    #108
        0x101,
        (
            "#378F#2P那、那个，雪拉姐。\x01",
            "我能问你一件事吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)

    ChrTalk(    #109
        0x103,
        "#1393F#1P哎呀，怎么了？一本正经的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#442F#2P我说，你真～的\x01",
            "和奥利维尔完全没什么？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29D8():
        TurnDirection(0x105, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_29D8)
    Sleep(150)
    TurnDirection(0x107, 0x103, 400)

    ChrTalk(    #111
        0x105,
        "#1414F#2P…………！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        (
            "#1393F#1P什么指的是……\x01",
            "那种关系？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#441F嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x103,
        (
            "#1391F#1P傻瓜，怎么可能有。\x02\x03",

            "只是普通的酒友啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#378F啊～真的吗？\x02\x03",

            "你们偶尔会进行只有你们\x01",
            "两个人才能明白的对话吧？\x02\x03",

            "那种彼此了解的协调感觉\x01",
            "还真是挺让人在意呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x107,
        "#396F（心、心砰砰跳……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#1396F#1P哦，原来如此……\x02\x03",

            "所以你才突然问\x01",
            "这么奇怪的话啊？\x02\x03",

            "很遗憾，那也只是工作的对话哦。\x01",
            "稍微有点原因的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        "#370F#2P原因？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x103,
        (
            "#1390F#1P嗯，不过以后再向你说明。\x02\x03",

            "总之现在不能太\x01",
            "热衷于聊天。\x02\x03",

            "我们是为了搜查来的，\x01",
            "必须对周围再警惕一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#379F啊，被你蒙混过关了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 300, 400)

    ChrTalk(    #121
        0x105,
        (
            "#1412F#2P不过，艾丝蒂尔……\x02\x03",

            "……看来雪拉小姐\x01",
            "说的没错。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_2CA2():
        TurnDirection(0x103, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2CA2)
    Sleep(150)

    def lambda_2CB5():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CB5)
    Sleep(150)
    OP_8C(0x107, 108, 400)

    ChrTalk(    #122
        0x101,
        "#374F#2P咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x107,
        "#393F#1P莫、莫非……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x103,
        "#1392F#1P（偷窥色魔来了！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x105,
        "#1412F#2P（……在北边的草丛里。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        "#445F（明白了，北边的草丛是吧……）\x02",
    )

    CloseMessageWindow()
    OP_43(0x17, 0x0, 0x0, 0x2)
    ClearChrFlags(0x17, 0x80)
    Call(1, 16)
    Sleep(1000)

    ChrTalk(    #127
        0x101,
        "#445F#2P（确、确实有什么东西在呢。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x103,
        (
            "#1392F#2P（莫非，那就是\x01",
            "　『偷窥犯』的原形？）\x02",
        )
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
            "#1413F#2P（可是，我们该怎么办？）\x02\x03",

            "（就算想抓住他，\x01",
            "　从这里也没办法出手啊。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#445F#2P（嗯，需要有人先出来\x01",
            "　从背后绕过去。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x103,
        (
            "#1392F#1P（我和艾丝蒂尔绕到\x01",
            "　那家伙的背后去。）\x02\x03",

            "（公主大人和提妲在这里\x01",
            "　吸引敌人的注意。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x105,
        "#1412F#2P（嗯，明白了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x107,
        "#398F（嗯、嗯！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        "#445F#2P（那么，赶快……）\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x17, 400)

    ChrTalk(    #135
        0x101,
        "#374F#2P（……咦，奇、奇怪！？）\x02",
    )

    CloseMessageWindow()

    def lambda_2FEC():
        OP_8C(0x103, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2FEC)
    Sleep(150)

    def lambda_2FFF():
        OP_8C(0x105, 300, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2FFF)
    Sleep(150)
    OP_8C(0x107, 0, 400)

    ChrTalk(    #136
        0x103,
        "#1393F#1P（怎么了！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        (
            "#374F#2P（你、你看！\x01",
            "　那家伙要逃跑了！）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3065():
        OP_8C(0x105, 350, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3065)

    def lambda_3073():
        TurnDirection(0x103, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3073)
    TurnDirection(0x107, 0x17, 400)
    WaitChrThread(0x105, 0x1)
    OP_59()
    Call(1, 10)

    ChrTalk(    #138
        0x103,
        "#1394F#2P艾丝蒂尔！追！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x3)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #139
        0x101,
        "#372F#2P明、明白！！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/R3101   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2395 end

    def Function_14_30EB(): pass

    label("Function_14_30EB")

    SetChrPos(0x101, 66830, 1000, 19670, 155)
    SetChrPos(0x103, 65900, 1000, 18260, 108)
    SetChrPos(0x107, 66310, 1000, 19250, 153)
    SetChrPos(0x104, 68340, 1000, 19480, 200)
    Call(1, 15)

    ChrTalk(    #140
        0x101,
        (
            "#377F#1P啊～真惬意～\x02\x03",

            "嗯，还是\x01",
            "露天浴令人心情舒畅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x103,
        (
            "#1391F#1P呵呵，真像仙境一般。\x02\x03",

            "要是能再来上一杯\x01",
            "就没的说了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 200, 400)

    ChrTalk(    #142
        0x101,
        (
            "#370F那倒是无所谓，不过雪拉姐，\x02\x03",

            "你的头发没放下来？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_31F4():
        OP_8C(0x107, 200, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_31F4)
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #143
        0x103,
        (
            "#1390F#1P这样的话只要穿上\x01",
            "衣服就能立即飞奔到外面了。\x02\x03",

            "一旦解开再\x01",
            "绕起来就要花很久了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#442F嗯，确实不知道\x01",
            "罪犯什么时候会来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x104,
        (
            "#1404F#2P呼，不过有点遗憾呢。\x02\x03",

            "洗后披散着的头发的雪拉也\x01",
            "也一定很有魅力啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 108, 400)

    ChrTalk(    #146
        0x103,
        "#1396F#1P呵呵，那就留待下次吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x104,
        (
            "#1401F#2P呵呵，原来如此。\x02\x03",

            "那么，下次我就\x01",
            "邀请你去帝国领土内的\x01",
            "高级温泉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#370F…………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #149
        0x107,
        "#390F姐姐，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        (
            "#443F#2P咦……？\x01",
            "不，没什么……\x02\x03",

            "#442F只是感觉……\x01",
            "有点可疑……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x107,
        "#393F啊？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #152
        0x103,
        (
            "#1393F#1P可疑……\x02\x03",

            "莫非，\x01",
            "是说我和奥利维尔？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#441F嗯、嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x107, 200, 400)

    ChrTalk(    #154
        0x103,
        (
            "#1391F#1P傻瓜，没什么的啦。\x02\x03",

            "只是普通的酒友啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #155
        0x104,
        (
            "#1401F#2P这、这个称号\x01",
            "我可不敢当。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#378F啊～真的吗？\x02\x03",

            "你们偶尔会进行只有你们\x01",
            "两个人才能明白的对话吧？\x02\x03",

            "那只互相了解的感觉\x01",
            "挺让人在意的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x107,
        "#396F（心、心砰砰跳……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x103,
        (
            "#1396F#1P哦，原来如此……\x02\x03",

            "所以你才突然问\x01",
            "这么奇怪的话吗？\x02\x03",

            "很遗憾，那也只是工作方面的对话哦。\x01",
            "稍微有点原因的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#370F#2P原因？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x103,
        (
            "#1390F#1P嗯，不过以后再向你说明。\x02\x03",

            "总之现在不能太\x01",
            "热衷于聊天。\x02\x03",

            "我们是为了搜查来的，\x01",
            "必须对周围再警惕一些。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#379F啊，被你蒙混过关了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x104,
        (
            "#1401F#2P呼，不过……\x01",
            "偶然还真是可怕的东西。\x02\x03",

            "看来真的必须要\x01",
            "警惕呢。\x02",
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

    def lambda_3714():
        TurnDirection(0x103, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3714)
    Sleep(150)

    def lambda_3727():
        OP_8C(0x101, 108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3727)
    Sleep(150)
    OP_8C(0x107, 108, 400)

    ChrTalk(    #163
        0x101,
        "#374F#2P咦！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x107,
        "#393F#1P莫、莫非……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x103,
        "#1392F#1P（偷窥色魔来了！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x104,
        (
            "#1402F#2P（能看到北边的草丛吗？）\x02\x03",

            "（以不会被察觉的方式\x01",
            "　偷偷地查看一下情况。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        "#445F#2P（嗯、嗯……）\x02",
    )

    CloseMessageWindow()
    OP_43(0x17, 0x0, 0x0, 0x2)
    ClearChrFlags(0x17, 0x80)
    Call(1, 16)
    Sleep(1000)

    ChrTalk(    #168
        0x101,
        "#445F#2P（确、确实有什么东西在呢。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x103,
        (
            "#1392F#2P（莫非，那就是\x01",
            "　『偷窥犯』的原形？）\x02",
        )
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
            "#1402F#2P（那接下来该怎么办呢？）\x02\x03",

            "（就算想抓，\x01",
            "　介入起来非常困难吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        (
            "#445F#2P（嗯，需要有人先出来\x01",
            "　从背后绕过去。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x103,
        (
            "#1392F#1P（我和艾丝蒂尔绕到\x01",
            "　那家伙的背后去。）\x02\x03",

            "（奥利维尔和提妲在这里\x01",
            "　吸引敌人的注意。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x107,
        "#398F#1P（嗯、嗯！）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x104,
        "#1400F#2P（嗯，明白了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#445F#2P（那么，赶快……）\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x17, 400)

    ChrTalk(    #176
        0x101,
        "#374F#2P（……咦，奇、奇怪！？）\x02",
    )

    CloseMessageWindow()

    def lambda_3A7D():
        OP_8C(0x103, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A7D)
    Sleep(150)

    def lambda_3A90():
        OP_8C(0x104, 300, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A90)
    Sleep(150)
    OP_8C(0x107, 0, 400)

    ChrTalk(    #177
        0x103,
        "#1393F#1P（怎么了！？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#374F#2P（你、你看！\x01",
            "　那家伙要逃跑了！）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3AF6():
        OP_8C(0x104, 350, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3AF6)

    def lambda_3B04():
        TurnDirection(0x103, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3B04)
    TurnDirection(0x107, 0x17, 400)
    WaitChrThread(0x104, 0x1)
    OP_59()
    Call(1, 10)

    ChrTalk(    #179
        0x103,
        "#1394F#2P艾丝蒂尔！　追！\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0x3)
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #180
        0x101,
        "#372F#2P明、明白！！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    SetMapFlags(0x2000000)
    NewScene("ED6_DT21/R3101   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_14_30EB end

    def Function_15_3B7E(): pass

    label("Function_15_3B7E")

    OP_6D(65820, 2000, 7860, 0)
    OP_67(0, 9000, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(80000, 0)
    OP_6E(246, 0)

    def lambda_3BC1():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3BC1)
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

    # Function_15_3B7E end

    def Function_16_3C21(): pass

    label("Function_16_3C21")


    def lambda_3C27():
        OP_6D(67620, 4000, 23820, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3C27)

    def lambda_3C3F():
        OP_67(0, 3370, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3C3F)

    def lambda_3C57():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_3C57)

    def lambda_3C67():
        OP_6C(350000, 3000)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_3C67)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    Return()

    # Function_16_3C21 end

    SaveToFile()

Try(main)
