from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0610   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0610.x',
        MapIndex            = 17,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0610_1 ._SN',
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
        'CWO Robin',                            # 9
        'Warrant Officer Graves',               # 10
        'Private Anden',                        # 11
        'Sam',                                  # 12
        'Emily',                                # 13
        'Percy',                                # 14
        'Ridge',                                # 15
        'Traveler',                             # 16
        'Traveler',                             # 17
        'Traveler',                             # 18
        'Traveler',                             # 19
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01310 ._CH',             # 01
        'ED6_DT07/CH01300 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
        'ED6_DT26/CH20237 ._CH',             # 05
        'ED6_DT07/CH01460 ._CH',             # 06
        'ED6_DT07/CH01760 ._CH',             # 07
        'ED6_DT07/CH01200 ._CH',             # 08
        'ED6_DT07/CH01233 ._CH',             # 09
        'ED6_DT07/CH01020 ._CH',             # 0A
        'ED6_DT07/CH01220 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01310P._CP',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
        'ED6_DT26/CH20237P._CP',             # 05
        'ED6_DT07/CH01460P._CP',             # 06
        'ED6_DT07/CH01760P._CP',             # 07
        'ED6_DT07/CH01200P._CP',             # 08
        'ED6_DT07/CH01233P._CP',             # 09
        'ED6_DT07/CH01020P._CP',             # 0A
        'ED6_DT07/CH01220P._CP',             # 0B
    )

    DeclNpc(
        X                   = -19380,
        Z                   = 0,
        Y                   = -980,
        Direction           = 98,
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
        X                   = -111940,
        Z                   = 0,
        Y                   = 21850,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -7220,
        Z                   = 0,
        Y                   = 2820,
        Direction           = 162,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -90130,
        Z                   = 0,
        Y                   = -22320,
        Direction           = 253,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -57740,
        Z                   = 0,
        Y                   = -21510,
        Direction           = 352,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -63920,
        Z                   = 0,
        Y                   = -22680,
        Direction           = 250,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -5350,
        Z                   = 0,
        Y                   = 880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -60600,
        Z                   = 0,
        Y                   = -27550,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -59280,
        Z                   = 100,
        Y                   = -26820,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -94140,
        Z                   = 0,
        Y                   = -28140,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -95590,
        Z                   = 0,
        Y                   = -25980,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )


    DeclActor(
        TriggerX            = -7430,
        TriggerZ            = 0,
        TriggerY            = 900,
        TriggerRange        = 1000,
        ActorX              = -7220,
        ActorZ              = 1500,
        ActorY              = 2820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -109840,
        TriggerZ            = 0,
        TriggerY            = 21450,
        TriggerRange        = 1000,
        ActorX              = -111940,
        ActorZ              = 1500,
        ActorY              = 21850,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -92220,
        TriggerZ            = 0,
        TriggerY            = -22040,
        TriggerRange        = 1000,
        ActorX              = -90130,
        ActorZ              = 1500,
        ActorY              = -22320,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2D6",          # 00, 0
        "Function_1_3DA",          # 01, 1
        "Function_2_442",          # 02, 2
        "Function_3_466",          # 03, 3
        "Function_4_46B",          # 04, 4
        "Function_5_470",          # 05, 5
        "Function_6_475",          # 06, 6
        "Function_7_1241",         # 07, 7
        "Function_8_1C61",         # 08, 8
        "Function_9_26C7",         # 09, 9
        "Function_10_317C",        # 0A, 10
        "Function_11_3F57",        # 0B, 11
        "Function_12_4002",        # 0C, 12
        "Function_13_45D0",        # 0D, 13
        "Function_14_467B",        # 0E, 14
        "Function_15_4723",        # 0F, 15
        "Function_16_477F",        # 10, 16
        "Function_17_4814",        # 11, 17
        "Function_18_48B7",        # 12, 18
        "Function_19_5671",        # 13, 19
        "Function_20_56CD",        # 14, 20
        "Function_21_5729",        # 15, 21
        "Function_22_5DC8",        # 16, 22
        "Function_23_64A0",        # 17, 23
    )


    def Function_0_2D6(): pass

    label("Function_0_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2F2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 18)

    label("loc_2F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_319")
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x8, -52400, 0, 23230, 0)
    OP_43(0x8, 0x0, 0x6, 0x2)
    Jump("loc_3D9")

    label("loc_319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x300, 6)), scpexpr(EXPR_END)), "loc_360")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_338")
    ClearChrFlags(0xD, 0x80)

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35D")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    label("loc_35D")

    Jump("loc_3D9")

    label("loc_360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_36A")
    Jump("loc_3D9")

    label("loc_36A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_37D")
    SetChrFlags(0x9, 0x80)
    OP_64(0x1, 0x1)
    Jump("loc_3D9")

    label("loc_37D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_3BE")
    SetChrPos(0x8, -19540, 0, 1620, 109)
    SetChrFlags(0x8, 0x10)
    OP_43(0x8, 0x0, 0x6, 0x2)
    SetChrPos(0x9, -17890, 0, 1620, 271)
    SetChrFlags(0x9, 0x10)
    OP_64(0x1, 0x1)
    Jump("loc_3D9")

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_3C8")
    Jump("loc_3D9")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3D2")
    Jump("loc_3D9")

    label("loc_3D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3D9")

    label("loc_3D9")

    Return()

    # Function_0_2D6 end

    def Function_1_3DA(): pass

    label("Function_1_3DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F2")
    OP_B1("t0610_y")
    Jump("loc_3FB")

    label("loc_3F2")

    OP_B1("t0610_n")

    label("loc_3FB")

    OP_1C(0x5, 0x0, 0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_414")
    OP_1B(0x0, 0x0, 0x15)
    Jump("loc_425")

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_425")
    OP_1B(0x1, 0x0, 0x16)

    label("loc_425")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_441")
    OP_6F(0x5, 100)
    OP_72(0x5, 0x10)
    OP_64(0x1, 0x1)

    label("loc_441")

    Return()

    # Function_1_3DA end

    def Function_2_442(): pass

    label("Function_2_442")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_465")
    OP_8D(0xFE, -22660, -4810, -14730, 1940, 3000)
    Jump("Function_2_442")

    label("loc_465")

    Return()

    # Function_2_442 end

    def Function_3_466(): pass

    label("Function_3_466")

    Call(0, 9)
    Return()

    # Function_3_466 end

    def Function_4_46B(): pass

    label("Function_4_46B")

    Call(0, 7)
    Return()

    # Function_4_46B end

    def Function_5_470(): pass

    label("Function_5_470")

    Call(0, 8)
    Return()

    # Function_5_470 end

    def Function_6_475(): pass

    label("Function_6_475")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_5CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54A")

    ChrTalk(    #0
        0xFE,
        (
            "Not just here, but all across the nation \x01",
            "we're on high alert status.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "If there's any exception, it'd\x01",
            "be the Wolf Fort, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Well, they take things at their own pace there.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5C8")

    label("loc_54A")


    ChrTalk(    #3
        0xFE,
        (
            "All military bases in the kingdom\x01",
            "are on high alert status.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "If there's any exception, it'd\x01",
            "be the Wolf Fort, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C8")

    Jump("loc_123D")

    label("loc_5CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_830")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_730")

    ChrTalk(    #5
        0xFE,
        (
            "Oh, you're the bracers, yes?\x01",
            "Very good work you've been doing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "We've restored our communications device\x01",
            "with that generator we were provided with,\x01",
            "but the situation remains pretty bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "For now, we've got plenty of supplies, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "We need to prepare a plan sooner rather\x01",
            "than later, in case the situation drags out.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_82D")

    label("loc_730")


    ChrTalk(    #9
        0xFE,
        (
            "Currently, in accordance with high alert\x01",
            "regulations we've upped our scrutiny of\x01",
            "persons passing through, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "By order of high command, bracers\x01",
            "are permitted to pass freely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Of course, that also means we're\x01",
            "expecting you to work hard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82D")

    Jump("loc_123D")

    label("loc_830")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_9BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8D4")

    ChrTalk(    #12
        0xFE,
        (
            "The non-aggression pact has been signed,\x01",
            "and the fog over Rolent finally cleared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I'm relieved, but I'm sure Mr. Ashton\x01",
            "is even more so.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BA")

    label("loc_8D4")


    ChrTalk(    #14
        0xFE,
        (
            "The non-aggression pact has been signed,\x01",
            "and the fog over Rolent finally cleared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "This morning's sunrise blew away both\x01",
            "of my great worries together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Now I can return to my daily\x01",
            "duties without any distractions.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_9BA")

    Jump("loc_123D")

    label("loc_9BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_B70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A6F")

    ChrTalk(    #17
        0xFE,
        (
            "The most effective medicine for making\x01",
            "people grow is responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Hopefully the new troops at Verte Bridge\x01",
            "will mature having overcome this trial.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B6D")

    label("loc_A6F")


    ChrTalk(    #19
        0xFE,
        (
            "Right, Mr. Ashton was worried about\x01",
            "the training of some new troops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "The most effective medicine for making\x01",
            "people grow is responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Hopefully they'll gain a lot of valuable\x01",
            "experience through this mission to\x01",
            "guard Rolent, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B6D")

    Jump("loc_123D")

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_D2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C01")

    ChrTalk(    #22
        0xFE,
        (
            "The Verte Bridge squad should arrive\x01",
            "in Rolent soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "There shouldn't be any problems if\x01",
            "we leave it to them, I think.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D28")

    label("loc_C01")


    ChrTalk(    #24
        0xFE,
        (
            "Apparently there are some worrisome\x01",
            "events going on in the city of Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "The Royal Army has dispatched a squad\x01",
            "to ensure the safety of the townspeople.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "The Verte Bridge squad should arrive\x01",
            "in Rolent soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "There shouldn't be any problems if\x01",
            "we leave it to them, I think.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D28")

    Jump("loc_123D")

    label("loc_D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_END)), "loc_DEB")

    ChrTalk(    #28
        0xFE,
        "The fog around Rolent might be quite serious...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "It's possible the fog might blow all\x01",
            "the way over here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "We might need to add some troops\x01",
            "to the guard schedule.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E67")

    label("loc_DEB")


    ChrTalk(    #31
        0xFE,
        "I hear the airliner Cecilia is stuck in Rolent.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "I've never experienced a fog so bad\x01",
            "that airships can't take off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E67")

    Jump("loc_123D")

    label("loc_E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_F49")

    ChrTalk(    #33
        0xFE,
        (
            "Some of the troops saw that giant\x01",
            "orbal construct fly off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "I hear it took off towards the\x01",
            "center of the lake, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Apparently even the pride of the Royal Army,\x01",
            "the patrol ships, couldn't find it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123D")

    label("loc_F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_1025")

    ChrTalk(    #36
        0xFE,
        "The society... Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "To suddenly attack the royal villa the guard\x01",
            "forces were using as a headquarters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I don't know what kind of organization they\x01",
            "are, but we should be prepared for anything.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123D")

    label("loc_1025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_1083")

    ChrTalk(    #39
        0xFE,
        (
            "...That is all. Please hurry organizing\x01",
            "the forces to patrol the scenic route.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123D")

    label("loc_1083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1162")

    ChrTalk(    #40
        0xFE,
        (
            "An order's come down for all forces stationed\x01",
            "in Grancel to strengthen patrols.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Ideally, the signing ceremony will conclude\x01",
            "without any issues, but it's our job to prepare\x01",
            "for the unexpected, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_123D")

    label("loc_1162")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_11C7")

    ChrTalk(    #42
        0xFE,
        (
            "Good afternoon. You're free to view anywhere\x01",
            "in this gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Enjoy your time here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_123D")

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_123D")

    ChrTalk(    #44
        0xFE,
        "Hey, hello.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "If you intend to head to Rolent, please go\x01",
            "through the inspection area at the reception.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123D")

    TalkEnd(0x8)
    Return()

    # Function_6_475 end

    def Function_7_1241(): pass

    label("Function_7_1241")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1418")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_12FD")

    ChrTalk(    #46
        0x9,
        (
            "Apparently the airship that was grounded\x01",
            "in Rolent is back in service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "This should help make sure all the attendees\x01",
            "to the signing ceremony get home on time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1415")

    label("loc_12FD")


    ChrTalk(    #48
        0x9,
        (
            "Apparently the airship that was grounded\x01",
            "in Rolent is back in service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "This should help make sure all the attendees\x01",
            "to the signing ceremony get home on time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "Gotta admit, I was breaking out in\x01",
            "a cold sweat over the whole thing,\x01",
            "but thankfully it all ended okay.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1415")

    Jump("loc_1C5D")

    label("loc_1418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_15B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_14C3")

    ChrTalk(    #51
        0x9,
        (
            "Verte Bridge is actually a pretty nice\x01",
            "fishing spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "Most people don't even know about it.\x01",
            "It's a secret spot for hardcore fishers.\x01",
            "*wink wink*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15B5")

    label("loc_14C3")


    ChrTalk(    #53
        0x9,
        (
            "Apparently the guard force at Verte Bridge\x01",
            "has started patrolling Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        "Hmm... Verte Bridge, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        "...That place is actually a good fishing spot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "I wonder if they'd let me join their\x01",
            "supplemental squad if I applied.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_15B5")

    Jump("loc_1C5D")

    label("loc_15B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_172E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_165F")

    ChrTalk(    #57
        0x9,
        (
            "Lately I've just been so busy.\x01",
            "I haven't had much time to fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        (
            "Once the signing ceremony ends I'd\x01",
            "like some time to relax and wet my\x01",
            "line.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_172B")

    label("loc_165F")


    ChrTalk(    #59
        0x9,
        "The fog's just getting worse and worse.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "I'd been planning to secretly enjoy some\x01",
            "fishing after the signing ceremony, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x9,
        (
            "Hmm, can't exactly go to the nearby\x01",
            "fishing spot in this fog.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_172B")

    Jump("loc_1C5D")

    label("loc_172E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_186C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_END)), "loc_177C")

    ChrTalk(    #62
        0x9,
        (
            "Seems awfully loud outside, but...\x01",
            "Did someone come by?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1869")

    label("loc_177C")


    ChrTalk(    #63
        0x9,
        "Tomorrow's the signing ceremony, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        (
            "Feels almost like a dream, thinking\x01",
            "of the Hundred Days War.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "Well, putting that aside, the\x01",
            "problem now is this fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "Thankfully there's not many travelers\x01",
            "right now. That helps.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1869")

    Jump("loc_1C5D")

    label("loc_186C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1951")

    ChrTalk(    #67
        0x9,
        (
            "Apparently the training facility in Nebel\x01",
            "Valley was attacked by sky bandits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "It almost seems like they were taking\x01",
            "advantage of the going-ons in Grancel,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x9,
        "Well, I'm probably just over thinking it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_1951")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_198A")

    ChrTalk(    #70
        0x9,
        "...Understood. I'll dispatch immediately.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_198A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_1AA0")

    ChrTalk(    #71
        0x9,
        (
            "I've got information that the remnants of\x01",
            "the Intelligence Division are in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        (
            "It's possible that they intend to disrupt\x01",
            "the signing ceremony, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "One way or another, our priority\x01",
            "is to protect this location.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        "We need to focus on that mission.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_1AA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1BBA")

    ChrTalk(    #75
        0x9,
        (
            "I hear that the Imperial and Republican\x01",
            "ambassadors get along like dogs\x01",
            "and cats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "Makes sense, given that their countries\x01",
            "are like water and oil to begin with, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        (
            "I wonder if two nations like that will really\x01",
            "be able to hold to a non-aggression pact...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5D")

    label("loc_1BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1C5D")

    ChrTalk(    #78
        0x9,
        "Hmm? Do you have some business here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        "I'm in the middle of drafting up a patrol plan.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "It is, after all, almost time for the\x01",
            "signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5D")

    TalkEnd(0x9)
    Return()

    # Function_7_1241 end

    def Function_8_1C61(): pass

    label("Function_8_1C61")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1DC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D52")

    ChrTalk(    #81
        0xA,
        (
            "The subject people bring up at every\x01",
            "meal is that darn floating island...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "We still don't have the slightest clue\x01",
            "what it is. Talk about creepy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "It's just floating there, but\x01",
            "that makes it creepier...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1DC1")

    label("loc_1D52")


    ChrTalk(    #84
        0xA,
        "Apparently we still don't know what it is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xA,
        (
            "It's just floating there, but\x01",
            "that makes it creepier...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC1")

    Jump("loc_26C3")

    label("loc_1DC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1F55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED4")

    ChrTalk(    #86
        0xA,
        (
            "I was shocked at that fog we had a while ago,\x01",
            "but I suppose it can always get worse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "To have orbments stop working like this...\x01",
            "Why did this happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xA,
        "Thanks to that, breakfast sure was sad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        "Mealtime is one of our few joys, too...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1F52")

    label("loc_1ED4")


    ChrTalk(    #90
        0xA,
        (
            "Emily over in the dining hall's having trouble\x01",
            "since she can't use her stove.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        "Meals are one of our few joys, too...\x02",
    )

    CloseMessageWindow()

    label("loc_1F52")

    Jump("loc_26C3")

    label("loc_1F55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_201E")

    ChrTalk(    #92
        0xA,
        (
            "I wonder if this non-aggression pact will\x01",
            "encourage more travelers from foreign\x01",
            "nations to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        (
            "I'd better brush up on my diplomatic skills\x01",
            "so I don't shame Liberl when they come.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C3")

    label("loc_201E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_20B1")

    ChrTalk(    #94
        0xA,
        (
            "I wonder if that traveling priest\x01",
            "reached Rolent safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xA,
        (
            "To go to Rolent at a time like this...\x01",
            "Maaan, talk about having guts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C3")

    label("loc_20B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2162")

    ChrTalk(    #96
        0xA,
        (
            "I-It kinda seems like the fog is just\x01",
            "getting thicker and thicker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        (
            "Today's the day of the signing ceremony.\x01",
            "I reeeally don't want anything to happen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2216")

    label("loc_2162")


    ChrTalk(    #98
        0xA,
        (
            "I-It kinda seems like the fog is just\x01",
            "getting thicker and thicker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        (
            "Today's the day of the important\x01",
            "signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        "Please, please don't let anything happen...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2216")

    Jump("loc_26C3")

    label("loc_2219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_230D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_END)), "loc_228D")

    ChrTalk(    #101
        0xA,
        (
            "Seems like the fog in Rolent's worse\x01",
            "than anyone expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        "The travelers were exhausted.\x02",
    )

    CloseMessageWindow()
    Jump("loc_230A")

    label("loc_228D")


    ChrTalk(    #103
        0xA,
        "It'll take a bit for any permits to be issued.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "Security's getting tighter in preparation\x01",
            "for the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_230A")

    Jump("loc_26C3")

    label("loc_230D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_23E5")

    ChrTalk(    #105
        0xA,
        (
            "At first, I heard the forces that appeared on\x01",
            "the scenic route were the society's men,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        (
            "Ultimately, it was just the remnants\x01",
            "of the Intelligence Division, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xA,
        "What was that all about?\x02",
    )

    CloseMessageWindow()
    Jump("loc_26C3")

    label("loc_23E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_2410")

    ChrTalk(    #108
        0xA,
        "Huh, where'd Mr. Graves go?\x02",
    )

    CloseMessageWindow()
    Jump("loc_26C3")

    label("loc_2410")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_2490")

    ChrTalk(    #109
        0xA,
        "Hey, come to see the evening view from the roof?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xA,
        (
            "It looks the best at this time of year,\x01",
            "so take your time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C3")

    label("loc_2490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_257D")

    ChrTalk(    #111
        0xA,
        (
            "Everyone's been talking about the Intelligence\x01",
            "Division's remnants from this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xA,
        (
            "I wonder what they're planning over\x01",
            "in Bose of all places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xA,
        (
            "Well, no matter what happens they're\x01",
            "not getting past Gurune Gate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26C3")

    label("loc_257D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2646")

    ChrTalk(    #114
        0xA,
        (
            "If you're going to take a look from\x01",
            "the roof of the fort, be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xA,
        (
            "I heard there was a tourist who almost\x01",
            "fell from the Sanktheim Gate walls.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xA,
        "Be careful you don't get hurt.\x02",
    )

    CloseMessageWindow()
    Jump("loc_26C3")

    label("loc_2646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_26C3")

    ChrTalk(    #117
        0xA,
        "Oh, heading to Rolent?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xA,
        (
            "If you're heading to Rolent, please\x01",
            "check in at the counter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xA,
        "...Oh, you're not?\x02",
    )

    CloseMessageWindow()

    label("loc_26C3")

    TalkEnd(0xA)
    Return()

    # Function_8_1C61 end

    def Function_9_26C7(): pass

    label("Function_9_26C7")

    TalkBegin(0xB)
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26E7")
    OP_0D()
    OP_A9(0xA)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_26E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26F8")
    TalkEnd(0xB)
    Return()

    label("loc_26F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_283B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27CA")

    ChrTalk(    #120
        0xB,
        (
            "Talk about a constant series of crises,\x01",
            "with this right after that fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xB,
        "Thanks to that we're being run ragged.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xB,
        (
            "Phew! I already can't wait for\x01",
            "the next birthday celebrations.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2838")

    label("loc_27CA")


    ChrTalk(    #123
        0xB,
        "Lately we've really been run ragged.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        (
            "Phew! I already can't wait for\x01",
            "the next birthday celebrations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2838")

    Jump("loc_3178")

    label("loc_283B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2906")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28B3")

    ChrTalk(    #125
        0xB,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xB,
        (
            "Traveling at a time like this,\x01",
            "maaan, must be rough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xB,
        "Well, rest well.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2903")

    label("loc_28B3")


    ChrTalk(    #128
        0xB,
        (
            "Traveling at a time like this,\x01",
            "maaan, must be rough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xB,
        "Well, rest well.\x02",
    )

    CloseMessageWindow()

    label("loc_2903")

    Jump("loc_3178")

    label("loc_2906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2A41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_298C")

    ChrTalk(    #130
        0xB,
        (
            "Today's our first bit of good weather\x01",
            "in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xB,
        (
            "The sheets here're gonna smell\x01",
            "like the sun for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A3E")

    label("loc_298C")


    ChrTalk(    #132
        0xB,
        (
            "Hey, today's our first bit of good weather\x01",
            "in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xB,
        (
            "The sheets here're gonna smell\x01",
            "like the sun for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xB,
        "Yeah, naturally dried sheets sure do feel good.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2A3E")

    Jump("loc_3178")

    label("loc_2A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2B93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2ACE")

    ChrTalk(    #135
        0xB,
        (
            "With the air so humid like this, the\x01",
            "sheets I washed aren't gonna dry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xB,
        "Maybe I should just toss them in the oven.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B90")

    label("loc_2ACE")


    ChrTalk(    #137
        0xB,
        (
            "With the air so humid like this, the\x01",
            "sheets I washed aren't gonna dry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xB,
        (
            "But on the flip side, if I don't change\x01",
            "them, they're gonna start getting moldy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xB,
        "Ahh, I miss blue skies.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2B90")

    Jump("loc_3178")

    label("loc_2B93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2CBC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2BFE")

    ChrTalk(    #140
        0xB,
        "You're free to choose any open bed right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xB,
        "If you'd like, go ahead and rest.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CB9")

    label("loc_2BFE")


    ChrTalk(    #142
        0xB,
        "Hey, you're free to choose any open bed right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xB,
        (
            "After all, today's the signing ceremony,\x01",
            "and on top of that, there's this fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xB,
        "Well, yeah, we won't have many guests.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2CB9")

    Jump("loc_3178")

    label("loc_2CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_2E22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_END)), "loc_2D31")

    ChrTalk(    #145
        0xB,
        "Is the fog that incredible?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xB,
        (
            "It's been lovely weather here at\x01",
            "Gurune Gate from morning on.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E1F")

    label("loc_2D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2DA2")

    ChrTalk(    #147
        0xB,
        (
            "We're a lodge for travelers.\x01",
            "Everyone's welcome here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xB,
        (
            "If you want to stay,\x01",
            "just let me know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E1F")

    label("loc_2DA2")


    ChrTalk(    #149
        0xB,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xB,
        (
            "We're a lodge for travelers.\x01",
            "Everyone's welcome here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xB,
        (
            "If you want to stay,\x01",
            "just let me know.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2E1F")

    Jump("loc_3178")

    label("loc_2E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2F12")

    ChrTalk(    #152
        0xB,
        "Lately, the soldiers seem really busy again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xB,
        (
            "I'm sure they're busy preparing for\x01",
            "the signing ceremony, too, but it\x01",
            "doesn't seem like it's just that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xB,
        (
            "I wonder if it has anything to do\x01",
            "with the events in the capital.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3178")

    label("loc_2F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_2F72")

    ChrTalk(    #155
        0xB,
        "Hey, you two. Gonna spend the night?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xB,
        "Unfortunately, we're full for tonight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3178")

    label("loc_2F72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_2FCB")

    ChrTalk(    #157
        0xB,
        "Hmm? You seem awfully worked up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xB,
        "Haha, late for a date or something?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3178")

    label("loc_2FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_306B")

    ChrTalk(    #159
        0xB,
        (
            "All right, the good weather today dried\x01",
            "the sheets even nicer than normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xB,
        (
            "If you want to enjoy the scent of the sun,\x01",
            "you should stay here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3178")

    label("loc_306B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3124")

    ChrTalk(    #161
        0xB,
        (
            "Right now, it seems like the Royal Army's\x01",
            "busy preparing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xB,
        (
            "After all, it'd be pretty sad if those\x01",
            "Intelligence Division types got in\x01",
            "the way of the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3178")

    label("loc_3124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3178")

    ChrTalk(    #163
        0xB,
        "Hey, this is the Gurune Gate Lodge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xB,
        "If you'd like, stay the night.\x02",
    )

    CloseMessageWindow()

    label("loc_3178")

    TalkEnd(0xB)
    Return()

    # Function_9_26C7 end

    def Function_10_317C(): pass

    label("Function_10_317C")

    TalkBegin(0xC)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_319C")
    OP_0D()
    OP_A9(0xB)
    OP_56(0x0)
    TalkEnd(0xC)
    Return()

    label("loc_319C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31AD")
    TalkEnd(0xC)
    Return()

    label("loc_31AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_337B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32DF")

    ChrTalk(    #165
        0xFE,
        "I'm trying to plan tomorrow's menu, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "If I can't use my oven, then maybe\x01",
            "I should make it all cold meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "A cold soup, a salad, and a carpaccio.\x01",
            "How's that sound?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "It'll kind of end up as an appetizer selection,\x01",
            "but that's kind of stylish, so it's okay, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_3378")

    label("loc_32DF")


    ChrTalk(    #169
        0xFE,
        (
            "If I can't use my oven, then maybe\x01",
            "I should make it all cold meals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "The problem might end up being getting\x01",
            "enough to fill everyone's stomachs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3378")

    Jump("loc_3F53")

    label("loc_337B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3500")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_348F")

    ChrTalk(    #171
        0xFE,
        "*siiigh* Today's been rough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "I can't make anything other than simple,\x01",
            "random stuff without my oven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "The soldiers here are all really nice,\x01",
            "so they say it's great, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Knowing they're having to put on\x01",
            "a face makes it all the harder.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_34FD")

    label("loc_348F")


    ChrTalk(    #175
        0xFE,
        "*siiigh* Today's been rough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "I can't make anything other than simple,\x01",
            "random stuff without my oven.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34FD")

    Jump("loc_3F53")

    label("loc_3500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_3637")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_357E")

    ChrTalk(    #177
        0xFE,
        (
            "The soldiers' expressions are brighter\x01",
            "than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "I bet mealtime's gonna be cheerier from today.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3634")

    label("loc_357E")


    ChrTalk(    #179
        0xFE,
        (
            "The soldiers' expressions are brighter\x01",
            "than before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "I bet mealtime's gonna be cheerier from today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "Guess I'd better work extra\x01",
            "hard too and make the meals special.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3634")

    Jump("loc_3F53")

    label("loc_3637")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_3879")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_36DF")

    ChrTalk(    #182
        0xFE,
        "Today's lunch will be fish, Ruan-style.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "It's a dish I'm quite proud of. It's a special\x01",
            "arrangement based on some Eastern\x01",
            "cooking techniques.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3876")

    label("loc_36DF")


    ChrTalk(    #184
        0xFE,
        "Today's lunch will be fish, Ruan-style.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "Scented with some special herbs\x01",
            "and cooked in a steamer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "It's a dish I'm quite proud of. It's a special\x01",
            "arrangement based on some Eastern\x01",
            "cooking techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "Guarding the signing ceremony, and\x01",
            "dealing with this whole fog mess...\x01",
            "It must be hard on the soldiers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "I want to do my best so they can at least\x01",
            "enjoy themselves during meal time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3876")

    Jump("loc_3F53")

    label("loc_3879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_3946")

    ChrTalk(    #189
        0xFE,
        "I've learned a lot from Eastern cooking methods.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "If you're clever, you can incorporate those\x01",
            "techniques with Liberlian recipes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "Can't just imitate.\x01",
            "You gotta steal the good parts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F53")

    label("loc_3946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_3BA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 1)), scpexpr(EXPR_END)), "loc_39D2")

    ChrTalk(    #192
        0xFE,
        (
            "It seems like our guests had quite\x01",
            "the tough time reaching here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        "I'd better make sure they get a wonderful meal.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BA3")

    label("loc_39D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3A6D")

    ChrTalk(    #194
        0xFE,
        (
            "Recently, I picked up a cookbook and have\x01",
            "been studying Eastern techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "There's no way to expand your\x01",
            "repertoire except challenge!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA3")

    label("loc_3A6D")


    ChrTalk(    #196
        0xFE,
        (
            "Recently, I picked up a cookbook and have\x01",
            "been studying Eastern techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "The hardest part is that they\x01",
            "use different spices.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "I'm trying to look for similar things\x01",
            "I can substitute from here, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "No matter what I try, all the guests who come\x01",
            "from the East say it's not quite right.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3BA3")

    Jump("loc_3F53")

    label("loc_3BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3D40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CBC")

    ChrTalk(    #200
        0xFE,
        (
            "Lately, I haven't been satisfied with\x01",
            "my own cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "I think the biggest reason is I've\x01",
            "been getting stuck in a rut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "Until now I've tried various different\x01",
            "recipes from time to time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "Maybe I should give some new\x01",
            "techniques a go.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_3D3D")

    label("loc_3CBC")


    ChrTalk(    #204
        0xFE,
        (
            "Until now I've tried various different\x01",
            "recipes from time to time, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "Maybe I should give some new\x01",
            "techniques a go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D3D")

    Jump("loc_3F53")

    label("loc_3D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_3D82")

    ChrTalk(    #206
        0xFE,
        (
            "Mr. Graves went running off.\x01",
            "Did something happen?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F53")

    label("loc_3D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_END)), "loc_3E22")

    ChrTalk(    #207
        0xFE,
        (
            "Mr. Robin and Mr. Graves were talking\x01",
            "and they both had really serious faces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        (
            "I wonder if something happened.\x01",
            "Even I'm getting nervous now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F53")

    label("loc_3E22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_3E95")

    ChrTalk(    #209
        0xFE,
        "Hmm, I'm getting tired of this flavor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "It's not selling that well with\x01",
            "the soldiers, either...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F53")

    label("loc_3E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_3F16")
    TurnDirection(0xFE, 0x12F, 400)

    ChrTalk(    #211
        0xFE,
        (
            "Oh, why, miss, what a lovely white dress.\x01",
            "It looks wonderful on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        "If you'd like, have a meal here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F53")

    label("loc_3F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3F53")

    ChrTalk(    #213
        0xFE,
        (
            "Welcome! Welcome to the Gurune\x01",
            "Gate dining hall!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F53")

    TalkEnd(0xC)
    Return()

    # Function_10_317C end

    def Function_11_3F57(): pass

    label("Function_11_3F57")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_3FD7")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Talk\x01",        # 0
            "Report\x01",      # 1
            "Leave\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FC0")
    Call(0, 12)
    Jump("loc_3FD4")

    label("loc_3FC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FD4")
    Call(1, 3)
    Jump("loc_3FD4")

    label("loc_3FD4")

    Jump("loc_3FFE")

    label("loc_3FD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3FFA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_3FF3")
    Call(1, 1)
    Jump("loc_3FF7")

    label("loc_3FF3")

    Call(1, 0)

    label("loc_3FF7")

    Jump("loc_3FFE")

    label("loc_3FFA")

    Call(0, 12)

    label("loc_3FFE")

    TalkEnd(0xD)
    Return()

    # Function_11_3F57 end

    def Function_12_4002(): pass

    label("Function_12_4002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4054")

    ChrTalk(    #214
        0xFE,
        "Well, then, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "Be sure there're no accidents.\x02",
    )

    CloseMessageWindow()
    Return()

    label("loc_4054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_425C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_4124")

    ChrTalk(    #216
        0xFE,
        (
            "How's the investigation of\x01",
            "the fishing spots going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "I bet it's gotten a lot easier\x01",
            "with the fog all cleared up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "Go over all the places you couldn't\x01",
            "go to in detail, please.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4259")

    label("loc_4124")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_4182")

    ChrTalk(    #219
        0xFE,
        "Now, then. The fog's finally cleared.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        "I'd better get ready to head out...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4259")

    label("loc_4182")

    OP_A2(0xA)

    ChrTalk(    #221
        0xFE,
        "Now, then. The fog's finally cleared.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        "I'd better get ready to head out...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "This fog's delayed my investigation\x01",
            "plans by a lot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "I'd better get to this or the captain'll\x01",
            "be really angry with me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4259")

    Jump("loc_45CF")

    label("loc_425C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_43B2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_4323")

    ChrTalk(    #225
        0xFE,
        (
            "The Rolent area's still wrapped in\x01",
            "a terrible fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "You don't need to worry too much about\x01",
            "the fishing spot investigation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        "Take your time and put your back into it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_43AF")

    label("loc_4323")


    ChrTalk(    #228
        0xFE,
        (
            "Seems like the fog in Rolent\x01",
            "still hasn't cleared up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "For the love of all that's holy,\x01",
            "how much longer is this going\x01",
            "to go on...?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43AF")

    Jump("loc_45CF")

    label("loc_43B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_449F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_4418")

    ChrTalk(    #230
        0xFE,
        "You take care too, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        "Apparently the fog this morning's bad, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_449C")

    label("loc_4418")


    ChrTalk(    #232
        0xFE,
        (
            "I heard this morning's fog is even\x01",
            "worse than yesterday's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "At this rate heading out onto the\x01",
            "highways isn't gonna happen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_449C")

    Jump("loc_45CF")

    label("loc_449F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_45CF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_4538")

    ChrTalk(    #234
        0xFE,
        (
            "Hey, how's it going?\x01",
            "Making progress on the investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "The fog is pretty bad, but don't worry.\x01",
            "Just keep going steady.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CF")

    label("loc_4538")


    ChrTalk(    #236
        0xFE,
        "*siiigh* How boring.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        "Still, with this fog I can't really go fishing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "Guess I'll just look at some flowers\x01",
            "and try to distract myself...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45CF")

    Return()

    # Function_12_4002 end

    def Function_13_45D0(): pass

    label("Function_13_45D0")

    TalkBegin(0xFE)

    ChrTalk(    #239
        0xFE,
        "Oh, what's up, guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "My clients seem more tired than\x01",
            "I would have expected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "Today we rest here at Gurune Gate,\x01",
            "tomorrow we head off for the capital.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_45D0 end

    def Function_14_467B(): pass

    label("Function_14_467B")

    TalkBegin(0xFE)

    ChrTalk(    #242
        0xFE,
        (
            "Thinking about how we could get attacked\x01",
            "by monsters at any time in the fog was\x01",
            "just so, so horrifying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        "Just coming this far's worn me out entirely.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_467B end

    def Function_15_4723(): pass

    label("Function_15_4723")

    TalkBegin(0xFE)

    ChrTalk(    #244
        0xFE,
        "Phew! We can finally relax.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "Now that I've calmed down,\x01",
            "I'm getting hungry.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_4723 end

    def Function_16_477F(): pass

    label("Function_16_477F")

    TalkBegin(0xFE)

    ChrTalk(    #246
        0xFE,
        (
            "Phew! What the heck is up with\x01",
            "that fog, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "If we hadn't had a bracer with us, it'd be\x01",
            "way too risky to even set foot outside.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_477F end

    def Function_17_4814(): pass

    label("Function_17_4814")

    TalkBegin(0xFE)

    ChrTalk(    #248
        0xFE,
        (
            "I was really relieved when we got\x01",
            "out of the fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "Now that we've come this far, the capital's\x01",
            "just a hop away, so there's nothing to worry\x01",
            "about.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_4814 end

    def Function_18_48B7(): pass

    label("Function_18_48B7")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    OP_6D(-16190, 4000, 40000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1500, 0)
    Sleep(500)
    OP_22(0xC6, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x109, 0x1, 0x0, 0x13)
    Sleep(1800)
    OP_43(0x101, 0x1, 0x0, 0x14)
    OP_6D(-20500, 4000, 40500, 2000)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #250
        0x101,
        (
            "#1005FNow just a damn SECOND, 'Kevin,'\x01",
            "if that's even your name!\x01",
            "You can't weasel your way out of this!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #251
        0x109,
        (
            "#1066F#6PAh...haha. Guess you won't just let\x01",
            "it slide, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x101,
        (
            "#1019FCheeky winks aren't helping your case,\x01",
            "buster.\x02\x03",

            "#1005FLook, who in the hell ARE you?!\x02\x03",

            "You know what we're doing, you know about\x01",
            "Grancel Castle, you know about Ouroboros...\x02\x03",

            "Don't tell me you're just some\x01",
            "wandering priest!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x109,
        (
            "#1060F#6PI promise I've never lied to you.\x01",
            "I AM a full priest of the church.\x02\x03",

            "Though it's true that I'm not...\x01",
            "just a priest, you could say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        (
            "#1009FYeah, that's super reassuring\x01",
            "and not sinister at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x109,
        (
            "#1065F#6PI'll...explain everything later.\x01",
            "And I do mean everything.\x02\x03",

            "#1063FI was serious when I said we should get\x01",
            "back to the guildhouse, though.\x02\x03",

            "I have a feeling some serious stuff is\x01",
            "goin' down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x101,
        (
            "#1020FHuh? 'Serious stuff'?\x02\x03",

            "#1007FAaargh... Now I'm totally confused!\x02\x03",

            "#1027FWhy...\x02\x03",

            "I was going to see Joshua again...\x01",
            "Why did all this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x109,
        (
            "#1063F#6PMmm, 'bout that.\x01",
            "That letter from your boyfriend...\x02\x03",

            "You're sure it's from him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x101,
        (
            "#1004FHuh?\x02\x03",

            "#1026FY-Yeah. From what the girl who gave me\x01",
            "the letter said, I can't imagine it's\x01",
            "anyone else...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x109,
        (
            "#1063F#6PBut this girl doesn't actually know your\x01",
            "Joshua by sight, right?\x02\x03",

            "In that case, it'd be easy enough to get\x01",
            "someone who looks close enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        "#1026FB-But even the handwriting is like Joshua's...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x109,
        (
            "#1065F#6PIt's easier to spoof handwriting than you think,\x01",
            "especially if you know how a person writes.\x02\x03",

            "It's definitely easy enough to fool someone\x01",
            "who...ah, already wants to believe.\x02\x03",

            "#1063FHere's the letter I got at the cathedral,\x01",
            "for the record.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #262
        "\x07\x05Kevin produced an envelope from his pocket.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x240097, 0xBE, 0x82, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(380, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #263
        "\x07\x00#1020FWhat...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1500)

    ChrTalk(    #264
        0x109,
        (
            "#1060F#6PThought so. We both got the same envelope.\x02\x03",

            "The letter I got promised me a juicy lead\x01",
            "on what I've been investigating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x101,
        (
            "#1020FSo both letters were done by the same group?\x02\x03",

            "But...who? Why?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x109,
        (
            "#1067F#6PNo idea.\x01",
            "Maybe the society, maybe someone else.\x02\x03",

            "#1068FAll I can say is...they got us both\x01",
            "hook, line, and sinker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        "#1020F...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 5)
    OP_0D()
    Sleep(500)
    OP_9E(0x101, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(500)

    ChrTalk(    #268
        0x101,
        "#1022F...Don't...with me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x109,
        "#1064F#6PEh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x101,
        (
            "#1022FI don't know who these jerks are,\x01",
            "but they don't get to screw with me...\x02\x03",

            "Pretending to be Joshua...\x01",
            "and trying to lure me to my death?\x02\x03",

            "#1027FI won't let them get away with this...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #271
        0x101,
        (
            "#1023F#3SYOU HEAR ME?!\x01",
            "I AM BEATING YOUR FACES IN, YOU JERKS!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #272
        0x109,
        (
            "#1070F#6PNghaaaa, my ears...\x01",
            "Calm down, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #273
        0x109,
        (
            "#1065F#6PGetting worked up and losing our focus is\x01",
            "EXACTLY what the people behind this want\x01",
            "to have happen.\x02\x03",

            "#1060FLet's head back and go over what we know,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(    #274
        0x101,
        (
            "#1007FYeah... Okay...\x02\x03",

            "#1019FThough, Kevin? Just to be clear, I still don't\x01",
            "trust you.\x02\x03",

            "If you, like, do a big dramatic reveal as an\x01",
            "Ouroboros agent or something...\x01",
            "I WILL brain you. Got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x109,
        (
            "#1062F#6PHaha! Don't worry.\x02\x03",

            "Heck, I'd love to get hit by you!\x02\x03",

            "#1061FI'm always willing to sacrifice my body\x01",
            "for the woman I love! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x101,
        (
            "#1013FWh-What're you...\x02\x03",

            "#1007FOh, come on... Stop trying to distract me\x01",
            "from my burning distrust, here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x109,
        (
            "#1061F#6PIt's what I do best!\x02\x03",

            "#1060FSo, like I said, back to the guildhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x101,
        "#1002FLet's go.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1638)
    OP_28(0x8D, 0x1, 0x4)
    OP_28(0x8D, 0x1, 0x8)
    OP_28(0x8D, 0x1, 0x10)
    OP_28(0x8D, 0x1, 0x20)
    OP_28(0x8D, 0x4, 0x10)
    OP_20(0x3E8)
    EventEnd(0x0)
    OP_1D(0x10)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_18_48B7 end

    def Function_19_5671(): pass

    label("Function_19_5671")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -15020, 4000, 36500, 0)

    def lambda_5698():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5698)
    OP_8E(0xFE, 0xFFFFC554, 0xFA0, 0x9BFA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFAE66, 0xFA0, 0x9BFA, 0x7D0, 0x0)
    Return()

    # Function_19_5671 end

    def Function_20_56CD(): pass

    label("Function_20_56CD")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -15020, 4000, 36500, 0)

    def lambda_56F4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_56F4)
    OP_8E(0xFE, 0xFFFFC554, 0xFA0, 0x9BFA, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFB794, 0xFA0, 0x9BFA, 0x9C4, 0x0)
    Return()

    # Function_20_56CD end

    def Function_21_5729(): pass

    label("Function_21_5729")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_5AB3")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_587F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_57CF")

    ChrTalk(    #279
        0x108,
        (
            "#070FTraveling by foot is good training,\x01",
            "but it's not a good use of time.\x02\x03",

            "If you want to go to Bose, we\x01",
            "should take the airship.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_587C")

    label("loc_57CF")


    ChrTalk(    #280
        0x108,
        (
            "#070FThis is towards Rolent, isn't it?\x02\x03",

            "Traveling by foot is good training,\x01",
            "but it's not a good use of time.\x02\x03",

            "If you want to go to Bose, we\x01",
            "should take the airship.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_587C")

    Jump("loc_5A95")

    label("loc_587F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5986")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_589C")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_58A3")

    label("loc_589C")

    TurnDirection(0x106, 0x0, 400)

    label("loc_58A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5925")

    ChrTalk(    #281
        0x106,
        (
            "#053F...Going by foot, put simply,\x01",
            "is a waste of time.\x02\x03",

            "#050FIf we're going to Bose,\x01",
            "let's go to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5983")

    label("loc_5925")


    ChrTalk(    #282
        0x106,
        (
            "#050FThis is towards Rolent.\x02\x03",

            "If we're going to Bose,\x01",
            "let's head to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_5983")

    Jump("loc_5A95")

    label("loc_5986")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_599C")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_59A3")

    label("loc_599C")

    TurnDirection(0x103, 0x0, 400)

    label("loc_59A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_5A2F")

    ChrTalk(    #283
        0x103,
        (
            "#026F...Going by foot, put simply,\x01",
            "is a waste of time.\x02\x03",

            "#020FIf we're going to Bose, we should\x01",
            "make use of the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A95")

    label("loc_5A2F")


    ChrTalk(    #284
        0x103,
        (
            "#020FThis is towards Rolent.\x02\x03",

            "If we're going to Bose, we should\x01",
            "make use of the landing port.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_5A95")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_5DC7")

    label("loc_5AB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 0)), scpexpr(EXPR_END)), "loc_5B87")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B1A")

    ChrTalk(    #285
        0x101,
        (
            "#1002FWe can't be wasting time here.\x01",
            "We'd better hurry back to the guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B69")

    label("loc_5B1A")


    ChrTalk(    #286
        0x109,
        (
            "#1063FWe can't be wasting time here.\x01",
            "We'd better hurry back to the guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B69")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_5DC7")

    label("loc_5B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 7)), scpexpr(EXPR_END)), "loc_5C00")
    EventBegin(0x1)

    ChrTalk(    #287
        0x101,
        (
            "#1003F(...Where am I even going? Joshua's\x01",
            "on the top of the wall, isn't he?)\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_5DC7")

    label("loc_5C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_5DC7")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C90")

    ChrTalk(    #288
        0x108,
        (
            "#070FWhoa, this is towards Rolent.\x02\x03",

            "We don't have the time to visit other\x01",
            "regions right now. Let's just turn back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DAC")

    label("loc_5C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5D21")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CAD")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_5CB4")

    label("loc_5CAD")

    TurnDirection(0x106, 0x0, 400)

    label("loc_5CB4")


    ChrTalk(    #289
        0x106,
        (
            "#050FWhoa, this is towards Rolent.\x02\x03",

            "We don't have time to go to other\x01",
            "regions. Let's just turn back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DAC")

    label("loc_5D21")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D37")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_5D3E")

    label("loc_5D37")

    TurnDirection(0x103, 0x0, 400)

    label("loc_5D3E")


    ChrTalk(    #290
        0x103,
        (
            "#020FWhoa, this is towards Rolent.\x02\x03",

            "We don't have the time to visit other\x01",
            "regions. Let's just turn back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DAC")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_5DC7")

    Return()

    # Function_21_5729 end

    def Function_22_5DC8(): pass

    label("Function_22_5DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_6075")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5E6F")

    ChrTalk(    #291
        0x108,
        (
            "#070F...No, it really isn't a good idea\x01",
            "to travel to Bose this way.\x02\x03",

            "When we want to leave Rolent,\x01",
            "let's head to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5F12")

    label("loc_5E6F")


    ChrTalk(    #292
        0x108,
        (
            "#070FThis is towards Grancel.\x02\x03",

            "...No, it really isn't a good idea\x01",
            "to head to Bose this way.\x02\x03",

            "When we want to leave Rolent,\x01",
            "let's head to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_5F12")

    Jump("loc_6057")

    label("loc_5F15")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F2B")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_5F32")

    label("loc_5F2B")

    TurnDirection(0x103, 0x0, 400)

    label("loc_5F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_5FBD")

    ChrTalk(    #293
        0x103,
        (
            "#020F...No, we really shouldn't travel\x01",
            "to Bose this way.\x02\x03",

            "When we want to leave Rolent,\x01",
            "let's make use of the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6057")

    label("loc_5FBD")


    ChrTalk(    #294
        0x103,
        (
            "#020FThis is towards Grancel.\x02\x03",

            "...No, we really shouldn't travel\x01",
            "to Bose this way.\x02\x03",

            "When we want to leave Rolent,\x01",
            "let's head to the landing port.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_6057")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_649F")

    label("loc_6075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_61BA")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6101")

    ChrTalk(    #295
        0x108,
        (
            "#070FWhoa, this is towards Grancel.\x02\x03",

            "We don't have the time to visit other\x01",
            "regions right now. Let's turn back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_619C")

    label("loc_6101")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6117")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_611E")

    label("loc_6117")

    TurnDirection(0x103, 0x0, 400)

    label("loc_611E")


    ChrTalk(    #296
        0x103,
        (
            "#022FBeyond this point is Grancel.\x02\x03",

            "...We don't have time to stop in at the\x01",
            "capital. Let's head to Mistwald in the east.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_619C")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_649F")

    label("loc_61BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_END)), "loc_637B")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61D9")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_61E0")

    label("loc_61D9")

    TurnDirection(0x103, 0x0, 400)

    label("loc_61E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_6254")

    ChrTalk(    #297
        0x103,
        (
            "#022FBeyond here is the Grancel region.\x02\x03",

            "Hold off on the side trip.\x01",
            "We need to hurry to Perzel Farm.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_635D")

    label("loc_6254")


    ChrTalk(    #298
        0x103,
        (
            "#022FBeyond here is the Grancel region.\x02\x03",

            "Hold off on the side trip.\x01",
            "We need to hurry to Perzel Farm.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62F5")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #299
        0x101,
        "#1002FY-Yeah, you're right.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_62F5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6326")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #300
        0x105,
        "#042FYes, absolutely.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_6326")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_635D")
    TurnDirection(0x0, 0x103, 400)

    ChrTalk(    #301
        0x107,
        "#062FY-Yes, um, understood.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_635D")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_649F")

    label("loc_637B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_649F")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6407")

    ChrTalk(    #302
        0x108,
        (
            "#070FWhoa, this is towards Grancel.\x02\x03",

            "We don't have the time to visit other\x01",
            "regions right now. Let's turn back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6484")

    label("loc_6407")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_641D")
    TurnDirection(0x103, 0x1, 400)
    Jump("loc_6424")

    label("loc_641D")

    TurnDirection(0x103, 0x0, 400)

    label("loc_6424")


    ChrTalk(    #303
        0x103,
        (
            "#020FPast here is the Grancel region.\x02\x03",

            "We don't have time for side trips.\x01",
            "Let's turn back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6484")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_649F")

    Return()

    # Function_22_5DC8 end

    def Function_23_64A0(): pass

    label("Function_23_64A0")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_23_64A0 end

    SaveToFile()

Try(main)
