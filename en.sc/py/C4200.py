from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4200   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        '',                                     # 16
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
        'ED6_DT09/CH10490 ._CH',             # 00
        'ED6_DT09/CH10491 ._CH',             # 01
        'ED6_DT09/CH10500 ._CH',             # 02
        'ED6_DT09/CH10501 ._CH',             # 03
        'ED6_DT09/CH10510 ._CH',             # 04
        'ED6_DT09/CH10511 ._CH',             # 05
        'ED6_DT09/CH11110 ._CH',             # 06
        'ED6_DT09/CH11111 ._CH',             # 07
        'ED6_DT09/CH11120 ._CH',             # 08
        'ED6_DT09/CH11121 ._CH',             # 09
        'ED6_DT09/CH11130 ._CH',             # 0A
        'ED6_DT09/CH11131 ._CH',             # 0B
        'ED6_DT09/CH11140 ._CH',             # 0C
        'ED6_DT09/CH11141 ._CH',             # 0D
        'ED6_DT09/CH11150 ._CH',             # 0E
        'ED6_DT09/CH11151 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT09/CH10490P._CP',             # 00
        'ED6_DT09/CH10491P._CP',             # 01
        'ED6_DT09/CH10500P._CP',             # 02
        'ED6_DT09/CH10501P._CP',             # 03
        'ED6_DT09/CH10510P._CP',             # 04
        'ED6_DT09/CH10511P._CP',             # 05
        'ED6_DT09/CH11110P._CP',             # 06
        'ED6_DT09/CH11111P._CP',             # 07
        'ED6_DT09/CH11120P._CP',             # 08
        'ED6_DT09/CH11121P._CP',             # 09
        'ED6_DT09/CH11130P._CP',             # 0A
        'ED6_DT09/CH11131P._CP',             # 0B
        'ED6_DT09/CH11140P._CP',             # 0C
        'ED6_DT09/CH11141P._CP',             # 0D
        'ED6_DT09/CH11150P._CP',             # 0E
        'ED6_DT09/CH11151P._CP',             # 0F
    )

    DeclMonster(
        X                   = 1040,
        Z                   = 0,
        Y                   = 33740,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x271,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13230,
        Z                   = 0,
        Y                   = 63010,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x271,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 24830,
        Z                   = 0,
        Y                   = 62910,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x271,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -71240,
        Z                   = 0,
        Y                   = 42750,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x271,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -75480,
        Z                   = 0,
        Y                   = -690,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x271,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32930,
        Z                   = 0,
        Y                   = -57110,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x273,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 20530,
        Z                   = 0,
        Y                   = -113240,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x273,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 280,
        Z                   = 0,
        Y                   = -131490,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x273,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -74020,
        TriggerZ            = 0,
        TriggerY            = -15990,
        TriggerRange        = 1000,
        ActorX              = -74020,
        ActorZ              = 1500,
        ActorY              = -16720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12830,
        TriggerZ            = 0,
        TriggerY            = -124920,
        TriggerRange        = 1000,
        ActorX              = 13480,
        ActorZ              = 1500,
        ActorY              = -124890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22010,
        TriggerZ            = 0,
        TriggerY            = -124520,
        TriggerRange        = 1000,
        ActorX              = 21700,
        ActorZ              = 1500,
        ActorY              = -125270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -11770,
        TriggerZ            = 0,
        TriggerY            = 4500,
        TriggerRange        = 1000,
        ActorX              = -11700,
        ActorZ              = -1000,
        ActorY              = 1260,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_29A",          # 00, 0
        "Function_1_29B",          # 01, 1
        "Function_2_315",          # 02, 2
        "Function_3_48E",          # 03, 3
        "Function_4_5E6",          # 04, 4
        "Function_5_73A",          # 05, 5
    )


    def Function_0_29A(): pass

    label("Function_0_29A")

    Return()

    # Function_0_29A end

    def Function_1_29B(): pass

    label("Function_1_29B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AD")
    OP_6F(0x0, 0)
    Jump("loc_2B4")

    label("loc_2AD")

    OP_6F(0x0, 60)

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C6")
    OP_6F(0x1, 0)
    Jump("loc_2CD")

    label("loc_2C6")

    OP_6F(0x1, 60)

    label("loc_2CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF")
    OP_6F(0x2, 0)
    Jump("loc_2E6")

    label("loc_2DF")

    OP_6F(0x2, 60)

    label("loc_2E6")

    OP_E0(0x0, 0xDC, 0xDE, 0xFE, 0xFF, 0x0, 0x0, 0x0, 0x0, 0x96, 0xBF, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_309")
    OP_10(0xF, 0x0)
    OP_10(0x10, 0x1)
    Jump("loc_30F")

    label("loc_309")

    OP_10(0xF, 0x1)
    OP_10(0x10, 0x0)

    label("loc_30F")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_29B end

    def Function_2_315(): pass

    label("Function_2_315")

    OP_EA(0x2, 0xFD, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ED")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1A1, 1)"), scpexpr(EXPR_END)), "loc_386")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xA1\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1710)
    Jump("loc_3EA")

    label("loc_386")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xA1\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xA1\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_3EA")

    Jump("loc_480")

    label("loc_3ED")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05You find a message scratched along the\x01",
            "bottom: 'Loot this chest and do your worst.\x01",
            "But be warned, for ye be cursed.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_480")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_315 end

    def Function_3_48E(): pass

    label("Function_3_48E")

    OP_EA(0x2, 0xFE, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_566")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x160, 1)"), scpexpr(EXPR_END)), "loc_4FF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x60\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1711)
    Jump("loc_563")

    label("loc_4FF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x60\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x60\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_563")

    Jump("loc_5D8")

    label("loc_566")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05You open the chest to find a bandanaed man\x01",
            "hiding inside! Just kidding, it's empty.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5D8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_48E end

    def Function_4_5E6(): pass

    label("Function_4_5E6")

    OP_EA(0x2, 0xFF, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2E2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6BE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xE1, 1)"), scpexpr(EXPR_END)), "loc_657")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "Found \x1F\xE1\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1713)
    Jump("loc_6BB")

    label("loc_657")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "Found \x1F\xE1\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xE1\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_6BB")

    Jump("loc_72C")

    label("loc_6BE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "\x07\x05For every extra item you take from a treasure\x01",
            "chest, a creepy sheep is sheared.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_72C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_5E6 end

    def Function_5_73A(): pass

    label("Function_5_73A")

    EventBegin(0x1)

    ChrTalk(    #9
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_766():
        OP_6D(-12420, 0, 1330, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_766)

    def lambda_77E():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_77E)

    def lambda_796():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_796)

    def lambda_7A6():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_7A6)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84C")
    OP_C0(0xE, 0x2A, 0xFFFFD1B6, 0x0, 0x1194, 0xB4, 0xFFFFCC48, 0x0, 0xFFFFFE2A)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_85B")

    label("loc_84C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85B")
    EventEnd(0x1)

    label("loc_85B")

    Return()

    # Function_5_73A end

    SaveToFile()

Try(main)
