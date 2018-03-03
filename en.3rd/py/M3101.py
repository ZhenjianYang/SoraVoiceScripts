from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M3101   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
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
        'ED6_DT09/CH10060 ._CH',             # 00
        'ED6_DT09/CH10061 ._CH',             # 01
        'ED6_DT09/CH11210 ._CH',             # 02
        'ED6_DT09/CH11211 ._CH',             # 03
        'ED6_DT09/CH11030 ._CH',             # 04
        'ED6_DT09/CH11031 ._CH',             # 05
        'ED6_DT09/CH11020 ._CH',             # 06
        'ED6_DT09/CH11021 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10060P._CP',             # 00
        'ED6_DT09/CH10061P._CP',             # 01
        'ED6_DT09/CH11210P._CP',             # 02
        'ED6_DT09/CH11211P._CP',             # 03
        'ED6_DT09/CH11030P._CP',             # 04
        'ED6_DT09/CH11031P._CP',             # 05
        'ED6_DT09/CH11020P._CP',             # 06
        'ED6_DT09/CH11021P._CP',             # 07
    )

    DeclMonster(
        X                   = 8500,
        Z                   = 0,
        Y                   = 28030,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 22270,
        Z                   = 0,
        Y                   = 9030,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14650,
        Z                   = 0,
        Y                   = 30060,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x290,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -38720,
        Z                   = 0,
        Y                   = 14660,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x291,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -43020,
        Z                   = 0,
        Y                   = 37800,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -17170,
        Z                   = 0,
        Y                   = 52830,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -50190,
        Z                   = 0,
        Y                   = 53970,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x290,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -52720,
        TriggerZ            = 500,
        TriggerY            = 17080,
        TriggerRange        = 1000,
        ActorX              = -52720,
        ActorZ              = 1000,
        ActorY              = 17080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -950,
        TriggerZ            = 500,
        TriggerY            = 36160,
        TriggerRange        = 1000,
        ActorX              = -950,
        ActorZ              = 1000,
        ActorY              = 36160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -35580,
        TriggerZ            = 120,
        TriggerY            = 37890,
        TriggerRange        = 1000,
        ActorX              = -35580,
        ActorZ              = 1120,
        ActorY              = 37890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_21A",          # 00, 0
        "Function_1_22E",          # 01, 1
        "Function_2_297",          # 02, 2
        "Function_3_3DB",          # 03, 3
        "Function_4_D0B",          # 04, 4
        "Function_5_E69",          # 05, 5
        "Function_6_12E0",         # 06, 6
    )


    def Function_0_21A(): pass

    label("Function_0_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_22D")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_22D")

    Return()

    # Function_0_21A end

    def Function_1_22E(): pass

    label("Function_1_22E")

    OP_16(0x2, 0xFA0, 0xFFFDFC60, 0xFFFE8130, 0x2300A6)
    OP_1B(0x1, 0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 0)), scpexpr(EXPR_END)), "loc_253")
    OP_6F(0x0, 450)

    label("loc_253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_264")
    OP_72(0x1002, 0x0)
    ExitThread()
    Jump("loc_268")

    label("loc_264")

    OP_64(0x0, 0x1)

    label("loc_268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_279")
    OP_72(0x1001, 0x0)
    ExitThread()
    Jump("loc_27D")

    label("loc_279")

    OP_64(0x1, 0x1)

    label("loc_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F")
    OP_6F(0x2E, 0)
    Jump("loc_296")

    label("loc_28F")

    OP_6F(0x2E, 60)

    label("loc_296")

    Return()

    # Function_1_22E end

    def Function_2_297(): pass

    label("Function_2_297")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_370")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x176, 1)"), scpexpr(EXPR_END)), "loc_305")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x76\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B83)
    Jump("loc_36D")

    label("loc_305")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x76\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x76\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2E, 60)
    OP_70(0x2E, 0x0)

    label("loc_36D")

    Jump("loc_3CD")

    label("loc_370")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05No, you can't return it. You don't even have the receipt!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x19, 0x0)

    label("loc_3CD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_297 end

    def Function_3_3DB(): pass

    label("Function_3_3DB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(238, 0x48, 0x2)
    OP_E0(238, 0x49, 0x3)
    OP_E0(239, 0x4A, 0x2)
    OP_E0(239, 0x4B, 0x3)
    OP_E0(240, 0x4C, 0x2)
    OP_E0(240, 0x4D, 0x3)
    OP_E0(241, 0x4E, 0x2)
    OP_E0(241, 0x4F, 0x3)
    SetChrPos(0x109, 37650, 400, 22330, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_464")
    SetChrPos(0x10C, 36700, 400, 23790, 270)
    SetChrPos(0xF0, 35510, 400, 22410, 270)
    SetChrPos(0xF1, 33730, 400, 23520, 270)
    Jump("loc_4E9")

    label("loc_464")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A8")
    SetChrPos(0x10C, 36700, 400, 23790, 270)
    SetChrPos(0xEF, 35510, 400, 22410, 270)
    SetChrPos(0xF1, 33730, 400, 23520, 270)
    Jump("loc_4E9")

    label("loc_4A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E9")
    SetChrPos(0x10C, 36700, 400, 23790, 270)
    SetChrPos(0xEF, 35510, 400, 22410, 270)
    SetChrPos(0xF0, 33730, 400, 23520, 270)

    label("loc_4E9")

    OP_6D(28800, 0, 24620, 0)
    OP_67(0, 6210, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(306, 0)
    SetChrChipByIndex(0xEE, 8)
    SetChrChipByIndex(0xEF, 10)
    SetChrChipByIndex(0xF0, 12)
    SetChrChipByIndex(0xF1, 14)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A1")

    def lambda_54E():
        OP_8F(0xFE, 0x4FEC, 0x0, 0x5BC2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_54E)

    def lambda_569():
        OP_8F(0xFE, 0x50D2, 0x0, 0x54C4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_569)
    Sleep(100)

    def lambda_589():
        OP_8F(0xFE, 0x571C, 0x0, 0x5CB2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 0, lambda_589)
    Jump("loc_66C")

    label("loc_5A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_608")

    def lambda_5B5():
        OP_8F(0xFE, 0x4FEC, 0x0, 0x5BC2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_5B5)

    def lambda_5D0():
        OP_8F(0xFE, 0x50D2, 0x0, 0x54C4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_5D0)
    Sleep(100)

    def lambda_5F0():
        OP_8F(0xFE, 0x571C, 0x0, 0x5CB2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 0, lambda_5F0)
    Jump("loc_66C")

    label("loc_608")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66C")

    def lambda_61C():
        OP_8F(0xFE, 0x4FEC, 0x0, 0x5BC2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_61C)

    def lambda_637():
        OP_8F(0xFE, 0x50D2, 0x0, 0x54C4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_637)
    Sleep(100)

    def lambda_657():
        OP_8F(0xFE, 0x571C, 0x0, 0x5CB2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10C, 0, lambda_657)

    label("loc_66C")


    def lambda_672():
        OP_8F(0xFE, 0x57D0, 0x0, 0x56C2, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_672)

    def lambda_68D():
        OP_6D(22650, 0, 23940, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_68D)

    def lambda_6A5():
        OP_67(0, 5840, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_6A5)

    def lambda_6BD():
        OP_6B(2750, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_6BD)

    def lambda_6CD():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_6CD)

    def lambda_6DD():
        OP_6E(300, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_6DD)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)

    def lambda_70B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_70B)
    Sleep(100)

    def lambda_71E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_71E)
    Sleep(100)

    def lambda_731():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_731)
    Sleep(100)
    OP_8C(0xEE, 90, 400)
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
    WaitChrThread(0xEE, 0x1)

    ChrTalk(    #3
        0x109,
        (
            "#1841F#5P*pant*...*pant*...\x02\x03",

            "#1069FWhat were we even supposed to do\x01",
            "against THAT?!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_835")

    ChrTalk(    #4
        0x10F,
        "#1445F#6PTruly...all we could do was run.\x02",
    )

    CloseMessageWindow()

    label("loc_835")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_88C")

    ChrTalk(    #5
        0x10E,
        (
            "#175F#6PIndeed... We can't compete on foot with\x01",
            "a military airship.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_88C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C5")

    ChrTalk(    #6
        0x101,
        "#1019F#6PThat thing was just crazy...\x02",
    )

    CloseMessageWindow()

    label("loc_8C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FD")

    ChrTalk(    #7
        0x102,
        "#1502F#6PWe didn't stand a chance...\x02",
    )

    CloseMessageWindow()

    label("loc_8FD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_933")

    ChrTalk(    #8
        0x10B,
        "#413F#6PTh-That was a nightmare...\x02",
    )

    CloseMessageWindow()

    label("loc_933")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_966")

    ChrTalk(    #9
        0x107,
        "#562F#6PTh-That was so scary...\x02",
    )

    CloseMessageWindow()

    label("loc_966")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A2")

    ChrTalk(    #10
        0x10A,
        "#1316F#6PI-I thought we were done for...\x02",
    )

    CloseMessageWindow()

    label("loc_9A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9DF")

    ChrTalk(    #11
        0x105,
        "#1169F#6PThat really took me off guard...\x02",
    )

    CloseMessageWindow()

    label("loc_9DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A12")

    ChrTalk(    #12
        0x103,
        "#1533F#6PThat was ridiculous...\x02",
    )

    CloseMessageWindow()

    label("loc_A12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A4D")

    ChrTalk(    #13
        0x106,
        "#057F#6PDamn it... That was just cheap.\x02",
    )

    CloseMessageWindow()

    label("loc_A4D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC1")

    ChrTalk(    #14
        0x104,
        (
            "#1544F#6PThat was certainly a heart-pounding experience...\x01",
            "that I'd rather not go through again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B1E")

    ChrTalk(    #15
        0x10D,
        (
            "#276F#6PIt's easy to see why Liberlian military airships\x01",
            "are so renowned.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B6A")

    ChrTalk(    #16
        0x108,
        "#075F#6PSheesh... I've got a long way to go, apparently.\x02",
    )

    CloseMessageWindow()

    label("loc_B6A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC9")

    ChrTalk(    #17
        0x110,
        (
            "#1300F#6PBah... Pater-Mater could make short work\x01",
            "of that thing in no time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC9")


    ChrTalk(    #18
        0x10C,
        (
            "#115F#5PI doubt we're meant to do anything against it.\x01",
            "It's more likely to serve as a warning that we\x01",
            "shouldn't go this way for now.\x02\x03",

            "#112FHow about we investigate elsewhere instead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        (
            "#1840F#6PWorks for me. As long as we're alive, there's\x01",
            "always a chance we'll be able to get through\x01",
            "here later.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B19)
    OP_28(0x39, 0x1, 0x10)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_3_3DB end

    def Function_4_D0B(): pass

    label("Function_4_D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_D52")
    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(500, 0, -1)

    def lambda_D30():
        OP_90(0x0, 0x1388, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_D30)
    OP_0D()
    NewScene("ED6_DT21/M3102   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_E68")

    label("loc_D52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 1)), scpexpr(EXPR_END)), "loc_E2B")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D71")
    TurnDirection(0x10C, 0x1, 400)
    Jump("loc_D78")

    label("loc_D71")

    TurnDirection(0x10C, 0x0, 400)

    label("loc_D78")


    ChrTalk(    #20
        0x10C,
        (
            "#115FI'm not sure there's any point in trying to go\x01",
            "through here a second time.\x02\x03",

            "#112FIt'll likely just be a repeat of what happened\x01",
            "last time.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFF830, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_E68")

    label("loc_E2B")

    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(500, 0, -1)

    def lambda_E49():
        OP_90(0x0, 0x1388, 0x0, 0x3E8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_E49)
    OP_0D()
    NewScene("ED6_DT21/M3102   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_E68")

    Return()

    # Function_4_D0B end

    def Function_5_E69(): pass

    label("Function_5_E69")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #21
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12DC")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-51170, 0, 17930, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(314000, 0)
    OP_6E(237, 0)
    SetChrPos(0x109, -50030, 0, 16870, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5F")
    SetChrPos(0x10C, -48670, 0, 15640, 270)
    SetChrPos(0xF0, -48500, 0, 17280, 270)
    SetChrPos(0xF1, -47560, 0, 16210, 270)
    Jump("loc_FE4")

    label("loc_F5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA3")
    SetChrPos(0x10C, -48670, 0, 15640, 270)
    SetChrPos(0xEF, -48500, 0, 17280, 270)
    SetChrPos(0xF1, -47560, 0, 16210, 270)
    Jump("loc_FE4")

    label("loc_FA3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE4")
    SetChrPos(0x10C, -48670, 0, 15640, 270)
    SetChrPos(0xEF, -48500, 0, 17280, 270)
    SetChrPos(0xF0, -47560, 0, 16210, 270)

    label("loc_FE4")

    OP_0D()
    Sleep(500)

    ChrTalk(    #22
        0x109,
        "#1079F#5PWhat's in here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10C,
        (
            "#115F#6PThis is Leiston Fortress' first barracks.\x02\x03",

            "#110FWe should be able to open it using the key we\x01",
            "received from the lieutenant colonel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        "#1060F#5PGood call. Let's give it a shot, then.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x109, 0xFFFF3616, 0x1F4, 0x41BE, 0x7D0, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #25
        "\x07\x05Kevin used the key to unlock the door.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #26
        0x10C,
        (
            "#115F#6PThis is only one of many such barracks in the\x01",
            "fortress, so it's not all that large inside.\x02\x03",

            "#110FWe shouldn't need to spend too long in here.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    ChrTalk(    #27
        0x109,
        "#1060F#5PGot it.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2B1B)
    OP_71(0x1002, 0x0)
    ExitThread()
    OP_64(0x0, 0x1)
    OP_6D(-48260, 0, 16650, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -48260, 0, 16650, 270)
    SetChrPos(0x1, -48260, 0, 16650, 270)
    SetChrPos(0x2, -48260, 0, 16650, 270)
    SetChrPos(0x3, -48260, 0, 16650, 270)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)

    label("loc_12DC")

    TalkEnd(0xFF)
    Return()

    # Function_5_E69 end

    def Function_6_12E0(): pass

    label("Function_6_12E0")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #28
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2361")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-200, 0, 33170, 0)
    OP_67(0, 5820, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(245, 0)
    SetChrPos(0x109, -2220, 0, 31530, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13D6")
    SetChrPos(0x10C, -1250, 0, 33430, 180)
    SetChrPos(0xF0, -780, 0, 31700, 0)
    SetChrPos(0xF1, -1500, 0, 30440, 0)
    Jump("loc_145B")

    label("loc_13D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_141A")
    SetChrPos(0x10C, -1250, 0, 33430, 180)
    SetChrPos(0xEF, -780, 0, 31700, 0)
    SetChrPos(0xF1, -1500, 0, 30440, 0)
    Jump("loc_145B")

    label("loc_141A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145B")
    SetChrPos(0x10C, -1250, 0, 33430, 180)
    SetChrPos(0xEF, -780, 0, 31700, 0)
    SetChrPos(0xF0, -1500, 0, 30440, 0)

    label("loc_145B")

    OP_0D()
    Sleep(500)

    ChrTalk(    #29
        0x10C,
        "#110F#5PThis building is the command center.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        (
            "#1079F#6PWow... Was the army compensating for\x01",
            "something with this thing, or what?\x02\x03",

            "Looks like there's about three floors to it.\x01",
            "That right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C17")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1607")

    ChrTalk(    #31
        0x101,
        (
            "#1015F#12PWe didn't see anything higher than the first\x01",
            "floor when we snuck in here before.\x02\x03",

            "#1006FYou think there's a staircase leading up\x01",
            "nearby?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_1607")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16BF")

    ChrTalk(    #32
        0x102,
        (
            "#1505F#12PWe didn't see anything higher than the first\x01",
            "floor when we snuck in here before.\x02\x03",

            "#1500FMaybe we just missed the staircase to get to\x01",
            "the higher floors.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_16BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1749")

    ChrTalk(    #33
        0x106,
        (
            "#053F#12PI didn't see any staircases when we were in\x01",
            "here last time.\x02\x03",

            "#050FI guess there's one somewhere we missed?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_1749")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17ED")

    ChrTalk(    #34
        0x107,
        (
            "#063F#4PWe never saw any staircases leading up to\x01",
            "the next floor when we were here last time.\x02\x03",

            "#560FBut there has to be one somewhere, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_188D")

    label("loc_17ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_188D")

    ChrTalk(    #35
        0x10B,
        (
            "#215F#4PWe never saw any higher than the first floor\x01",
            "when we were locked away last time.\x02\x03",

            "#210FWhere do you think the staircase to go up is?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_188D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_195E")

    ChrTalk(    #36
        0x10E,
        (
            "#179F#12PThe building is deliberately designed to be \x01",
            "confusing so as to thwart intruders.\x02\x03",

            "#170FThe staircase to the second floor should be\x01",
            "on the other side of one of the doors within.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B42")

    label("loc_195E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A57")

    ChrTalk(    #37
        0x105,
        (
            "#1383F#12PI believe the building was deliberately\x01",
            "designed to be confusing so as to thwart\x01",
            "would-be intruders.\x02\x03",

            "#1160FThe staircase to the second floor should\x01",
            "be on the other side of one of the doors\x01",
            "within...or so I've heard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B42")

    label("loc_1A57")


    ChrTalk(    #38
        0x10C,
        (
            "#119F#5PThe building was deliberately designed to confuse\x01",
            "would-be intruders.\x02\x03",

            "#110FAnd unless the layout has changed significantly\x01",
            "compared to the real fortress, one of the doors\x01",
            "in here will lead us to the staircase leading up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B6F")

    ChrTalk(    #39
        0x10B,
        "#210F#12PGood to know.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C14")

    label("loc_1B6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B98")

    ChrTalk(    #40
        0x107,
        "#060F#12POh, okay.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C14")

    label("loc_1B98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC0")

    ChrTalk(    #41
        0x106,
        "#051F#12PGot'cha.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C14")

    label("loc_1BC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BE8")

    ChrTalk(    #42
        0x102,
        "#1500F#12PThanks.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C14")

    label("loc_1BE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C14")

    ChrTalk(    #43
        0x101,
        "#1011F#12PO-Oh, right...\x02",
    )

    CloseMessageWindow()

    label("loc_1C14")

    Jump("loc_203D")

    label("loc_1C17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D01")

    ChrTalk(    #44
        0x10C,
        "#115F#5PCorrect.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10E,
        (
            "#170F#12PThe building is deliberately designed to be \x01",
            "confusing so as to thwart intruders as well.\x02\x03",

            "The staircase to the second floor should be\x01",
            "on the other side of one of the doors within.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1D01")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E00")

    ChrTalk(    #46
        0x10C,
        "#115F#5PCorrect.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x105,
        (
            "#1160F#4PI believe the building was deliberately designed\x01",
            "to be confusing so as to thwart intruders.\x02\x03",

            "The staircase to the second floor should be on\x01",
            "the other side of one of the doors within...or\x01",
            "so I've heard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF5")

    label("loc_1E00")


    ChrTalk(    #48
        0x10C,
        (
            "#115F#5PCorrect.\x02\x03",

            "#110FThe building was deliberately designed to confuse\x01",
            "would-be intruders.\x02\x03",

            "And unless the layout has changed significantly\x01",
            "compared to the real fortress, one of the doors\x01",
            "in here will lead us to the staircase leading up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F1C")

    ChrTalk(    #49
        0x10F,
        "#1448F#12PI see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_203D")

    label("loc_1F1C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F50")

    ChrTalk(    #50
        0x10A,
        "#816F#4PThat's encouraging...\x02",
    )

    CloseMessageWindow()
    Jump("loc_203D")

    label("loc_1F50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F84")

    ChrTalk(    #51
        0x103,
        "#1525F#12PHmm... Makes sense.\x02",
    )

    CloseMessageWindow()
    Jump("loc_203D")

    label("loc_1F84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FB5")

    ChrTalk(    #52
        0x108,
        "#070F#12PThat makes sense.\x02",
    )

    CloseMessageWindow()
    Jump("loc_203D")

    label("loc_1FB5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FEC")

    ChrTalk(    #53
        0x104,
        "#1541F#12PThat's understandable.\x02",
    )

    CloseMessageWindow()
    Jump("loc_203D")

    label("loc_1FEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_201D")

    ChrTalk(    #54
        0x10D,
        "#277F#12PThat makes sense.\x02",
    )

    CloseMessageWindow()
    Jump("loc_203D")

    label("loc_201D")


    ChrTalk(    #55
        0x109,
        "#1060F#6PThat makes sense.\x02",
    )

    CloseMessageWindow()

    label("loc_203D")


    ChrTalk(    #56
        0x10C,
        "#116F#5P...All right. Shall we continue?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10C, 0, 400)
    Sleep(300)

    def lambda_207D():
        OP_6D(400, 0, 34740, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_207D)
    OP_8E(0x10C, 0xFFFFFBFA, 0x1F4, 0x8976, 0x7D0, 0x0)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #57
        "\x07\x05Richard unlocked the door using its key.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #58
        0x10C,
        (
            "#115F#5PEveryone!\x02\x03",

            "These trials will be like none that we've ever\x01",
            "faced before.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10C, 180, 400)
    Sleep(300)

    ChrTalk(    #59
        0x10C,
        (
            "#112F#5PYet there is but one clear path for us to take.\x02\x03",

            "#114FSo I must ask: are you with me?\x02\x03",

            "It is only when we fight together that we can\x01",
            "overcome the great wall that stands before\x01",
            "us...and attain victory!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetMessageWindowPos(400, 200, -1, -1)
    SetChrName("Everyone")

    AnonymousTalk(    #60
        "\x07\x00#4SYeah!!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2B1E)
    OP_71(0x1001, 0x0)
    ExitThread()
    OP_64(0x1, 0x1)
    OP_6D(-1110, 0, 33110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1110, 0, 33110, 0)
    SetChrPos(0x1, -1110, 0, 33110, 0)
    SetChrPos(0x2, -1110, 0, 33110, 0)
    SetChrPos(0x3, -1110, 0, 33110, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)

    label("loc_2361")

    TalkEnd(0xFF)
    Return()

    # Function_6_12E0 end

    SaveToFile()

Try(main)
