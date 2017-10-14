from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3300   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60032",
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
        'ED6_DT09/CH10630 ._CH',             # 00
        'ED6_DT09/CH10631 ._CH',             # 01
        'ED6_DT09/CH10640 ._CH',             # 02
        'ED6_DT09/CH10641 ._CH',             # 03
        'ED6_DT09/CH10650 ._CH',             # 04
        'ED6_DT09/CH10651 ._CH',             # 05
        'ED6_DT09/CH10660 ._CH',             # 06
        'ED6_DT09/CH10661 ._CH',             # 07
        'ED6_DT09/CH10670 ._CH',             # 08
        'ED6_DT09/CH10671 ._CH',             # 09
        'ED6_DT09/CH10680 ._CH',             # 0A
        'ED6_DT09/CH10681 ._CH',             # 0B
        'ED6_DT09/CH10690 ._CH',             # 0C
        'ED6_DT09/CH10691 ._CH',             # 0D
        'ED6_DT09/CH10700 ._CH',             # 0E
        'ED6_DT09/CH10701 ._CH',             # 0F
        'ED6_DT29/CH12420 ._CH',             # 10
        'ED6_DT29/CH12421 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT09/CH10630P._CP',             # 00
        'ED6_DT09/CH10631P._CP',             # 01
        'ED6_DT09/CH10640P._CP',             # 02
        'ED6_DT09/CH10641P._CP',             # 03
        'ED6_DT09/CH10650P._CP',             # 04
        'ED6_DT09/CH10651P._CP',             # 05
        'ED6_DT09/CH10660P._CP',             # 06
        'ED6_DT09/CH10661P._CP',             # 07
        'ED6_DT09/CH10670P._CP',             # 08
        'ED6_DT09/CH10671P._CP',             # 09
        'ED6_DT09/CH10680P._CP',             # 0A
        'ED6_DT09/CH10681P._CP',             # 0B
        'ED6_DT09/CH10690P._CP',             # 0C
        'ED6_DT09/CH10691P._CP',             # 0D
        'ED6_DT09/CH10700P._CP',             # 0E
        'ED6_DT09/CH10701P._CP',             # 0F
        'ED6_DT29/CH12420P._CP',             # 10
        'ED6_DT29/CH12421P._CP',             # 11
    )

    DeclMonster(
        X                   = 93670,
        Z                   = -30,
        Y                   = -101140,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E2,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 105420,
        Z                   = 140,
        Y                   = -100870,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 75750,
        Z                   = -50,
        Y                   = -78300,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 106940,
        Z                   = 20,
        Y                   = -79600,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1E7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 39780,
        TriggerZ            = -60,
        TriggerY            = -82680,
        TriggerRange        = 1000,
        ActorX              = 39410,
        ActorZ              = 1440,
        ActorY              = -82290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 100900,
        TriggerZ            = 60,
        TriggerY            = -111450,
        TriggerRange        = 1000,
        ActorX              = 103740,
        ActorZ              = -2060,
        ActorY              = -114730,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1F2",          # 00, 0
        "Function_1_1F3",          # 01, 1
        "Function_2_212",          # 02, 2
        "Function_3_33B",          # 03, 3
    )


    def Function_0_1F2(): pass

    label("Function_0_1F2")

    Return()

    # Function_0_1F2 end

    def Function_1_1F3(): pass

    label("Function_1_1F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_205")
    OP_6F(0x0, 0)
    Jump("loc_20C")

    label("loc_205")

    OP_6F(0x0, 60)

    label("loc_20C")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_1F3 end

    def Function_2_212(): pass

    label("Function_2_212")

    OP_EA(0x2, 0xB7, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_283")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1530)
    Jump("loc_2E7")

    label("loc_283")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_2E7")

    Jump("loc_32D")

    label("loc_2EA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05FUN FACT: That didn't belong to you.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_32D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_212 end

    def Function_3_33B(): pass

    label("Function_3_33B")

    EventBegin(0x1)

    ChrTalk(    #3
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_367():
        OP_6D(101900, 20, -113230, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_367)

    def lambda_37F():
        OP_67(0, 8000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_37F)

    def lambda_397():
        OP_6B(3200, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_397)

    def lambda_3A7():
        OP_6C(90000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_3A7)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #4
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44D")
    OP_C0(0xE, 0x1F, 0x189C0, 0x32, 0xFFFE4C88, 0x8C, 0x193D4, 0xFFFFFA24, 0xFFFE403A)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_45C")

    label("loc_44D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45C")
    EventEnd(0x1)

    label("loc_45C")

    Return()

    # Function_3_33B end

    SaveToFile()

Try(main)
