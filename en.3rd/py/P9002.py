from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'P9002   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P9002.x',
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
        'Guardian Beast',                       # 9
        'Event Camera',                         # 10
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
        'ED6_DT27/CHDUMMY ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT27/CHDUMMYP._CP',             # 00
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_F2",           # 00, 0
        "Function_1_1D7",          # 01, 1
        "Function_2_1D8",          # 02, 2
        "Function_3_209",          # 03, 3
        "Function_4_23A",          # 04, 4
        "Function_5_26B",          # 05, 5
        "Function_6_29C",          # 06, 6
        "Function_7_2CD",          # 07, 7
        "Function_8_37B",          # 08, 8
        "Function_9_479",          # 09, 9
        "Function_10_4D3",         # 0A, 10
        "Function_11_518",         # 0B, 11
        "Function_12_59C",         # 0C, 12
        "Function_13_651",         # 0D, 13
        "Function_14_705",         # 0E, 14
        "Function_15_79B",         # 0F, 15
        "Function_16_979",         # 10, 16
        "Function_17_9FE",         # 11, 17
        "Function_18_A90",         # 12, 18
        "Function_19_B22",         # 13, 19
        "Function_20_BB8",         # 14, 20
        "Function_21_C3B",         # 15, 21
    )


    def Function_0_F2(): pass

    label("Function_0_F2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_111")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_111")

    Event(0, 14)
    Jump("loc_1D6")

    label("loc_118")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_137")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_137")

    Event(0, 17)
    Jump("loc_1D6")

    label("loc_13E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_164")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_15D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15D")

    Event(0, 18)
    Jump("loc_1D6")

    label("loc_164")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_183")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_183")

    Event(0, 19)
    Jump("loc_1D6")

    label("loc_18A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x18, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1A9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A9")

    Event(0, 20)
    Jump("loc_1D6")

    label("loc_1B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1CF")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CF")

    Event(0, 21)
    Jump("loc_1D6")

    label("loc_1D6")

    Return()

    # Function_0_F2 end

    def Function_1_1D7(): pass

    label("Function_1_1D7")

    Return()

    # Function_1_1D7 end

    def Function_2_1D8(): pass

    label("Function_2_1D8")

    Sleep(4000)

    def lambda_1E3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1E3)
    OP_8E(0xFE, 0x258, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_2_1D8 end

    def Function_3_209(): pass

    label("Function_3_209")

    Sleep(4000)

    def lambda_214():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_214)
    OP_8E(0xFE, 0xFFFFFF38, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_3_209 end

    def Function_4_23A(): pass

    label("Function_4_23A")

    Sleep(4000)

    def lambda_245():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_245)
    OP_8E(0xFE, 0xFFFFFC18, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_4_23A end

    def Function_5_26B(): pass

    label("Function_5_26B")

    Sleep(4000)

    def lambda_276():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_276)
    OP_8E(0xFE, 0x258, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_5_26B end

    def Function_6_29C(): pass

    label("Function_6_29C")

    Sleep(4000)

    def lambda_2A7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A7)
    OP_8E(0xFE, 0xFFFFFC18, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_29C end

    def Function_7_2CD(): pass

    label("Function_7_2CD")

    SetChrPos(0x0, 600, 0, -16500, 0)
    SetChrPos(0x1, -1000, 0, -16500, 0)
    SetChrPos(0x2, 600, 0, -18500, 0)
    SetChrPos(0x3, -1000, 0, -18500, 0)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(440, 9760, 12190, 0)
    OP_67(0, 2440, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(397, 0)
    Return()

    # Function_7_2CD end

    def Function_8_37B(): pass

    label("Function_8_37B")

    Fade(1000)
    OP_44(0x11, 0x0)
    OP_6D(2140, 5910, 10240, 0)
    OP_67(0, 3590, -10000, 0)
    OP_6B(3900, 0)
    OP_6C(45000, 0)
    OP_6E(478, 0)

    def lambda_3C7():
        OP_6D(5340, 3360, 4440, 6000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_3C7)

    def lambda_3DF():
        OP_67(0, 1910, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3DF)

    def lambda_3F7():
        OP_6B(4100, 6000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3F7)

    def lambda_407():
        OP_6E(571, 6000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_407)
    OP_C8(0x200, 0x46, "C_PLAC43._CH", 0x0, 0x3E8)
    WaitChrThread(0x11, 0x0)
    Sleep(2000)
    Fade(500)
    OP_6D(890, 110, -4660, 0)
    OP_67(0, 5970, -10000, 0)
    OP_6B(2210, 0)
    OP_6C(45000, 0)
    OP_6E(384, 0)
    OP_0D()
    Sleep(300)
    Return()

    # Function_8_37B end

    def Function_9_479(): pass

    label("Function_9_479")


    def lambda_47F():
        OP_D0(-270000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_47F)

    def lambda_48F():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_48F)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    OP_44(0x0, 0x2)
    OP_44(0x0, 0x3)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    Return()

    # Function_9_479 end

    def Function_10_4D3(): pass

    label("Function_10_4D3")

    SetChrPos(0x0, 1260, 0, -5630, 0)
    SetChrPos(0x1, -2060, 0, -6120, 0)
    SetChrPos(0x2, 450, 0, -9110, 0)
    SetChrPos(0x3, -1470, 0, -9140, 0)
    Return()

    # Function_10_4D3 end

    def Function_11_518(): pass

    label("Function_11_518")

    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 128, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x05#2S#40WI shall grant to you a memory fragment\x01",
            "and my blessing...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Return()

    # Function_11_518 end

    def Function_12_59C(): pass

    label("Function_12_59C")

    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #1
        (
            "\x07\x05#2S#40WYou have overcome the trial...\x01",
            "#500W \x01",
            "#40WThus I shall grant to you a memory fragment\x01",
            "and my blessing...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Return()

    # Function_12_59C end

    def Function_13_651(): pass

    label("Function_13_651")

    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 100, -1, -1)

    AnonymousTalk(    #2
        (
            "\x07\x05#40WOvercome the trial before you...\x01",
            "#500W \x01",
            "#40WThen I shall grant to you a memory fragment\x01",
            "and my blessing...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Return()

    # Function_13_651 end

    def Function_14_705(): pass

    label("Function_14_705")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x1, 0, 0x0)
    ClearParty()
    AddParty(0xA, 0xEE, 0xFF)
    Call(0, 7)
    SetChrPos(0x10B, 0, 0, -16000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x24, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77A")

    def lambda_744():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_744)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x10B, 0x0, 0x0, 0x3)
    Call(0, 8)
    WaitChrThread(0x10B, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_77A")

    OP_D6(0x0)
    OP_E3(0x0, 0x1, 1024, 0x2)
    ClearParty()
    AddParty(0xA, 0xEE, 0xFF)
    OP_28(0x24, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_705 end

    def Function_15_79B(): pass

    label("Function_15_79B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0xA, 0, 0x0)
    Call(0, 7)

    def lambda_7B9():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_7B9)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(2000)
    Fade(1000)
    LoadEffect(0x0, "map\\mp200_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x222, 0x0, 0x64)
    OP_0D()
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 0, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)

    def lambda_88F():

        label("loc_88F")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_88F")

    QueueWorkItem2(0x10, 3, lambda_88F)
    OP_6D(0, 0, -3000, 1500)
    LoadEffect(0x1, "map\\mp200_02.eff")
    PlayEffect(0x1, 0xFF, 0xFF, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_905():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_905)
    Sleep(500)
    OP_82(0x0, 0x2)
    WaitChrThread(0x10, 0x0)
    Fade(250)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    Sleep(300)
    Call(0, 13)

    def lambda_940():
        OP_6D(0, 0, 0, 200)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_940)

    def lambda_958():
        OP_6B(2280, 200)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_958)
    WaitChrThread(0x0, 0x0)
    Battle(0x385, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 16)
    Return()

    # Function_15_79B end

    def Function_16_979(): pass

    label("Function_16_979")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x80)
    OP_44(0x10, 0x3)
    Call(0, 10)
    OP_6D(100, 0, -7160, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(500)
    Call(0, 12)
    Call(0, 9)
    OP_28(0x19, 0x4, 0x8)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_979 end

    def Function_17_9FE(): pass

    label("Function_17_9FE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0xA, 0, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x19, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A81")

    def lambda_A27():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_A27)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_A81")

    OP_28(0x19, 0x4, 0x8)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_9FE end

    def Function_18_A90(): pass

    label("Function_18_A90")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0xB, 0, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B13")

    def lambda_AB9():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_AB9)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_B13")

    OP_28(0x1F, 0x4, 0x8)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_A90 end

    def Function_19_B22(): pass

    label("Function_19_B22")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0xC, 0, 0x0)
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    Call(0, 7)
    SetChrPos(0x101, 0, 0, -16000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B97")

    def lambda_B61():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_B61)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x101, 0x0, 0x0, 0x3)
    Call(0, 8)
    WaitChrThread(0x101, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_B97")

    OP_D6(0x0)
    OP_E3(0x0, 0xC, 1, 0x2)
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_28(0x1C, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T1500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_B22 end

    def Function_20_BB8(): pass

    label("Function_20_BB8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0xF, 0, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x18, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2C")

    def lambda_BE1():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_BE1)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_C2C")

    OP_28(0x18, 0x4, 0x8)
    NewScene("ED6_DT21/E1000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_BB8 end

    def Function_21_C3B(): pass

    label("Function_21_C3B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x10, 0, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBE")

    def lambda_C64():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_C64)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x0, 0x0, 0x0, 0x2)
    OP_43(0x1, 0x0, 0x0, 0x4)
    OP_43(0x2, 0x0, 0x0, 0x5)
    OP_43(0x3, 0x0, 0x0, 0x6)
    Call(0, 8)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x1, 0x0)
    WaitChrThread(0x2, 0x0)
    WaitChrThread(0x3, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_CBE")

    OP_28(0x21, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1001   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_C3B end

    SaveToFile()

Try(main)
