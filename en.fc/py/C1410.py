from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1410   ._SN',
        MapName             = 'Bose',
        Location            = 'C1410.x',
        MapIndex            = 62,
        MapDefaultBGM       = "ed60015",
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
        'Whemler',                              # 9
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
        Unknown_3A              = 62,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01680 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01680P._CP',             # 00
    )

    DeclNpc(
        X                   = 3200,
        Z                   = 0,
        Y                   = 33900,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = 3930,
        TriggerZ            = 0,
        TriggerY            = 39420,
        TriggerRange        = 800,
        ActorX              = 5010,
        ActorZ              = 1500,
        ActorY              = 39620,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F6",           # 00, 0
        "Function_1_F7",           # 01, 1
        "Function_2_F8",           # 02, 2
        "Function_3_10E",          # 03, 3
        "Function_4_61A",          # 04, 4
    )


    def Function_0_F6(): pass

    label("Function_0_F6")

    Return()

    # Function_0_F6 end

    def Function_1_F7(): pass

    label("Function_1_F7")

    Return()

    # Function_1_F7 end

    def Function_2_F8(): pass

    label("Function_2_F8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_F8")

    label("loc_10D")

    Return()

    # Function_2_F8 end

    def Function_3_10E(): pass

    label("Function_3_10E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_339")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Shop\x01",              # 1
            "Share a meal\x01",      # 2
            "Leave\x01",             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_182")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x6F)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_182")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_316")
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DC")
    OP_31(0x3, 0x2, 0x1)
    OP_31(0x3, 0x5, 0x64)
    Jump("loc_21A")

    label("loc_1DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F6")
    OP_31(0x2, 0x2, 0x1)
    OP_31(0x2, 0x5, 0x64)
    Jump("loc_21A")

    label("loc_1F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_210")
    OP_31(0x0, 0x2, 0x1)
    OP_31(0x0, 0x5, 0x64)
    Jump("loc_21A")

    label("loc_210")

    OP_31(0x1, 0x2, 0x1)
    OP_31(0x1, 0x5, 0x64)

    label("loc_21A")

    Jump("loc_290")

    label("loc_21D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_245")
    OP_31(0x2, 0x2, 0x1)
    OP_31(0x2, 0x5, 0x64)
    Jump("loc_269")

    label("loc_245")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x42), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_25F")
    OP_31(0x0, 0x2, 0x1)
    OP_31(0x0, 0x5, 0x64)
    Jump("loc_269")

    label("loc_25F")

    OP_31(0x1, 0x2, 0x1)
    OP_31(0x1, 0x5, 0x64)

    label("loc_269")

    Jump("loc_290")

    label("loc_26C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_286")
    OP_31(0x0, 0x2, 0x1)
    OP_31(0x0, 0x5, 0x64)
    Jump("loc_290")

    label("loc_286")

    OP_31(0x1, 0x2, 0x1)
    OP_31(0x1, 0x5, 0x64)

    label("loc_290")


    AnonymousTalk(    #0
        "\x06\x07\x00Ate \x07\x02Abaddon Potluck\x07\x00.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x8)"), scpexpr(EXPR_END)), "loc_2C8")
    Jump("loc_2F9")

    label("loc_2C8")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06\x07\x00Learned '\x07\x02Abaddon Potluck\x07\x00' recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_2F9")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_316")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_330")
    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    label("loc_330")

    FadeToBright(300, 0)

    label("loc_339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_457")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_410")
    OP_A2(0x0)

    ChrTalk(    #2
        0x8,
        (
            "Well, what brings you to\x01",
            "a place like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "From the looks of you, you\x01",
            "appear to be bracers. Are\x01",
            "you here on a job?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "There's not much I can offer you,\x01",
            "but make yourselves at home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_454")

    label("loc_410")


    ChrTalk(    #5
        0x8,
        (
            "If you need to take a rest, you're\x01",
            "welcome to use the bed too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_454")

    Jump("loc_616")

    label("loc_457")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_548")
    OP_A2(0x0)

    ChrTalk(    #6
        0x8,
        "What a surprise to have visitors...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "You don't appear to be mountain\x01",
            "climbers...but you seem rather\x01",
            "worn out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "How about lying down and\x01",
            "resting for a bit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "You're welcome to use anything\x01",
            "you like in this place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_616")

    label("loc_548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_616")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DE")
    OP_A2(0x0)

    ChrTalk(    #10
        0x8,
        (
            "You've done rather well to\x01",
            "make it to this place...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "There's not much I can offer you,\x01",
            "but make yourselves comfortable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_616")

    label("loc_5DE")


    ChrTalk(    #12
        0x8,
        (
            "If you need it, you're welcome\x01",
            "to use the bed too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_616")

    TalkEnd(0x8)
    Return()

    # Function_3_10E end

    def Function_4_61A(): pass

    label("Function_4_61A")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B7")
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_6B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D1")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_6D1")

    Return()

    # Function_4_61A end

    SaveToFile()

Try(main)
