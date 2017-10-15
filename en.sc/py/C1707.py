from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1707   ._SN',
        MapName             = 'Bose',
        Location            = 'C1707.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        'Renne',                                # 9
        'Gospel',                               # 10
        'Pater-Mater',                          # 11
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


    AddCharChip(
        'ED6_DT27/CH04510 ._CH',             # 00
        'ED6_DT06/CH20020 ._CH',             # 01
        'ED6_DT27/CH04000 ._CH',             # 02
        'ED6_DT27/CH04010 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH04510P._CP',             # 00
        'ED6_DT06/CH20020P._CP',             # 01
        'ED6_DT27/CH04000P._CP',             # 02
        'ED6_DT27/CH04010P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458753,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1E6,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_12A",          # 00, 0
        "Function_1_142",          # 01, 1
        "Function_2_160",          # 02, 2
        "Function_3_1141",         # 03, 3
        "Function_4_11C7",         # 04, 4
    )


    def Function_0_12A(): pass

    label("Function_0_12A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_141")
    OP_A3(0x10F0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_141")

    Return()

    # Function_0_12A end

    def Function_1_142(): pass

    label("Function_1_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156")
    OP_B1("C1707_y")
    Jump("loc_15F")

    label("loc_156")

    OP_B1("C1707_n")

    label("loc_15F")

    Return()

    # Function_1_142 end

    def Function_2_160(): pass

    label("Function_2_160")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_177")
    Call(0, 3)
    Call(0, 4)

    label("loc_177")

    OP_82(0x80, 0x0)
    OP_82(0x82, 0x0)
    OP_72(0x9, 0x4)
    OP_72(0x8, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_7B()
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    LoadEffect(0x2, "map\\\\mp064_01.eff")
    LoadEffect(0x3, "map\\\\mp065_01.eff")
    LoadEffect(0x4, "map\\\\mp064_00.eff")
    LoadEffect(0x5, "map\\\\mp065_00.eff")
    OP_72(0x0, 0x4)
    OP_A1(0xA, 0x0)
    SetChrPos(0xA, 10580, 500, 9330, 225)
    OP_71(0x0, 0x20)
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 381)
    OP_70(0x0, 0x1A4)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x1)
    OP_51(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x40)
    SetChrPos(0x101, 1200, 0, 1200, 45)
    SetChrPos(0x102, 870, 0, 2560, 45)
    SetChrPos(0xF8, -50, 0, 110, 45)
    SetChrPos(0xF9, -450, 0, 1740, 45)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 65535)
    SetChrPos(0x8, 1220, 950, 12420, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 0)
    ClearChrFlags(0x8, 0x1)
    OP_CF(0x8, 0x0, "Frame85__ren")
    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(34920, 250, 12030, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3960, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0x1C3, 0x0, 0x64)

    def lambda_386():
        OP_6D(6260, 250, 8340, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_386)

    def lambda_39E():
        OP_67(0, 5950, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_39E)

    def lambda_3B6():
        OP_6B(4940, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B6)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0x101, 0x0)
    Fade(500)
    OP_71(0x8, 0x4)
    OP_6D(7230, 250, 9770, 0)
    OP_67(0, 3510, -10000, 0)
    OP_6B(5260, 0)
    OP_6C(32000, 0)
    OP_6E(243, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x101,
        "#1026F#5PIt's reverted...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        "#1042F#5PThe barrier's been dispelled.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#1302F#6PUgh. Why now?\x02\x03",

            "Just a few more minutes and I could have\x01",
            "burned you and made you cry and scream\x01",
            "as I ripped out your guts with my bare hands.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x113, 0x1, 0x46)
    OP_22(0x114, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0xA, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    PlayEffect(0x4, 0x1, 0xA, 4950, 2800, 0, 0, 0, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xA, -4950, 2800, 0, 0, 0, 340, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_619")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_657")

    label("loc_619")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_640")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_657")

    label("loc_640")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_657")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67E")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6BC")

    label("loc_67E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A5")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6BC")

    label("loc_6A5")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6BC")

    Sleep(1000)

    def lambda_6C7():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6C7)

    def lambda_6D5():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6D5)
    Sleep(100)

    def lambda_6E8():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_6E8)
    OP_8C(0xF9, 45, 400)

    ChrTalk(    #3
        0x101,
        "#1005F#5PH-Hey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#1306F#6PBuuuut, that's how life goes sometimes!\x01",
            "I have to go back to the Glorious now.\x02\x03",

            "The professor told me to come back\x01",
            "once the beta served its purpose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1020F#5PYou mean Weissmann?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#1044F#5POnce the beta's served its...?\x02\x03",

            "#1046FSo the towers returning to normal\x01",
            "is part of your plan?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "#263F#6PMaybe? I didn't ask for the details.\x02\x03",

            "#1305FBut he did say the barriers around the\x01",
            "towers were the Aureole's 'hands.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#1026F#5PThe Aureole's... Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#261F#6PHeehee. What DOES that mean?\x01",
            "It makes you wonder!\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)

    def lambda_938():
        OP_6D(11800, 4800, 10810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_938)

    def lambda_950():
        OP_67(0, 3560, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_950)

    def lambda_968():
        OP_6B(3450, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_968)

    def lambda_978():
        OP_6C(41000, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_978)

    def lambda_988():
        OP_6E(325, 3000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_988)
    PlayEffect(0x2, 0x1, 0xA, 5000, 2500, 0, 0, 0, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xA, -4900, 2500, 0, 0, 0, 340, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_A02():
        OP_8F(0xFE, 0x2954, 0x9C4, 0x2472, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A02)
    Sleep(300)

    def lambda_A22():
        OP_8F(0xFE, 0x2954, 0x9C4, 0x2472, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A22)
    Sleep(300)

    def lambda_A42():
        OP_8F(0xFE, 0x2954, 0x9C4, 0x2472, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A42)
    OP_24(0x113, 0x50)
    Sleep(100)
    OP_72(0x0, 0x20)
    OP_D8(0x0, 0x1F4)
    OP_6F(0x0, 241)
    OP_70(0x0, 0x104)
    OP_82(0x0, 0x2)
    Sleep(50)
    PlayEffect(0x2, 0x1, 0xA, 4600, 2600, 0, 0, 0, 18, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0xA, -4600, 2600, 0, 0, 0, 342, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)

    def lambda_AF4():
        OP_8F(0xFE, 0x2954, 0x9C4, 0x2472, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_AF4)
    OP_24(0x113, 0x5A)
    Sleep(100)
    OP_24(0x113, 0x64)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x1)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #10
        0x8,
        (
            "#263F#6PWell, bye-bye! See you later!\x02\x03",

            "#1304FOh, and next time we meet?\x01",
            "I'LL BUTCHER YOU ALL.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B98():
        OP_8C(0xFE, 80, 10)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B98)
    Sleep(200)

    def lambda_BAB():
        OP_8C(0xFE, 80, 15)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_BAB)
    Sleep(200)

    def lambda_BBE():
        OP_8C(0xFE, 80, 20)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_BBE)
    Sleep(500)

    def lambda_BD1():
        OP_8C(0xFE, 80, 30)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_BD1)
    Sleep(100)

    def lambda_BE4():
        OP_8C(0xFE, 80, 40)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_BE4)
    Sleep(2500)
    Fade(500)
    OP_6D(16090, 5040, 13150, 0)
    OP_67(0, 3440, -10000, 0)
    OP_6B(3690, 0)
    OP_6C(39000, 0)
    OP_6E(325, 0)
    ClearChrFlags(0xA, 0x1)

    def lambda_C3E():
        OP_8C(0xFE, 80, 20)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C3E)
    Sleep(500)

    def lambda_C51():
        OP_8C(0xFE, 80, 15)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C51)
    Sleep(500)

    def lambda_C64():
        OP_8C(0xFE, 80, 10)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C64)
    WaitChrThread(0xA, 0x2)

    def lambda_C77():
        OP_6B(3900, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_C77)
    OP_72(0x0, 0x20)
    OP_D8(0x0, 0x1F4)
    OP_6F(0x0, 261)
    OP_70(0x0, 0x118)
    OP_22(0x116, 0x0, 0x64)
    OP_73(0x0)
    Sleep(500)
    PlayEffect(0x3, 0x0, 0xA, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0xA, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0xA, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x5, 0xA, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x6, 0xA, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x7, 0xA, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x114, 0x0, 0x64)
    Sleep(2000)
    PlayEffect(0x2, 0x0, 0xA, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0xA, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0xA, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0xA, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0xA, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x7, 0xA, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_71(0x0, 0x20)
    OP_6F(0x0, 281)
    OP_70(0x0, 0x12C)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)
    Sleep(500)

    def lambda_F4F():
        OP_6D(16040, 8000, 13170, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F4F)

    def lambda_F67():
        OP_67(0, 690, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F67)

    def lambda_F7F():
        OP_6C(75000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F7F)

    def lambda_F8F():
        OP_6E(548, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F8F)

    def lambda_F9F():
        OP_8F(0xFE, 0x25968, 0x61A8, 0x5064, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F9F)
    Sleep(100)

    def lambda_FBF():
        OP_8F(0xFE, 0x25968, 0x61A8, 0x5064, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FBF)
    Sleep(100)

    def lambda_FDF():
        OP_8F(0xFE, 0x16F2D8, 0x61A8, 0x5064, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FDF)
    Sleep(100)

    def lambda_FFF():
        OP_8F(0xFE, 0x25968, 0x61A8, 0x5064, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_FFF)
    Sleep(100)

    def lambda_101F():
        OP_8F(0xFE, 0x25968, 0x61A8, 0x5064, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_101F)
    Sleep(100)

    def lambda_103F():
        OP_8F(0xFE, 0x25968, 0x7530, 0x5064, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_103F)
    Sleep(100)

    def lambda_105F():
        OP_8F(0xFE, 0x25968, 0x7530, 0x5064, 0x59D8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_105F)
    Sleep(100)

    def lambda_107F():
        OP_8F(0xFE, 0x25968, 0x7530, 0x5064, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_107F)
    Sleep(100)

    def lambda_109F():
        OP_8F(0xFE, 0x25968, 0x9C40, 0x5064, 0x80E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_109F)
    Sleep(100)

    def lambda_10BF():
        OP_8F(0xFE, 0x25968, 0x9C40, 0x5064, 0x9470, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10BF)
    Sleep(100)

    def lambda_10DF():
        OP_8F(0xFE, 0x25968, 0xC350, 0x5064, 0xA7F8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10DF)
    Sleep(100)

    def lambda_10FF():
        OP_8F(0xFE, 0x25968, 0xC350, 0x5064, 0xBB80, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_10FF)
    WaitChrThread(0xA, 0x1)
    WaitChrThread(0x101, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x1E24)
    SetMapFlags(0x100000)
    OP_A2(0x10FF)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_160 end

    def Function_3_1141(): pass

    label("Function_3_1141")

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
        (0, "loc_11BA"),
        (1, "loc_11C0"),
        (SWITCH_DEFAULT, "loc_11C6"),
    )


    label("loc_11BA")

    OP_A2(0x1200)
    Jump("loc_11C6")

    label("loc_11C0")

    OP_A2(0x1201)
    Jump("loc_11C6")

    label("loc_11C6")

    Return()

    # Function_3_1141 end

    def Function_4_11C7(): pass

    label("Function_4_11C7")

    FadeToDark(0, 0, -1)
    OP_6D(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_4_11C7 end

    SaveToFile()

Try(main)
