from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'P9000   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P9000.x',
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
        'Mystery Receptionist',                 # 9
        'Guardian Beast',                       # 10
        'Event Camera',                         # 11
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
        'ED6_DT07/CH01570 ._CH',             # 00
        'ED6_DT29/CH15210 ._CH',             # 01
        'ED6_DT07/CH00160 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01570P._CP',             # 00
        'ED6_DT29/CH15210P._CP',             # 01
        'ED6_DT07/CH00160P._CP',             # 02
    )

    DeclNpc(
        X                   = 8080,
        Z                   = 0,
        Y                   = -4170,
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
        "Function_0_122",          # 00, 0
        "Function_1_205",          # 01, 1
        "Function_2_206",          # 02, 2
        "Function_3_237",          # 03, 3
        "Function_4_268",          # 04, 4
        "Function_5_299",          # 05, 5
        "Function_6_2CA",          # 06, 6
        "Function_7_2FB",          # 07, 7
        "Function_8_3A9",          # 08, 8
        "Function_9_4A7",          # 09, 9
        "Function_10_501",         # 0A, 10
        "Function_11_546",         # 0B, 11
        "Function_12_5CA",         # 0C, 12
        "Function_13_67F",         # 0D, 13
        "Function_14_733",         # 0E, 14
        "Function_15_9DD",         # 0F, 15
        "Function_16_A76",         # 10, 16
        "Function_17_B0C",         # 11, 17
        "Function_18_BC4",         # 12, 18
        "Function_19_CB7",         # 13, 19
        "Function_20_DBA",         # 14, 20
        "Function_21_EB0",         # 15, 21
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_146")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_13F")
    Event(0, 16)
    Jump("loc_143")

    label("loc_13F")

    Event(0, 14)

    label("loc_143")

    Jump("loc_204")

    label("loc_146")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_165")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_165")

    Event(0, 17)
    Jump("loc_204")

    label("loc_16C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_192")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_18B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18B")

    Event(0, 18)
    Jump("loc_204")

    label("loc_192")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1B1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B1")

    Event(0, 19)
    Jump("loc_204")

    label("loc_1B8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1D7")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D7")

    Event(0, 20)
    Jump("loc_204")

    label("loc_1DE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_204")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1FD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FD")

    Event(0, 21)
    Jump("loc_204")

    label("loc_204")

    Return()

    # Function_0_122 end

    def Function_1_205(): pass

    label("Function_1_205")

    Return()

    # Function_1_205 end

    def Function_2_206(): pass

    label("Function_2_206")

    Sleep(4000)

    def lambda_211():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_211)
    OP_8E(0xFE, 0x258, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_2_206 end

    def Function_3_237(): pass

    label("Function_3_237")

    Sleep(4000)

    def lambda_242():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_242)
    OP_8E(0xFE, 0xFFFFFF38, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_3_237 end

    def Function_4_268(): pass

    label("Function_4_268")

    Sleep(4000)

    def lambda_273():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_273)
    OP_8E(0xFE, 0xFFFFFC18, 0x0, 0xFFFFE69C, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_4_268 end

    def Function_5_299(): pass

    label("Function_5_299")

    Sleep(4000)

    def lambda_2A4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2A4)
    OP_8E(0xFE, 0x258, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_5_299 end

    def Function_6_2CA(): pass

    label("Function_6_2CA")

    Sleep(4000)

    def lambda_2D5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D5)
    OP_8E(0xFE, 0xFFFFFC18, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_6_2CA end

    def Function_7_2FB(): pass

    label("Function_7_2FB")

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

    # Function_7_2FB end

    def Function_8_3A9(): pass

    label("Function_8_3A9")

    Fade(1000)
    OP_44(0x12, 0x0)
    OP_6D(2140, 5910, 10240, 0)
    OP_67(0, 3590, -10000, 0)
    OP_6B(3900, 0)
    OP_6C(45000, 0)
    OP_6E(478, 0)

    def lambda_3F5():
        OP_6D(5340, 3360, 4440, 6000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_3F5)

    def lambda_40D():
        OP_67(0, 1910, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_40D)

    def lambda_425():
        OP_6B(4100, 6000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_425)

    def lambda_435():
        OP_6E(571, 6000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_435)
    OP_C8(0x200, 0x46, "C_PLAC42._CH", 0x0, 0x3E8)
    WaitChrThread(0x12, 0x0)
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

    # Function_8_3A9 end

    def Function_9_4A7(): pass

    label("Function_9_4A7")


    def lambda_4AD():
        OP_D0(-270000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4AD)

    def lambda_4BD():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4BD)
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

    # Function_9_4A7 end

    def Function_10_501(): pass

    label("Function_10_501")

    SetChrPos(0x0, 1260, 0, -5630, 0)
    SetChrPos(0x1, -2060, 0, -6120, 0)
    SetChrPos(0x2, 450, 0, -9110, 0)
    SetChrPos(0x3, -1470, 0, -9140, 0)
    Return()

    # Function_10_501 end

    def Function_11_546(): pass

    label("Function_11_546")

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

    # Function_11_546 end

    def Function_12_5CA(): pass

    label("Function_12_5CA")

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

    # Function_12_5CA end

    def Function_13_67F(): pass

    label("Function_13_67F")

    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 90, -1, -1)

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

    # Function_13_67F end

    def Function_14_733(): pass

    label("Function_14_733")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x19, 0, 0x0)
    ClearParty()
    AddParty(0x6, 0xEE, 0xFF)
    OP_31(0x6, 0xFE, 0x0)
    Call(0, 7)
    SetChrPos(0x107, 0, 0, -16000, 0)

    def lambda_76C():
        OP_6B(3100, 4000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_76C)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x107, 0x0, 0x0, 0x3)
    Call(0, 8)
    WaitChrThread(0x107, 0x0)
    Sleep(500)

    ChrTalk(    #3
        0x107,
        (
            "#560F#5PWow... This room's so pretty...\x02\x03",

            "I wonder how it's made up, though?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    LoadEffect(0x0, "map\\mp250_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x222, 0x0, 0x64)
    OP_0D()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 0, 0, 0, 180)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xCF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_89B():

        label("loc_89B")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_89B")

    QueueWorkItem2(0x11, 3, lambda_89B)

    def lambda_8AE():
        OP_6D(1120, 110, -2080, 1500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_8AE)

    def lambda_8C6():
        OP_67(0, 4750, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8C6)

    def lambda_8DE():
        OP_6B(2350, 1500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_8DE)

    def lambda_8EE():
        OP_6E(406, 1500)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_8EE)
    WaitChrThread(0x12, 0x0)
    LoadEffect(0x1, "map\\mp250_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 0, 200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)

    def lambda_955():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_955)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_82(0x1, 0x2)
    WaitChrThread(0x11, 0x0)
    Sleep(500)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    Fade(250)
    ClearMapFlags(0x10)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x107, 2)
    SetChrSubChip(0x107, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #4
        0x107,
        "#065F#6PUh-oh...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Call(0, 13)
    Battle(0x384, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 15)
    Return()

    # Function_14_733 end

    def Function_15_9DD(): pass

    label("Function_15_9DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapFlags(0x10)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    SetChrFlags(0x11, 0x80)
    OP_44(0x11, 0x3)
    OP_6D(1190, 110, -4250, 0)
    OP_67(0, 5850, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(310, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(500)
    Call(0, 12)
    Call(0, 9)
    OP_D6(0x0)
    OP_E3(0x0, 0x19, 64, 0x2)
    ClearParty()
    AddParty(0x6, 0xEE, 0xFF)
    OP_28(0x1, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_9DD end

    def Function_16_A76(): pass

    label("Function_16_A76")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x19, 0, 0x0)
    ClearParty()
    AddParty(0x6, 0xEE, 0xFF)
    Call(0, 7)
    SetChrPos(0x107, 0, 0, -16000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEB")

    def lambda_AB5():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_AB5)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x107, 0x0, 0x0, 0x3)
    Call(0, 8)
    WaitChrThread(0x107, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_AEB")

    OP_D6(0x0)
    OP_E3(0x0, 0x19, 64, 0x2)
    ClearParty()
    AddParty(0x6, 0xEE, 0xFF)
    OP_28(0x1, 0x4, 0x8)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_A76 end

    def Function_17_B0C(): pass

    label("Function_17_B0C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x1A, 0, 0x0)
    ClearParty()
    AddParty(0x5, 0xEE, 0xFF)
    AddParty(0x6, 0xEF, 0xFF)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B80")

    def lambda_B3E():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_B3E)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x106, 0x0, 0x0, 0x2)
    OP_43(0x107, 0x0, 0x0, 0x4)
    Call(0, 8)
    WaitChrThread(0x106, 0x0)
    WaitChrThread(0x107, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_B80")

    OP_D6(0x0)
    OP_E3(0x0, 0x1A, 32, 0x2)
    ClearParty()
    AddParty(0x5, 0xEE, 0xFF)
    OP_E6(0x0, 0x0)
    OP_E6(0x2)
    OP_28(0x2, 0x4, 0x8)
    OP_A3(0x2F85)
    OP_A3(0x2F86)
    OP_A3(0x2F87)
    OP_A3(0x2F88)
    OP_A3(0x2F89)
    OP_A3(0x2F8A)
    OP_A3(0x2F8B)
    OP_A3(0x2F8C)
    OP_A3(0x2F8D)
    OP_C2(0x1, 0x1F)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_B0C end

    def Function_18_BC4(): pass

    label("Function_18_BC4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x7, 0, 0x0)
    ClearParty()
    AddParty(0x2, 0xEE, 0xFF)
    Call(0, 7)
    SetChrPos(0x103, 0, 0, -16000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x4, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C39")

    def lambda_C03():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_C03)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x103, 0x0, 0x0, 0x3)
    Call(0, 8)
    WaitChrThread(0x103, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_C39")

    OP_D6(0x0)
    OP_3E(0x32B, 1)
    OP_E3(0x0, 0x7, 4, 0x2)
    ClearParty()
    AddParty(0x2, 0xEE, 0xFF)
    OP_BB(0x2, 0x1, 0x18)
    OP_BD()
    OP_E6(0x0, 0x0)
    OP_E6(0x2)
    OP_C2(0x1, 0x4)
    OP_28(0x4, 0x4, 0x8)
    OP_A3(0x2F4A)
    OP_A3(0x2F4B)
    OP_A3(0x2F4C)
    OP_A3(0x2F4D)
    OP_A3(0x2F4E)
    OP_A3(0x2F4F)
    OP_A3(0x2F50)
    OP_A3(0x2F51)
    OP_A3(0x2F52)
    OP_A3(0x2F53)
    OP_A3(0x2F54)
    OP_A3(0x2F55)
    OP_A3(0x2F56)
    OP_A3(0x2F57)
    OP_A3(0x2F58)
    OP_A3(0x2F59)
    OP_A3(0x2F5A)
    OP_A3(0x2FF0)
    OP_A3(0x2FF1)
    OP_A3(0x2FF2)
    OP_A3(0x2FF3)
    OP_A3(0x2FF4)
    OP_A3(0x2FF5)
    OP_A3(0x2FF6)
    OP_A3(0x2FF7)
    NewScene("ED6_DT21/T0135   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_BC4 end

    def Function_19_CB7(): pass

    label("Function_19_CB7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x8, 0, 0x0)
    ClearParty()
    AddParty(0x4, 0xEF, 0xFF)
    Call(0, 7)
    SetChrPos(0x105, 0, 0, -16000, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2C")

    def lambda_CF6():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_CF6)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x105, 0x0, 0x0, 0x3)
    Call(0, 8)
    WaitChrThread(0x105, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_D2C")

    OP_D6(0x0)
    OP_E3(0x0, 0x8, 16, 0x2)
    ClearParty()
    AddParty(0x4, 0xEE, 0xFF)
    OP_BB(0x4, 0x1, 0x4)
    OP_BD()
    OP_31(0x4, 0x10, 0xA)
    OP_C2(0x1, 0x1F)
    OP_28(0x5, 0x4, 0x8)
    OP_A3(0x2F65)
    OP_A3(0x2F66)
    OP_A3(0x2F67)
    OP_A3(0x2F68)
    OP_A3(0x2F69)
    OP_A3(0x2F6A)
    OP_A3(0x2F6B)
    OP_A3(0x2F6C)
    OP_A3(0x2F6D)
    OP_A3(0x2F6E)
    OP_A3(0x2F6F)
    OP_A3(0x2F70)
    OP_A3(0x2F71)
    OP_A3(0x2F72)
    OP_A3(0x2F73)
    OP_A3(0x2F74)
    OP_A3(0x2F75)
    OP_A3(0x2F76)
    OP_A3(0x2F77)
    OP_A3(0x2F78)
    OP_A3(0x2F79)
    OP_A3(0x2F7A)
    OP_A3(0x2F7B)
    OP_A3(0x2F7C)
    OP_A3(0x2F7D)
    OP_A3(0x2F7E)
    OP_A3(0x2F7F)
    OP_A3(0x2F80)
    OP_A3(0x2F81)
    OP_A3(0x2F82)
    OP_A3(0x2F83)
    OP_A3(0x2FA7)
    NewScene("ED6_DT21/T2500   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_CB7 end

    def Function_20_DBA(): pass

    label("Function_20_DBA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x9, 0, 0x0)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3D")

    def lambda_DE3():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_DE3)
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

    label("loc_E3D")

    OP_D6(0x0)
    ClearParty()
    AddParty(0x4D, 0xEE, 0xFF)
    OP_C2(0x1, 0x1F)
    OP_28(0x6, 0x4, 0x8)
    OP_A3(0x2F17)
    OP_A3(0x2F18)
    OP_A3(0x2F19)
    OP_A3(0x2F1A)
    OP_A3(0x2F1B)
    OP_A3(0x2F1C)
    OP_A3(0x2F1D)
    OP_A3(0x2F1E)
    OP_A3(0x2F1F)
    OP_A3(0x2F20)
    OP_A3(0x2F21)
    OP_A3(0x2F22)
    OP_A3(0x2F23)
    OP_A3(0x2F24)
    OP_A3(0x2F25)
    OP_A3(0x2F26)
    OP_A3(0x2F28)
    OP_A3(0x2F29)
    OP_A3(0x2F3A)
    OP_A3(0x2F3B)
    OP_A3(0x2F3C)
    OP_A3(0x2F3D)
    OP_A3(0x2F3E)
    OP_A3(0x2F3F)
    OP_A3(0x2F40)
    OP_A3(0x2F41)
    OP_A3(0x2F42)
    OP_A3(0x2F43)
    OP_A3(0x2F44)
    OP_A3(0x2F45)
    NewScene("ED6_DT21/T2402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_DBA end

    def Function_21_EB0(): pass

    label("Function_21_EB0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E3(0x0, 0x11, 0, 0x0)
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    AddParty(0x1, 0xEF, 0xFF)
    Call(0, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x3, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F24")

    def lambda_EE2():
        OP_6B(3100, 3000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_EE2)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_43(0x101, 0x0, 0x0, 0x2)
    OP_43(0x102, 0x0, 0x0, 0x4)
    Call(0, 8)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x102, 0x0)
    Sleep(500)
    Call(0, 11)
    Call(0, 9)

    label("loc_F24")

    OP_D6(0x0)
    OP_E3(0x0, 0x11, 1, 0x2)
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_BB(0x0, 0x1, 0x44)
    OP_BD()
    OP_28(0x3, 0x4, 0x8)
    OP_A3(0x2F60)
    OP_A3(0x2F61)
    OP_A3(0x2F62)
    NewScene("ED6_DT21/T0311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_EB0 end

    SaveToFile()

Try(main)
