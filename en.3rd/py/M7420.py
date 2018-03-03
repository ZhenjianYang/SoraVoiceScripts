from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M7420   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7420.x',
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
        X                   = -22920,
        Z                   = 0,
        Y                   = 1630,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x322,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 72250,
        Z                   = -6000,
        Y                   = -95530,
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
        X                   = 161310,
        Z                   = -4000,
        Y                   = 2650,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x320,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -22950,
        TriggerZ            = 0,
        TriggerY            = 13060,
        TriggerRange        = 1000,
        ActorX              = -22950,
        ActorZ              = 1000,
        ActorY              = 13060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 153050,
        TriggerZ            = 0,
        TriggerY            = 13030,
        TriggerRange        = 1000,
        ActorX              = 153050,
        ActorZ              = 1000,
        ActorY              = 13030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 163030,
        TriggerZ            = -4000,
        TriggerY            = 21030,
        TriggerRange        = 1000,
        ActorX              = 163030,
        ActorZ              = -3000,
        ActorY              = 21030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1DA",          # 00, 0
        "Function_1_1DB",          # 01, 1
        "Function_2_2BB",          # 02, 2
        "Function_3_361",          # 03, 3
        "Function_4_3ED",          # 04, 4
    )


    def Function_0_1DA(): pass

    label("Function_0_1DA")

    Return()

    # Function_0_1DA end

    def Function_1_1DB(): pass

    label("Function_1_1DB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_PUSH_LONG, 0xF3C), scpexpr(EXPR_NEG), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_20D")
    OP_E5(0x0, 0xFF, 0x1, 1)
    OP_E5(0x0, 0xFF, 0x17, 1)
    OP_E5(0x1, 0xFF, 0x2, 1)
    OP_E5(0x1, 0xFF, 0x18, 1)
    Jump("loc_22D")

    label("loc_20D")

    OP_E5(0x1, 0xFF, 0x1, 1)
    OP_E5(0x1, 0xFF, 0x17, 1)
    OP_E5(0x0, 0xFF, 0x2, 1)
    OP_E5(0x0, 0xFF, 0x18, 1)

    label("loc_22D")

    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_281")
    OP_6F(0x0, 0)
    Jump("loc_288")

    label("loc_281")

    OP_6F(0x0, 60)

    label("loc_288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29A")
    OP_6F(0x1, 0)
    Jump("loc_2A1")

    label("loc_29A")

    OP_6F(0x1, 60)

    label("loc_2A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B3")
    OP_6F(0x2, 0)
    Jump("loc_2BA")

    label("loc_2B3")

    OP_6F(0x2, 60)

    label("loc_2BA")

    Return()

    # Function_1_1DB end

    def Function_2_2BB(): pass

    label("Function_2_2BB")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C")
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
    OP_A2(0x2CB8)
    Jump("loc_34A")

    label("loc_30C")


    AnonymousTalk(    #0
        "\x07\x05These are the kinds of stories that turn into legends.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_34A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x0, 0x0)
    Return()

    # Function_2_2BB end

    def Function_3_361(): pass

    label("Function_3_361")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B2")
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
    OP_A2(0x2CB9)
    Jump("loc_3D6")

    label("loc_3B2")


    AnonymousTalk(    #1
        "\x07\x05Promise me we'll meet again!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_3D6")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x0, 0x0)
    Return()

    # Function_3_361 end

    def Function_4_3ED(): pass

    label("Function_4_3ED")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x597, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Call(6, 24)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2CBA)
    Jump("loc_452")

    label("loc_43E")


    AnonymousTalk(    #2
        "\x07\x05Empty. Oops.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_452")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x0, 0x0)
    Return()

    # Function_4_3ED end

    SaveToFile()

Try(main)
