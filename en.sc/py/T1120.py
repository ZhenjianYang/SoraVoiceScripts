from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1120   ._SN',
        MapName             = 'Bose',
        Location            = 'T1120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 0,
        EntryFunctionIndex  = 12,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T1120   ._SN',
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
        'Sein',                                 # 9
        'Cornelius',                            # 10
        'Carrie',                               # 11
        'Sting',                                # 12
        'Aldan',                                # 13
        'Kuwano',                               # 14
        'Lore',                                 # 15
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
        'ED6_DT07/CH01020 ._CH',             # 00
        'ED6_DT07/CH01040 ._CH',             # 01
        'ED6_DT07/CH01550 ._CH',             # 02
        'ED6_DT27/CH03790 ._CH',             # 03
        'ED6_DT07/CH01000 ._CH',             # 04
        'ED6_DT07/CH01120 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
        'ED6_DT07/CH01040P._CP',             # 01
        'ED6_DT07/CH01550P._CP',             # 02
        'ED6_DT27/CH03790P._CP',             # 03
        'ED6_DT07/CH01000P._CP',             # 04
        'ED6_DT07/CH01120P._CP',             # 05
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = 7400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -24500,
        Z                   = 0,
        Y                   = 4690,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -28800,
        Z                   = 0,
        Y                   = 24200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -2460,
        Z                   = 0,
        Y                   = 2950,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -26270,
        Z                   = 0,
        Y                   = 2690,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -22750,
        Z                   = 0,
        Y                   = 4660,
        Direction           = 266,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -28810,
        Z                   = 0,
        Y                   = 1020,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )


    DeclActor(
        TriggerX            = -24000,
        TriggerZ            = 0,
        TriggerY            = 3580,
        TriggerRange        = 700,
        ActorX              = -24500,
        ActorZ              = 1500,
        ActorY              = 4690,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 920,
        TriggerZ            = 0,
        TriggerY            = 6280,
        TriggerRange        = 700,
        ActorX              = 500,
        ActorZ              = 1500,
        ActorY              = 7400,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_202",          # 00, 0
        "Function_1_265",          # 01, 1
        "Function_2_266",          # 02, 2
        "Function_3_3E3",          # 03, 3
        "Function_4_3E8",          # 04, 4
        "Function_5_101B",         # 05, 5
        "Function_6_1020",         # 06, 6
        "Function_7_2539",         # 07, 7
        "Function_8_3070",         # 08, 8
        "Function_9_3899",         # 09, 9
        "Function_10_3A69",        # 0A, 10
        "Function_11_3BF7",        # 0B, 11
        "Function_12_3D05",        # 0C, 12
        "Function_13_3E5B",        # 0D, 13
        "Function_14_3F1D",        # 0E, 14
    )


    def Function_0_202(): pass

    label("Function_0_202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_235")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_223")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_232")

    label("loc_223")

    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xC, 0x10)

    label("loc_232")

    Jump("loc_246")

    label("loc_235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_246")
    SetChrFlags(0xA, 0x10)

    label("loc_246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_264")
    ClearChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_264")
    SetChrFlags(0xB, 0x10)

    label("loc_264")

    Return()

    # Function_0_202 end

    def Function_1_265(): pass

    label("Function_1_265")

    Return()

    # Function_1_265 end

    def Function_2_266(): pass

    label("Function_2_266")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28B")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3CD")

    label("loc_28B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A4")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3CD")

    label("loc_2A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BD")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3CD")

    label("loc_2BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D6")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3CD")

    label("loc_2D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3CD")

    label("loc_2EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_308")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3CD")

    label("loc_308")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_321")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3CD")

    label("loc_321")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3CD")

    label("loc_33A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_353")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3CD")

    label("loc_353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36C")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3CD")

    label("loc_36C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_385")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3CD")

    label("loc_385")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3CD")

    label("loc_39E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B7")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3CD")

    label("loc_3B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CD")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3CD")

    label("loc_3E2")

    Return()

    # Function_2_266 end

    def Function_3_3E3(): pass

    label("Function_3_3E3")

    Call(0, 4)
    Return()

    # Function_3_3E3 end

    def Function_4_3E8(): pass

    label("Function_4_3E8")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_459")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_44E")
    OP_A9(0x53)
    Jump("loc_450")

    label("loc_44E")

    OP_A9(0x33)

    label("loc_450")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_459")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46A")
    TalkEnd(0x8)
    Return()

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_63E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55C")

    ChrTalk(    #0
        0x8,
        (
            "Well, damn it. Not getting any business\x01",
            "at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "This is what happens when the Goddess\x01",
            "just decides to flick the off switch on\x01",
            "your most important product!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "Most folk just aren't interested in\x01",
            "melee weapons.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_63B")

    label("loc_55C")


    ChrTalk(    #3
        0x8,
        (
            "Normally, we get a pretty decent stream\x01",
            "of casual customers. Folks just looking\x01",
            "to defend themselves, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "But our orbal guns aren't working,\x01",
            "and that's what those sorts of customers\x01",
            "are usually looking for.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63B")

    Jump("loc_1017")

    label("loc_63E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_762")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71E")

    ChrTalk(    #5
        0x8,
        (
            "Now, NEXT DOOR they're busier than\x01",
            "bees, but with my guns not working,\x01",
            "I've got nothing but free time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "Good news is, I have a full stock\x01",
            "of non-orbal weapons for you bracer\x01",
            "types. Take a look!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_75F")

    label("loc_71E")


    ChrTalk(    #7
        0x8,
        (
            "You're the only business I have,\x01",
            "so please, take your time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75F")

    Jump("loc_1017")

    label("loc_762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_85E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7DC")

    ChrTalk(    #8
        0x8,
        (
            "It's a big relief, having that dragon\x01",
            "madness settled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "Now I can finally get back to business.\x02",
    )

    CloseMessageWindow()
    Jump("loc_85B")

    label("loc_7DC")


    ChrTalk(    #10
        0x8,
        "Hey, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "It's a big relief, having that dragon\x01",
            "madness settled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "Now I can finally get back to business.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_85B")

    Jump("loc_1017")

    label("loc_85E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_C9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x348, 7)), scpexpr(EXPR_END)), "loc_A3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_980")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8E6")

    ChrTalk(    #13
        0x8,
        (
            "I wonder what happened to that plan\x01",
            "the Royal Army had.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        "There's been no news about it at all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_97D")

    label("loc_8E6")


    ChrTalk(    #15
        0x8,
        (
            "I wonder what happened to that\x01",
            "plan the Royal Army had.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "I know it involved quite a bit of the air\x01",
            "force, but there's been no news at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_97D")

    Jump("loc_A37")

    label("loc_980")

    TurnDirection(0x8, 0x106, 0)

    ChrTalk(    #17
        0x8,
        (
            "I still don't know what it is you want to\x01",
            "cut with that thing, kid, but don't worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "That's the toughest sword I've ever sold.\x01",
            "You swing that thing like you mean it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A37")

    Jump("loc_C9C")

    label("loc_A3A")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x106, 0)
    Sleep(400)

    ChrTalk(    #19
        0x8,
        (
            "Oh, hey, kid.\x01",
            "How's the sword?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x106,
        (
            "#050FNo problems with it right now.\x02\x03",

            "Seems like the unit Russell sent us is\x01",
            "staying on tight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "Good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "That sword itself the toughest damn\x01",
            "thing I've EVER sold, so you swing that\x01",
            "thing like you mean it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x106,
        (
            "#050FDon't need to tell me.\x01",
            "That was the plan anyway.\x02\x03",

            "#552FReally hope it holds out for at least\x01",
            "two or three hits...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(    #24
        0x8,
        (
            "I'm still not sure what you're\x01",
            "on about...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "Well! If anything comes up, come by\x01",
            "again. I'll be happy to sharpen the edge\x01",
            "or tune that device of yours!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A47)
    OP_A2(0x1)

    label("loc_C9C")

    Jump("loc_1017")

    label("loc_C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_E8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D52")

    ChrTalk(    #26
        0x8,
        (
            "Those poor folk from the Market are\x01",
            "working out of the hotel and bar now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "It's kept things at least a little\x01",
            "normal for the rest of the town,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E8A")

    label("loc_D52")


    ChrTalk(    #28
        0x8,
        (
            "Those poor folk from the Market are\x01",
            "working out of the hotel and bar now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        (
            "They apparently agreed to keep going thanks\x01",
            "to a request from Mayor Maybelle. She can\x01",
            "work miracles when she needs to!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        (
            "Thanks to that, things are still pretty normal\x01",
            "for most folk, at least when it comes to\x01",
            "necessities.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E8A")

    Jump("loc_1017")

    label("loc_E8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_FC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F0F")

    ChrTalk(    #31
        0x8,
        "Is the market itself okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "If it closes, that'll disrupt every single\x01",
            "thing that goes on in this town.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FC5")

    label("loc_F0F")


    ChrTalk(    #33
        0x8,
        "What a thing to happen!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "I know some people were injured,\x01",
            "but is the market itself okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        (
            "If it closes, that'll disrupt every single\x01",
            "thing that goes on in this town.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_FC5")

    Jump("loc_1017")

    label("loc_FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1017")

    ChrTalk(    #36
        0x8,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "I've got some good stuff in stock.\x01",
            "Take a look!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1017")

    TalkEnd(0x8)
    Return()

    # Function_4_3E8 end

    def Function_5_101B(): pass

    label("Function_5_101B")

    Call(0, 6)
    Return()

    # Function_5_101B end

    def Function_6_1020(): pass

    label("Function_6_1020")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1075")
    Call(6, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1061")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1056")
    OP_A9(0x52)
    Jump("loc_1058")

    label("loc_1056")

    OP_A9(0x32)

    label("loc_1058")

    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_1061")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1072")
    TalkEnd(0x9)
    Return()

    label("loc_1072")

    Jump("loc_1C7F")

    label("loc_1075")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C7F")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -23800, 0, 2400, 0)
    SetChrPos(0x102, -24600, 0, 2200, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DC")
    SetChrPos(0xF9, -24200, 0, 1200, 0)
    SetChrPos(0xF8, -25100, 0, 1000, 0)
    Jump("loc_10FE")

    label("loc_10DC")

    SetChrPos(0xF8, -24200, 0, 1200, 0)
    SetChrPos(0xF9, -25100, 0, 1000, 0)

    label("loc_10FE")

    OP_8C(0x9, 180, 0)
    OP_6D(-24840, 0, 3030, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(    #38
        0x9,
        "Oh, uh, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "I'm sorry you've come all this way, but\x01",
            "we're currently not taking any business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        "None of our equipment is working, you see.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1258")

    ChrTalk(    #41
        0x101,
        (
            "#1018F#6POh, right, of course.\x01",
            "Don't worry, though!\x02\x03",

            "I THINK we have a little something to\x01",
            "help with that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x9,
        "A little...what?\x02",
    )

    CloseMessageWindow()
    Jump("loc_17F4")

    label("loc_1258")


    ChrTalk(    #43
        0x101,
        (
            "#1026F#6POhhh, right.\x02\x03",

            "#1015FWell, that's kind of a problem,\x01",
            "isn't it?\x02\x03",

            "If we can't manufacture quartz or\x01",
            "upgrade our slots, we're kinda\x01",
            "in trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1346")

    ChrTalk(    #44
        0x103,
        (
            "#025FYes, it would be something of a waste\x01",
            "of our generators.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144F")

    label("loc_1346")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B1")

    ChrTalk(    #45
        0x108,
        (
            "#072FIt does seem a waste of our generators,\x01",
            "not getting the most from our orbments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144F")

    label("loc_13B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_144F")

    ChrTalk(    #46
        0x106,
        (
            "#552FKeep in mind we ARE kind of lucky to\x01",
            "even have arts right now.\x02\x03",

            "Does feel like a waste to just be sittin'\x01",
            "on all this sepith, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_144F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14AD")

    ChrTalk(    #47
        0x107,
        (
            "#064FOh, but, Estelle!\x02\x03",

            "If it's just for a minute,\x01",
            "we can do something!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1527")

    label("loc_14AD")


    ChrTalk(    #48
        0x102,
        (
            "#1043FTrue, but...I wonder.\x02\x03",

            "#1040FGiven the nature of our 'toys,'\x01",
            "I think the solution may be right\x01",
            "in front of us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1527")

    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15A4")

    def lambda_1557():
        TurnDirection(0x0, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1557)
    Sleep(120)

    def lambda_156A():
        TurnDirection(0x1, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_156A)

    def lambda_1578():
        TurnDirection(0x2, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_1578)
    Sleep(120)

    def lambda_158B():
        TurnDirection(0x3, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_158B)

    def lambda_1599():
        TurnDirection(0x9, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1599)
    Jump("loc_15AB")

    label("loc_15A4")

    TurnDirection(0x101, 0x102, 400)

    label("loc_15AB")

    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    ChrTalk(    #49
        0x101,
        "#1004F#4PReally?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1615")

    ChrTalk(    #50
        0x106,
        "#052F#6PYou think we can use the factory?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1683")

    label("loc_1615")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1650")

    ChrTalk(    #51
        0x103,
        "#023F#6PWe can use the factory? How?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1683")

    label("loc_1650")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1683")

    ChrTalk(    #52
        0x108,
        "#073F#6PWe can use their tools?\x02",
    )

    CloseMessageWindow()

    label("loc_1683")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16E2")

    ChrTalk(    #53
        0x107,
        (
            "#060FYeah, we should be able to!\x02\x03",

            "Our ZFGs work with anything, remember!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1740")

    label("loc_16E2")


    ChrTalk(    #54
        0x102,
        (
            "#1040F#6PWell, can't we?\x02\x03",

            "Our ZFGs can restore operation to ANY\x01",
            "orbal device, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1740")


    ChrTalk(    #55
        0x101,
        "#1018F#6PRight, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        "Errr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        "Zee Eff Gee...? What are you talking about?\x02",
    )

    CloseMessageWindow()

    def lambda_17A4():
        TurnDirection(0x0, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_17A4)
    Sleep(120)

    def lambda_17B7():
        TurnDirection(0x1, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_17B7)

    def lambda_17C5():
        TurnDirection(0x2, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_17C5)
    Sleep(120)

    def lambda_17D8():
        TurnDirection(0x3, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_17D8)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)

    label("loc_17F4")


    ChrTalk(    #58
        0x102,
        "#1040F#6PLet me explain.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #59
        (
            "\x07\x05Joshua explained that by using the Zero Field Generator the\x01",
            "factory's functionality could be temporarily restored.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #60
        0x9,
        "That's absolutely incredible!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "Please, by all means!\x01",
            "I'd love it if it worked!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1006F#6PLet's give it a shot, then.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_196B")

    ChrTalk(    #63
        0x107,
        "#560FOkay, give me just a second!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1996")

    label("loc_196B")


    ChrTalk(    #64
        0x102,
        "#1040F#6PGive me just a moment, then.\x02",
    )

    CloseMessageWindow()

    label("loc_1996")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_22(0x9D, 0x0, 0x64)
    OP_8C(0x9, 270, 0)
    SetChrName("")

    AnonymousTalk(    #65
        (
            "\x07\x05On activation, the Zero Field Generator restored\x01",
            "power to the factory's tools.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #66
        0x9,
        "The equipment's working!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A5C")
    TurnDirection(0x9, 0x0, 400)
    Jump("loc_1B8C")

    label("loc_1A5C")


    ChrTalk(    #67
        0x101,
        "#1000F#6PAwesome!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AD2")

    ChrTalk(    #68
        0x107,
        (
            "#063FWell, it worked for now.\x02\x03",

            "#561FIt won't last for very long, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B67")

    label("loc_1AD2")


    ChrTalk(    #69
        0x102,
        (
            "#1040F#6PThat worked well for the moment.\x02\x03",

            "Unless we leave the ZFG here, though,\x01",
            "it won't fix the problem permanently.\x01",
            "And given our mission...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B67")

    TurnDirection(0x9, 0x0, 400)

    ChrTalk(    #70
        0x9,
        "We'd better hurry, then.\x02",
    )

    CloseMessageWindow()

    label("loc_1B8C")


    ChrTalk(    #71
        0x9,
        (
            "So if you want to modify your orbments,\x01",
            "now's your chance!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x52)
    OP_56(0x0)
    OP_0D()
    Sleep(30)

    ChrTalk(    #72
        0x9,
        (
            "Whenever you want to use the workshop,\x01",
            "just bring that device of yours along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "You'll be able to use our services like\x01",
            "normal if you do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    OP_A2(0x20E2)
    EventEnd(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_1C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1D73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D3E")

    ChrTalk(    #74
        0x9,
        (
            "I don't care how many people yell at me,\x01",
            "I can't fix any of these!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x9,
        (
            "I mean, none of the orbments are actually\x01",
            "BROKEN!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        "How many times have I explained this?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1D70")

    label("loc_1D3E")


    ChrTalk(    #77
        0x9,
        (
            "It's like I said!\x01",
            "Your orbment isn't broken!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D70")

    Jump("loc_2535")

    label("loc_1D73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1EC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E3C")

    ChrTalk(    #78
        0x9,
        (
            "It's been wall-to-wall customers since this\x01",
            "morning, begging for repairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "And they refuse to leave, even when\x01",
            "I explain nothing is damaged!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        "Oh, Aidios, save me now!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1EBE")

    label("loc_1E3C")


    ChrTalk(    #81
        0x9,
        (
            "These customers asking for repairs are\x01",
            "crazy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "I keep telling them there's nothing we\x01",
            "can do, and they just keep coming!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EBE")

    Jump("loc_2535")

    label("loc_1EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2015")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1F43")

    ChrTalk(    #83
        0x9,
        (
            "It seems the market building is back to\x01",
            "normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x9,
        (
            "I'm glad. It just isn't Bose if the market\x01",
            "isn't open!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2012")

    label("loc_1F43")


    ChrTalk(    #85
        0x9,
        "Hey, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x9,
        (
            "Did you see the market building?\x01",
            "It's back to how it used to be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x9,
        (
            "It's such a good thing.\x01",
            "That place is the symbol of Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        "The whole city lit up the moment it re-opened.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2012")

    Jump("loc_2535")

    label("loc_2015")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_21DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_20A2")

    ChrTalk(    #89
        0x9,
        (
            "My market days were definitely the\x01",
            "most fun I've ever had in business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        "Hope I can recapture that feeling someday.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21DB")

    label("loc_20A2")


    ChrTalk(    #91
        0x9,
        (
            "I just donated a bit to the market\x01",
            "repair fund.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x9,
        "After all, I used to work there too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        (
            "And, honestly, thinking about it?\x01",
            "My time in the market was the funnest\x01",
            "of my life, if nothing else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x9,
        (
            "Nigel and I worked our butts off,\x01",
            "chasing our dreams.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        "Haha! If I could, I'd go back to those days.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_21DB")

    Jump("loc_2535")

    label("loc_21DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2263")

    ChrTalk(    #96
        0x9,
        "So dragons really do exist.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x9,
        (
            "I remember hearing tales about them in bars\x01",
            "and whatnot, but who ever believed them?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2535")

    label("loc_2263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_22FF")

    ChrTalk(    #98
        0x9,
        "Something's happened to the market!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        (
            "Something about a big monster,\x01",
            "or something, and everyone was\x01",
            "losing it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x9,
        "I wonder what it was.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2535")

    label("loc_22FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2535")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_23CB")

    ChrTalk(    #101
        0x9,
        (
            "Nigel, the man who stole the factory\x01",
            "from me at one point, is still in jail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "I actually still keep in touch with him.\x01",
            "He was a friend once.\x01",
            "And prison sounds like hell for him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2535")

    label("loc_23CB")


    ChrTalk(    #103
        0x9,
        (
            "Nigel, the man who stole the factory\x01",
            "from me at one point, is still in jail.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x9,
        (
            "And honestly? I keep in touch with him.\x01",
            "He was a friend once.\x01",
            "And prison sounds like hell for him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "Still, though, the shop's been healthy\x01",
            "and, if I may say so, well run ever since\x01",
            "I got it back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x9,
        (
            "So kick back, relax, and let me know\x01",
            "if there's anything you need.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2535")

    TalkEnd(0x9)
    Return()

    # Function_6_1020 end

    def Function_7_2539(): pass

    label("Function_7_2539")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_26D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_263B")

    ChrTalk(    #107
        0xFE,
        "Boy, are our customers are persistent!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "I guess laymen, who don't really understand\x01",
            "how orbments work, not getting the problem\x01",
            "is to be expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "Trying to explain it, over and over,\x01",
            "is Corn's job. I feel sorry for him.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_26D6")

    label("loc_263B")


    ChrTalk(    #110
        0xFE,
        "Boy, are our customers are persistent!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "I guess laymen, who don't really understand\x01",
            "how orbments work, not getting the problem\x01",
            "is to be expected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D6")

    Jump("loc_306C")

    label("loc_26D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_282D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D3")

    ChrTalk(    #112
        0xFE,
        (
            "Customers have been pouring in since early\x01",
            "this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "Dealing with them is really Corn's job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "My only job is to keep at my work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "Even with orbments not functioning,\x01",
            "I still have a mountain of things to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_282A")

    label("loc_27D3")


    ChrTalk(    #116
        0xFE,
        (
            "Dealing with the customers is Corn's\x01",
            "job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "My only job is to keep at my work.\x02",
    )

    CloseMessageWindow()

    label("loc_282A")

    Jump("loc_306C")

    label("loc_282D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2ACB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2902")

    ChrTalk(    #118
        0xFE,
        (
            "I heard that an unbelievably pristine\x01",
            "goldia crystal was delivered to the\x01",
            "mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "It was apparently a gift...but a crystal\x01",
            "of that quality is more like a gift for a\x01",
            "monarch than a mayor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AC8")

    label("loc_2902")


    ChrTalk(    #120
        0xFE,
        (
            "I heard that an unbelievably pristine\x01",
            "goldia crystal was delivered to the\x01",
            "mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "It was apparently a gift...but a crystal\x01",
            "of that quality is more like a gift for a\x01",
            "monarch than a mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "It'll probably come to that either way.\x01",
            "That's not exactly something Mayor Maybelle\x01",
            "can just walk in here to trade mira for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Most likely they'll have to send it to\x01",
            "Grancel to be stored in the royal treasury,\x01",
            "accompanied by half the Royal Guard.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2AC8")

    Jump("loc_306C")

    label("loc_2ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2C85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2B79")

    ChrTalk(    #124
        0xFE,
        (
            "One of our regulars was going to come and\x01",
            "get an advance look at our newest wares.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "But with the flights canceled, his visit's\x01",
            "been delayed a week.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C82")

    label("loc_2B79")


    ChrTalk(    #126
        0xFE,
        (
            "One of our regulars was going to come and\x01",
            "get an advance look at our newest wares.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "But with the flights canceled, his visit's\x01",
            "been delayed a week.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "I was really looking forward to having a\x01",
            "critical eye take a look at my work.\x01",
            "It's too bad, really.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2C82")

    Jump("loc_306C")

    label("loc_2C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2E55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2D20")

    ChrTalk(    #129
        0xFE,
        (
            "Mmm, if I had the chance, I'd love to\x01",
            "see that dragon with my own eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "I bet it'd make a great motif for some\x01",
            "orbment designs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E52")

    label("loc_2D20")


    ChrTalk(    #131
        0xFE,
        (
            "That whole mess the other day...\x01",
            "Apparently it really was a dragon causing\x01",
            "all of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "The mythical Harbingers of Aidios,\x01",
            "said to have lived before the Great Collapse...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "Mmm, if I had the chance, I'd love to see\x01",
            "one for myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "I bet it'd make a great motif for some\x01",
            "orbment designs.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2E52")

    Jump("loc_306C")

    label("loc_2E55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2EB0")

    ChrTalk(    #135
        0xFE,
        "Things sound mad outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "I'm just going to focus on work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_306C")

    label("loc_2EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_306C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2F55")

    ChrTalk(    #138
        0xFE,
        (
            "The current owner, Cornelius, actually founded\x01",
            "this orbal workshop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "The previous owner got arrested, so\x01",
            "now old Corn is back in business.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_306C")

    label("loc_2F55")


    ChrTalk(    #140
        0xFE,
        (
            "The current owner, Cornelius, actually founded\x01",
            "this orbal workshop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "It had a different owner for a while, but he\x01",
            "was actually arrested recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "So Cornelius once again owns his factory.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "I never really heard the details, but it\x01",
            "was apparently a huge mess.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_306C")

    TalkEnd(0xA)
    Return()

    # Function_7_2539 end

    def Function_8_3070(): pass

    label("Function_8_3070")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_307D")
    OP_A2(0x4)

    label("loc_307D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_311A")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as met Sting in the previous game\x01",               # 0
            "Set as did not meet Sting in the previous game\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_310E"),
        (1, "loc_3114"),
        (SWITCH_DEFAULT, "loc_311A"),
    )


    label("loc_310E")

    OP_A2(0x4)
    Jump("loc_311A")

    label("loc_3114")

    OP_A3(0x4)
    Jump("loc_311A")

    label("loc_311A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3895")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_END)), "loc_326C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_320F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3194")

    ChrTalk(    #144
        0xFE,
        "I'll take care of all the small stuff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "It's on you to take care of that dragon.\x02",
    )

    CloseMessageWindow()
    Jump("loc_320C")

    label("loc_3194")


    ChrTalk(    #146
        0xFE,
        (
            "From the sound of it, you led the rescue\x01",
            "effort at the Market the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "Thanks.\x01",
            "Sorry I wasn't there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_320C")

    Jump("loc_3269")

    label("loc_320F")


    ChrTalk(    #148
        0xFE,
        "I'll take care of all the small stuff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "It's on you to take care of that dragon.\x02",
    )

    CloseMessageWindow()

    label("loc_3269")

    Jump("loc_3895")

    label("loc_326C")


    ChrTalk(    #150
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_351A")

    ChrTalk(    #151
        0x101,
        (
            "#1011FOh, hey, you're, um...\x02\x03",

            "Sting! Right? With the Bose branch.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #152
        0xFE,
        "You're that junior from a month or two ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "You've been promoted since then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#1016FYep! Managed it somehow.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3459")

    ChrTalk(    #155
        0x103,
        "#027FAs cool as ever, Sting.\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #156
        0xFE,
        "Scherazard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "From the sound of it, you led the rescue\x01",
            "effort at the market the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "Thanks.\x01",
            "Sorry I wasn't there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x103,
        "#026FNo, it's really just part of the job.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3517")

    label("loc_3459")


    ChrTalk(    #160
        0xFE,
        (
            "From the sound of it, you led the rescue\x01",
            "effort at the market the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "Thanks.\x01",
            "Sorry I wasn't there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        (
            "#1002FNah, it was the only thing to do in that\x01",
            "situation, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3517")

    Jump("loc_3835")

    label("loc_351A")


    ChrTalk(    #163
        0x101,
        (
            "#1015F(Huh? Hey.)\x02\x03",

            "(Now that I look, doesn't this guy have\x01",
            "a guild emblem?)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3689")

    ChrTalk(    #164
        0x103,
        (
            "#027FHello, Sting.\x01",
            "It's been quite a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #165
        0xFE,
        "Scherazard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "From the sound of it, you led the rescue\x01",
            "effort at the market the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "Thanks.\x01",
            "Sorry I wasn't there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x103,
        "#026FNo, it's really just part of the job.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3835")

    label("loc_3689")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36C4")

    ChrTalk(    #169
        0x108,
        "#070F(I think he's a senior bracer.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_36FE")

    label("loc_36C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36FE")

    ChrTalk(    #170
        0x104,
        "#030F(I believe he's a senior bracer.)\x02",
    )

    CloseMessageWindow()

    label("loc_36FE")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #171
        0xFE,
        "Hmm. You.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        "You're that new senior Lugran mentioned.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        "#1011FAh, yeah, that's probably me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "From the sound of it, you led the rescue\x01",
            "effort at the market the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "Thanks.\x01",
            "Sorry I wasn't there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1002FNah, it was the only thing to do in that\x01",
            "situation, you know?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3835")


    ChrTalk(    #178
        0xFE,
        "I'll take care of all the small stuff.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "It's on you to take care of that dragon.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A53)
    OP_A2(0x5)

    label("loc_3895")

    TalkEnd(0xB)
    Return()

    # Function_8_3070 end

    def Function_9_3899(): pass

    label("Function_9_3899")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3986")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3950")

    ChrTalk(    #180
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "I'm getting tired and I'M the one asking\x01",
            "questions!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "I've been here since this morning,\x01",
            "after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "It gets exhausting after a while!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_3983")

    label("loc_3950")


    ChrTalk(    #184
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        "I'm starting to get tired myself!\x02",
    )

    CloseMessageWindow()

    label("loc_3983")

    Jump("loc_3A65")

    label("loc_3986")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A1D")

    ChrTalk(    #186
        0xFE,
        (
            "You can't repair it?\x01",
            "What's that supposed to mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "This is just some kind of trick to sell\x01",
            "me something new, isn't it?!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_3A65")

    label("loc_3A1D")


    ChrTalk(    #188
        0xFE,
        "HEY, OWNER!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "I am NOT MOVING until you fix my camera!\x01",
            "GET IT?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A65")

    TalkEnd(0xC)
    Return()

    # Function_9_3899 end

    def Function_10_3A69(): pass

    label("Function_10_3A69")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3B21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B0F")

    ChrTalk(    #190
        0xFE,
        (
            "Mrrrrrrgh, you explain and explain and\x01",
            "I just don't get it!\x01",
            "How can an orbment not work?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        "*yawn* Oh, it doesn't even really matter.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3B1E")

    label("loc_3B0F")


    ChrTalk(    #192
        0xFE,
        "*yawn*...\x02",
    )

    CloseMessageWindow()

    label("loc_3B1E")

    Jump("loc_3BF3")

    label("loc_3B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3BF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BA0")

    ChrTalk(    #193
        0xFE,
        "Enough talking. Hurry up and fix it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "I have FISHING to get to!\x01",
            "Stop yammering and do something!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3BF3")

    label("loc_3BA0")


    ChrTalk(    #195
        0xFE,
        "Oh just fix it already, you pansy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        "Do you want me to sic my wife on you?\x02",
    )

    CloseMessageWindow()

    label("loc_3BF3")

    TalkEnd(0xD)
    Return()

    # Function_10_3A69 end

    def Function_11_3BF7(): pass

    label("Function_11_3BF7")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C97")

    ChrTalk(    #197
        0xFE,
        (
            "Those two at the counter are being\x01",
            "completely unreasonable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        "I feel really bad for the store owner.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "Talk about a bed of needles!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_3D01")

    label("loc_3C97")


    ChrTalk(    #200
        0xFE,
        "I actually came in for repairs too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "I just can't bring myself to be\x01",
            "THAT worked up over it all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D01")

    TalkEnd(0xE)
    Return()

    # Function_11_3BF7 end

    def Function_12_3D05(): pass

    label("Function_12_3D05")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D12")
    Return()

    label("loc_3D12")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3D24")
    Return()

    label("loc_3D24")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x9)"), scpexpr(EXPR_END)), "loc_3D5F")
    Call(0, 13)
    Jump("loc_3E54")

    label("loc_3D5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x8)"), scpexpr(EXPR_END)), "loc_3D6E")
    Call(0, 14)
    Jump("loc_3E54")

    label("loc_3D6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E8)"), scpexpr(EXPR_END)), "loc_3D7D")
    Call(0, 13)
    Jump("loc_3E54")

    label("loc_3D7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0x3E9)"), scpexpr(EXPR_END)), "loc_3D8C")
    Call(0, 14)
    Jump("loc_3E54")

    label("loc_3D8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_3DFE")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #202
        "\x07\x05Tried showing them the photograph, but they didn't recognize her.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_3E54")

    label("loc_3DFE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #203
        "\x07\x05There's no one to show the photograph to nearby.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_3E54")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_12_3D05 end

    def Function_13_3E5B(): pass

    label("Function_13_3E5B")

    TalkBegin(0x9)

    ChrTalk(    #204
        0x9,
        (
            "A girl who got lost ten years ago during\x01",
            "the fighting? That's terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x9,
        (
            "I'm sorry, but I'm afraid none of my\x01",
            "regular customers look like her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x9,
        "You'll need to ask elsewhere.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_13_3E5B end

    def Function_14_3F1D(): pass

    label("Function_14_3F1D")

    TalkBegin(0x8)

    ChrTalk(    #207
        0x8,
        "Mm. No, I don't recognize her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x8,
        (
            "We don't exactly get a lot of women in here,\x01",
            "if you take my meaning, so I'd remember her.\x01",
            "Uh, begging your pardon, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x8,
        (
            "And even accounting for ten years,\x01",
            "I think I'd recognize her.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_14_3F1D end

    SaveToFile()

Try(main)
