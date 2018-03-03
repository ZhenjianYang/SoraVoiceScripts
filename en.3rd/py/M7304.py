from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7304   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7304.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60175",
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
        'Elmer',                                # 9
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
        'ED6_DT29/CH14430 ._CH',             # 00
        'ED6_DT29/CH14431 ._CH',             # 01
        'ED6_DT27/CH03471 ._CH',             # 02
        'ED6_DT26/CH20723 ._CH',             # 03
        'ED6_DT29/CH14550 ._CH',             # 04
        'ED6_DT29/CH14551 ._CH',             # 05
        'ED6_DT29/CH14440 ._CH',             # 06
        'ED6_DT29/CH14440 ._CH',             # 07
        'ED6_DT29/CH14140 ._CH',             # 08
        'ED6_DT29/CH14140 ._CH',             # 09
        'ED6_DT29/CH14150 ._CH',             # 0A
        'ED6_DT29/CH14150 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT29/CH14430P._CP',             # 00
        'ED6_DT29/CH14431P._CP',             # 01
        'ED6_DT27/CH03471P._CP',             # 02
        'ED6_DT26/CH20723P._CP',             # 03
        'ED6_DT29/CH14550P._CP',             # 04
        'ED6_DT29/CH14551P._CP',             # 05
        'ED6_DT29/CH14440P._CP',             # 06
        'ED6_DT29/CH14440P._CP',             # 07
        'ED6_DT29/CH14140P._CP',             # 08
        'ED6_DT29/CH14140P._CP',             # 09
        'ED6_DT29/CH14150P._CP',             # 0A
        'ED6_DT29/CH14150P._CP',             # 0B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -43630,
        Z                   = 18980,
        Y                   = 25220,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -36020,
        Z                   = 21340,
        Y                   = 50150,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -49770,
        Z                   = 24490,
        Y                   = 60070,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -48120,
        Z                   = 29440,
        Y                   = 88230,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BE,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -84510,
        Z                   = 36540,
        Y                   = 87440,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2BD,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -83350,
        Z                   = 45800,
        Y                   = 124250,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2C3,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -5510,
        Y                   = 6000,
        Z                   = 16230,
        Range               = 4720,
        Unknown_10          = 0x2EE0,
        Unknown_14          = 0x4B64,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = -34630,
        TriggerZ            = 21300,
        TriggerY            = 56020,
        TriggerRange        = 1000,
        ActorX              = -34630,
        ActorZ              = 22300,
        ActorY              = 56020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -31580,
        TriggerZ            = 21300,
        TriggerY            = 56540,
        TriggerRange        = 1000,
        ActorX              = -31580,
        ActorZ              = 22300,
        ActorY              = 56540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30310,
        TriggerZ            = 21300,
        TriggerY            = 51290,
        TriggerRange        = 1000,
        ActorX              = -30310,
        ActorZ              = 22300,
        ActorY              = 51290,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -39480,
        TriggerZ            = 21300,
        TriggerY            = 53160,
        TriggerRange        = 1000,
        ActorX              = -39480,
        ActorZ              = 22300,
        ActorY              = 53160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -81110,
        TriggerZ            = 36500,
        TriggerY            = 79820,
        TriggerRange        = 1000,
        ActorX              = -81110,
        ActorZ              = 37500,
        ActorY              = 79820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2A6",          # 00, 0
        "Function_1_2A7",          # 01, 1
        "Function_2_362",          # 02, 2
        "Function_3_480",          # 03, 3
        "Function_4_59E",          # 04, 4
        "Function_5_6BC",          # 05, 5
        "Function_6_7DA",          # 06, 6
        "Function_7_8F8",          # 07, 7
        "Function_8_909",          # 08, 8
        "Function_9_1120",         # 09, 9
        "Function_10_1BD8",        # 0A, 10
    )


    def Function_0_2A6(): pass

    label("Function_0_2A6")

    Return()

    # Function_0_2A6 end

    def Function_1_2A7(): pass

    label("Function_1_2A7")

    OP_16(0x2, 0xFA0, 0xFFFD6FC0, 0xFFFEF660, 0x230097)
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F6")
    OP_6F(0x0, 0)
    Jump("loc_2FD")

    label("loc_2F6")

    OP_6F(0x0, 60)

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F")
    OP_6F(0x1, 0)
    Jump("loc_316")

    label("loc_30F")

    OP_6F(0x1, 60)

    label("loc_316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328")
    OP_6F(0x2, 0)
    Jump("loc_32F")

    label("loc_328")

    OP_6F(0x2, 60)

    label("loc_32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341")
    OP_6F(0x3, 0)
    Jump("loc_348")

    label("loc_341")

    OP_6F(0x3, 60)

    label("loc_348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35A")
    OP_6F(0x4, 0)
    Jump("loc_361")

    label("loc_35A")

    OP_6F(0x4, 60)

    label("loc_361")

    Return()

    # Function_1_2A7 end

    def Function_2_362(): pass

    label("Function_2_362")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x55B, 1)"), scpexpr(EXPR_END)), "loc_3D0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\x5B\x05\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C68)
    Jump("loc_438")

    label("loc_3D0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\x5B\x05\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x5B\x05\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_438")

    Jump("loc_472")

    label("loc_43B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_472")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_362 end

    def Function_3_480(): pass

    label("Function_3_480")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_559")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x6E, 1)"), scpexpr(EXPR_END)), "loc_4EE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\x6E\x00\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C69)
    Jump("loc_556")

    label("loc_4EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\x6E\x00\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x6E\x00\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_556")

    Jump("loc_590")

    label("loc_559")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_590")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_480 end

    def Function_4_59E(): pass

    label("Function_4_59E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_677")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_60C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\x01\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C6A)
    Jump("loc_674")

    label("loc_60C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\x01\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x01\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_674")

    Jump("loc_6AE")

    label("loc_677")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_6AE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_59E end

    def Function_5_6BC(): pass

    label("Function_5_6BC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_795")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_72A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\xF7\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C6B)
    Jump("loc_792")

    label("loc_72A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Found \x1F\xF7\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF7\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_792")

    Jump("loc_7CC")

    label("loc_795")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_7CC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_6BC end

    def Function_6_7DA(): pass

    label("Function_6_7DA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x59C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x18E, 1)"), scpexpr(EXPR_END)), "loc_848")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05Found \x1F\x8E\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CE0)
    Jump("loc_8B0")

    label("loc_848")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05Found \x1F\x8E\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x8E\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_8B0")

    Jump("loc_8EA")

    label("loc_8B3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_8EA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_7DA end

    def Function_7_8F8(): pass

    label("Function_7_8F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x581, 5)), scpexpr(EXPR_END)), "loc_900")
    Return()

    label("loc_900")

    Call(0, 8)
    Call(0, 9)
    Return()

    # Function_7_8F8 end

    def Function_8_909(): pass

    label("Function_8_909")

    EventBegin(0x0)
    OP_D2(0x270176, 0x270183, 0xC)
    OP_D2(0x270177, 0x270184, 0xD)
    OP_D2(0x270178, 0x270185, 0xE)
    OP_D2(0x27058C, 0x270590, 0xF)
    OP_D2(0x27058D, 0x270591, 0x10)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 110, 9040, 30080, 180)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_964():

        label("loc_964")

        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        OP_48()
        Jump("loc_964")

    QueueWorkItem2(0x10, 3, lambda_964)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x02#80W#3SGaaah.... Graaaaaah!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_A11():
        OP_6D(-840, 9030, 31100, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_A11)

    def lambda_A29():
        OP_67(0, 5220, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_A29)

    def lambda_A41():
        OP_6B(2560, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_A41)

    def lambda_A51():
        OP_6C(315000, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_A51)

    def lambda_A61():
        OP_6E(335, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_A61)

    def lambda_A71():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_A71)
    Sleep(100)
    OP_8C(0x1, 0, 400)
    WaitChrThread(0xEE, 0x1)
    OP_22(0x1D9, 0x0, 0x64)
    Fade(1000)

    def lambda_A9A():
        OP_6B(2300, 500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_A9A)

    def lambda_AAA():
        OP_6E(360, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_AAA)

    def lambda_ABA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_ABA)
    OP_22(0x1E0, 0x0, 0x64)
    OP_0D()
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEE, 0x1)
    OP_23(0x1D9)
    Sleep(1000)
    SetChrPos(0x109, -60, 8580, 18720, 0)
    SetChrPos(0x10F, -1370, 8620, 18810, 0)

    def lambda_B0B():
        OP_6D(-1900, 9040, 27710, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_B0B)

    def lambda_B23():
        OP_67(0, 5450, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_B23)

    def lambda_B3B():
        OP_6B(2780, 2500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_B3B)

    def lambda_B4B():
        OP_6E(313, 2500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_B4B)

    def lambda_B5B():
        OP_8E(0xFE, 0xFFFFFF7E, 0x2350, 0x5A28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B5B)
    Sleep(400)

    def lambda_B7B():
        OP_8E(0xFE, 0xFFFFF9FC, 0x2350, 0x59E2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_B7B)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        (
            "\x07\x02#80WPlease...\x01",
            "Let me...eat you...\x01",
            "#1000W \x01",
            "#80WI... I'm so...#500W \x01",
            "#80WI'm so, so hungry...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #17
        0x10F,
        "#1934F#6P...A-A child...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x109,
        (
            "#1076F#6PHis name's Elmer...\x02\x03",

            "He was a young boy turned into a flesh-eating\x01",
            "monster by a fanatical devil-worshiping cult.\x01",
            "They did it all through a ritual involving artifacts.\x02\x03",

            "#1065FI tried everything I could to save him--every kind\x01",
            "of Thaumaturgy I could think of...but eventually,\x01",
            "the only option was to put him out of his misery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10F,
        "#1949F#6PNo...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "\x07\x02#80WI can...right...?\x01",
            "#1000W \x01",
            "#80WYou both look so tasty...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        (
            "\x07\x02#80WSo go on...#500W \x01",
            "#80WIt won't hurt...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #22
        0x10F,
        "#1950F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        (
            "#1065F#6PYou didn't deserve this, kid...\x02\x03",

            "...but I'm not gonna blame Aidios, either.\x02\x03",

            "#1067FIf you want to resent someone...resent me.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x109, 12)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 15)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(700)

    ChrTalk(    #24
        0x109,
        "#1844F#6PSo...let me put you to peace a second time.\x02",
    )

    CloseMessageWindow()

    def lambda_FA4():

        label("loc_FA4")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_FA4")

    QueueWorkItem2(0x10, 3, lambda_FA4)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x02#40W#3SNo! I don't wanna die!\x07\x00\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_43(0x10, 0x1, 0x0, 0xA)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "\x07\x02#80WI just... I just...#1000W \x01",
            "#40W#4SI just don't want to be hungry anymore!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_10A3():
        OP_6D(-2070, 9040, 25590, 300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_10A3)

    def lambda_10BB():
        OP_67(0, 6120, -10000, 300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_10BB)

    def lambda_10D3():
        OP_6B(2150, 300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_10D3)

    def lambda_10E3():
        OP_6E(280, 300)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_10E3)
    SetChrChipByIndex(0x10, 1)

    def lambda_10F8():
        OP_8F(0xFE, 0xFFFFFC7C, 0x2350, 0x5D02, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_10F8)
    WaitChrThread(0xEE, 0x1)
    Battle(0x2CD, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_8_909 end

    def Function_9_1120(): pass

    label("Function_9_1120")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0x109, 0x0)
    OP_44(0x10F, 0x0)
    OP_44(0x10, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x109, -1450, 9040, 26490, 0)
    SetChrPos(0x10F, -1390, 9040, 24190, 0)
    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 3)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-2540, 9000, 30650, 0)
    OP_67(0, 6070, -10000, 0)
    OP_6B(1840, 0)
    OP_6C(315000, 0)
    OP_6E(404, 0)
    Sleep(500)

    def lambda_11C9():
        OP_6D(-2640, 9040, 26660, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_11C9)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #27
        0x109,
        "#1076F#5P#40W...\x02",
    )

    CloseMessageWindow()
    OP_99(0x109, 0x0, 0x3, 0x5DC)
    Sleep(500)

    ChrTalk(    #28
        0x109,
        (
            "#1846F#5P#40WHaha... I didn't wanna get out of bed for a week\x01",
            "after that one.\x02\x03",

            "How times change... This is practically another\x01",
            "day for me now.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #29
        0x10F,
        "#1950F#6P#3SKevin!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_12DB():
        OP_6D(-2610, 9040, 27800, 800)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_12DB)

    def lambda_12F3():
        OP_6B(1800, 800)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_12F3)
    SetChrFlags(0x10F, 0x20)
    SetChrFlags(0x10F, 0x1000)
    SetChrChipByIndex(0x10F, 2)

    def lambda_1312():
        OP_8E(0xFE, 0xFFFFFA42, 0x2350, 0x6464, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_1312)

    def lambda_132D():
        OP_99(0xFE, 0x5, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_132D)
    WaitChrThread(0x10F, 0x1)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0x10F, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(30)
    OP_44(0x10F, 0x0)
    SetChrFlags(0x10F, 0x8)
    OP_99(0x109, 0x8, 0xD, 0xBB8)
    OP_22(0x8F, 0x0, 0x64)
    OP_99(0x109, 0xE, 0xF, 0xBB8)
    WaitChrThread(0xEE, 0x0)
    ClearChrFlags(0x10F, 0x1000)
    Fade(1000)
    OP_6D(-2900, 9040, 25120, 0)
    OP_67(0, 5000, -10000, 0)
    OP_6B(1650, 0)
    OP_6C(230000, 0)
    OP_6E(478, 0)
    SetChrSubChip(0x109, 6)
    OP_0D()
    Sleep(300)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)

    ChrTalk(    #30
        0x10F,
        (
            "#1954F#5P#40WWhy?!\x02\x03",

            "Why have you been trying to deal with all\x01",
            "this all on your own all this time?!\x02\x03",

            "#1950FYou could have at least talked to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x109,
        (
            "#1843F#6P#40WI chose the path I walk by myself, Ries.\x01",
            "What right do I have to drag others down\x01",
            "with me?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_99(0x109, 0x10, 0x12, 0x3E8)
    Sleep(200)

    ChrTalk(    #32
        0x109,
        "#1844F#6P#40WEspecially you.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    Sleep(500)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)

    ChrTalk(    #33
        0x109,
        (
            "#1841F#6P#40W...Nah. That's not why I didn't talk to you\x01",
            "about it at all, is it?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #34
        0x109,
        (
            "#1845F#6P#40WI think more than anything, I was afraid.\x02\x03",

            "I didn't want you to see me trying to hurt\x01",
            "myself. To punish myself...\x02\x03",

            "I was afraid that if you did, the bond between\x01",
            "us would be severed forever, and that thought\x01",
            "alone was too much to bear.\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)

    ChrTalk(    #35
        0x109,
        "#1844F#6P#40WYeah... I bet that was the real reason.\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_99(0x109, 0x20, 0x22, 0x5DC)
    Sleep(300)

    ChrTalk(    #36
        0x10F,
        (
            "#1953F#5P#40WI was right. You're stupid.\x02\x03",

            "You're the stupidest person I've ever met!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x109,
        (
            "#1846F#6P#40WHaha...\x02\x03",

            "Couldn't you use something a little more\x01",
            "affectionate? I called you a dummy before,\x01",
            "right? That one's cute.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x25), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x109, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x27), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)

    ChrTalk(    #38
        0x109,
        "#1840F#6P#40W...Although, I guess being stupid suits me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10F,
        (
            "#1950F#5P#40WYou dummy...\x02\x03",

            "You blockhead... You halfwit...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_99(0x109, 0x28, 0x2D, 0x5DC)

    ChrTalk(    #40
        0x109,
        (
            "#1068F#6P#40WThat's an impressive collection of insults\x01",
            "you've got in stock.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A11():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1A11)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xEE, 0x0)
    SetChrPos(0x109, -1080, 9040, 28640, 180)
    SetChrPos(0x10F, -1190, 9040, 27050, 0)
    ClearChrFlags(0x109, 0x2)
    ClearChrFlags(0x109, 0x800)
    ClearChrFlags(0x10F, 0x8)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(-2380, 9040, 29090, 0)
    OP_67(0, 5420, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(314, 0)
    Sleep(2000)

    def lambda_1AB7():
        OP_6B(2550, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1AB7)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #41
        0x109,
        "#1840F#11P...You okay now, Ries?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10F,
        (
            "#1935F#6PI'm fine. You don't need to worry about me.\x02\x03",

            "#1936FI'll do all I can to get us out of here.\x02\x03",

            "#1933FSo I don't want you to worry about me.\x01",
            "I want you to rely on me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x109,
        "#1078F#11POkay.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C0D)
    OP_28(0x3D, 0x1, 0x4)
    Sleep(300)
    EventEnd(0x0)
    SetMapFlags(0x100000)
    Return()

    # Function_9_1120 end

    def Function_10_1BD8(): pass

    label("Function_10_1BD8")

    Sleep(2000)
    OP_7C(0x0, 0x12C, 0xBB8, 0x320)
    Return()

    # Function_10_1BD8 end

    SaveToFile()

Try(main)
