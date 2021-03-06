from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7418   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7418.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60225",
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
            'ED6_DT21/SUB000  ._SN',
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
        '',                                     # 17
        '',                                     # 18
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
        'ED6_DT29/CH14040 ._CH',             # 00
        'ED6_DT29/CH14040 ._CH',             # 01
        'ED6_DT29/CH14880 ._CH',             # 02
        'ED6_DT29/CH14880 ._CH',             # 03
        'ED6_DT29/CH14890 ._CH',             # 04
        'ED6_DT29/CH14890 ._CH',             # 05
        'ED6_DT29/CH14870 ._CH',             # 06
        'ED6_DT29/CH14870 ._CH',             # 07
        'ED6_DT29/CH14820 ._CH',             # 08
        'ED6_DT29/CH14820 ._CH',             # 09
        'ED6_DT29/CH14610 ._CH',             # 0A
        'ED6_DT29/CH14610 ._CH',             # 0B
        'ED6_DT29/CH14840 ._CH',             # 0C
        'ED6_DT29/CH14840 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH14040P._CP',             # 00
        'ED6_DT29/CH14040P._CP',             # 01
        'ED6_DT29/CH14880P._CP',             # 02
        'ED6_DT29/CH14880P._CP',             # 03
        'ED6_DT29/CH14890P._CP',             # 04
        'ED6_DT29/CH14890P._CP',             # 05
        'ED6_DT29/CH14870P._CP',             # 06
        'ED6_DT29/CH14870P._CP',             # 07
        'ED6_DT29/CH14820P._CP',             # 08
        'ED6_DT29/CH14820P._CP',             # 09
        'ED6_DT29/CH14610P._CP',             # 0A
        'ED6_DT29/CH14610P._CP',             # 0B
        'ED6_DT29/CH14840P._CP',             # 0C
        'ED6_DT29/CH14840P._CP',             # 0D
    )

    DeclMonster(
        X                   = 250,
        Z                   = 0,
        Y                   = 21270,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x321,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 91420,
        Z                   = -4000,
        Y                   = 98630,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x320,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -78960,
        Z                   = -8000,
        Y                   = 20970,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -83000,
        Z                   = -8000,
        Y                   = 17010,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -86980,
        Z                   = -8000,
        Y                   = 21030,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -82930,
        Z                   = -8000,
        Y                   = 24970,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -79010,
        Z                   = 0,
        Y                   = 117030,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -82900,
        Z                   = 0,
        Y                   = 113020,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -86980,
        Z                   = 0,
        Y                   = 116990,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -83020,
        Z                   = 0,
        Y                   = 121080,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x324,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 3920,
        TriggerZ            = 0,
        TriggerY            = -1060,
        TriggerRange        = 1000,
        ActorX              = 3920,
        ActorZ              = 1000,
        ActorY              = -1060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -83000,
        TriggerZ            = -8000,
        TriggerY            = 21000,
        TriggerRange        = 1000,
        ActorX              = -83000,
        ActorZ              = -7000,
        ActorY              = 21000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -82960,
        TriggerZ            = 0,
        TriggerY            = 117030,
        TriggerRange        = 1000,
        ActorX              = -82960,
        ActorZ              = 1000,
        ActorY              = 117030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -83000,
        TriggerZ            = -8000,
        TriggerY            = 24000,
        TriggerRange        = 1000,
        ActorX              = -83000,
        ActorZ              = -7000,
        ActorY              = 24000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -83000,
        TriggerZ            = -8000,
        TriggerY            = 18000,
        TriggerRange        = 1000,
        ActorX              = -83000,
        ActorZ              = -7000,
        ActorY              = 18000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2E6",          # 00, 0
        "Function_1_2FA",          # 01, 1
        "Function_2_412",          # 02, 2
        "Function_3_49D",          # 03, 3
        "Function_4_517",          # 04, 4
        "Function_5_678",          # 05, 5
        "Function_6_807",          # 06, 6
        "Function_7_959",          # 07, 7
        "Function_8_9B9",          # 08, 8
    )


    def Function_0_2E6(): pass

    label("Function_0_2E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_2F9")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_2F9")

    Return()

    # Function_0_2E6 end

    def Function_1_2FA(): pass

    label("Function_1_2FA")

    OP_1B(0x0, 0x0, 0x7)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31D")
    OP_72(0x41E, 0x0)
    ExitThread()
    OP_71(0x41F, 0x0)
    ExitThread()
    Jump("loc_329")

    label("loc_31D")

    OP_71(0x41E, 0x0)
    ExitThread()
    OP_72(0x41F, 0x0)
    ExitThread()

    label("loc_329")

    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x596, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BF")
    OP_6F(0x0, 0)
    Jump("loc_3C6")

    label("loc_3BF")

    OP_6F(0x0, 60)

    label("loc_3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x596, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D8")
    OP_6F(0x1, 0)
    Jump("loc_3DF")

    label("loc_3D8")

    OP_6F(0x1, 60)

    label("loc_3DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x596, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F1")
    OP_6F(0x20, 0)
    Jump("loc_3F8")

    label("loc_3F1")

    OP_6F(0x20, 60)

    label("loc_3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x596, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40A")
    OP_6F(0x21, 0)
    Jump("loc_411")

    label("loc_40A")

    OP_6F(0x21, 60)

    label("loc_411")

    Return()

    # Function_1_2FA end

    def Function_2_412(): pass

    label("Function_2_412")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x596, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_463")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 28)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2CB0)
    Jump("loc_486")

    label("loc_463")


    AnonymousTalk(    #0
        "\x07\x05See you, space priestboy...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_486")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x0, 0x0)
    Return()

    # Function_2_412 end

    def Function_3_49D(): pass

    label("Function_3_49D")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x596, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 28)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2CB1)
    Jump("loc_500")

    label("loc_4EE")


    AnonymousTalk(    #1
        "\x07\x05Good luck!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_500")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x0, 0x0)
    Return()

    # Function_3_49D end

    def Function_4_517(): pass

    label("Function_4_517")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x596, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x20, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_585")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Found \x1F\x05\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CB2)
    Jump("loc_5ED")

    label("loc_585")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x05Found \x1F\x05\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x05\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x20, 60)
    OP_70(0x20, 0x0)

    label("loc_5ED")

    Jump("loc_66A")

    label("loc_5F0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05I'm normally not one for sappy goodbyes, but man... Who knew a chest\x01",
            "could shed tears?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_66A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_517 end

    def Function_5_678(): pass

    label("Function_5_678")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x596, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_751")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x21, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x206, 1)"), scpexpr(EXPR_END)), "loc_6E6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Found \x1F\x06\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2CB3)
    Jump("loc_74E")

    label("loc_6E6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05Found \x1F\x06\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x06\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x21, 60)
    OP_70(0x21, 0x0)

    label("loc_74E")

    Jump("loc_7F9")

    label("loc_751")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Trails means the world to me. I'm happy I could share my world with you.\x01",
            "Thank you for giving this wonderful series a chance. -- 'B'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_7F9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_678 end

    def Function_6_807(): pass

    label("Function_6_807")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, -570, 0, -2040, 0)
    SetChrPos(0x1, 970, 0, -2080, 0)
    SetChrPos(0x2, -780, 0, -3720, 0)
    SetChrPos(0x3, 950, 0, -3720, 0)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    OP_6D(610, 0, 38510, 0)
    OP_67(0, 12160, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(462, 0)

    def lambda_8C9():
        OP_6D(40, 0, -1760, 8000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8C9)

    def lambda_8E1():
        OP_67(0, 12160, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8E1)

    def lambda_8F9():
        OP_6B(3120, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_8F9)

    def lambda_909():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_909)

    def lambda_919():
        OP_6E(462, 8000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_919)
    FadeToBright(1000, 0)
    OP_0D()
    OP_C8(0x200, 0x46, "C_PLAC39._CH", 0x0, 0x3E8)
    WaitChrThread(0x0, 0x0)
    Fade(1000)
    OP_AA(65282)
    ClearMapFlags(0x2000000)
    EventEnd(0x0)
    Return()

    # Function_6_807 end

    def Function_7_959(): pass

    label("Function_7_959")

    EventBegin(0x1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05The door has already closed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_7_959 end

    def Function_8_9B9(): pass

    label("Function_8_9B9")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Strange power is overflowing from the orb.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A54"),
        (1, "loc_AF2"),
        (SWITCH_DEFAULT, "loc_AF2"),
    )


    label("loc_A54")

    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x82, 0x0)
    OP_1D(0xE1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_AF2")

    TalkEnd(0xFF)
    Return()

    # Function_8_9B9 end

    SaveToFile()

Try(main)
