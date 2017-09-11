from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2700   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2700.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/T2700   ._SN',
            'ED6_DT01/T2700_1 ._SN',
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
        'CWO Hahn',                             # 9
        'Butler Phillip',                       # 10
        '1st Lieutenant Schwarz',               # 11
        'Sieg',                                 # 12
        'Target Camera',                        # 13
        'Carna',                                # 14
        'Private Nix',                          # 15
        'Private Vernon',                       # 16
        'Mikelson',                             # 17
        'Aina Holden',                          # 18
        'Kaldia Tunnel',                        # 19
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
        'ED6_DT07/CH01310 ._CH',             # 00
        'ED6_DT07/CH02470 ._CH',             # 01
        'ED6_DT07/CH01240 ._CH',             # 02
        'ED6_DT07/CH02320 ._CH',             # 03
        'ED6_DT07/CH01640 ._CH',             # 04
        'ED6_DT07/CH02090 ._CH',             # 05
        'ED6_DT07/CH02323 ._CH',             # 06
        'ED6_DT06/CH20059 ._CH',             # 07
        'ED6_DT06/CH20113 ._CH',             # 08
        'ED6_DT07/CH01220 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01310P._CP',             # 00
        'ED6_DT07/CH02470P._CP',             # 01
        'ED6_DT07/CH01240P._CP',             # 02
        'ED6_DT07/CH02320P._CP',             # 03
        'ED6_DT07/CH01640P._CP',             # 04
        'ED6_DT07/CH02090P._CP',             # 05
        'ED6_DT07/CH02323P._CP',             # 06
        'ED6_DT06/CH20059P._CP',             # 07
        'ED6_DT06/CH20113P._CP',             # 08
        'ED6_DT07/CH01220P._CP',             # 09
    )

    DeclNpc(
        X                   = 5500,
        Z                   = 5000,
        Y                   = 0,
        Direction           = 270,
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
        X                   = 4500,
        Z                   = 5000,
        Y                   = 0,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -15300,
        Z                   = 100,
        Y                   = -11300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 18400,
        Z                   = 5000,
        Y                   = 1400,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -19800,
        Z                   = 0,
        Y                   = -2200,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 4710,
        Z                   = 5000,
        Y                   = 2490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -62340,
        Z                   = 0,
        Y                   = -1100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 21320,
        Z                   = 5000,
        Y                   = 460,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 19830,
        TriggerZ            = 5000,
        TriggerY            = -50,
        TriggerRange        = 800,
        ActorX              = 19830,
        ActorZ              = 6000,
        ActorY              = -50,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -45890,
        TriggerZ            = 0,
        TriggerY            = 2240,
        TriggerRange        = 1500,
        ActorX              = -45890,
        ActorZ              = 1700,
        ActorY              = 2240,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2A2",          # 00, 0
        "Function_1_358",          # 01, 1
        "Function_2_3D7",          # 02, 2
        "Function_3_3ED",          # 03, 3
        "Function_4_411",          # 04, 4
        "Function_5_685",          # 05, 5
        "Function_6_6E8",          # 06, 6
        "Function_7_101B",         # 07, 7
        "Function_8_1254",         # 08, 8
        "Function_9_12A4",         # 09, 9
        "Function_10_173D",        # 0A, 10
        "Function_11_2C3C",        # 0B, 11
        "Function_12_2C64",        # 0C, 12
        "Function_13_2CB8",        # 0D, 13
        "Function_14_2D19",        # 0E, 14
    )


    def Function_0_2A2(): pass

    label("Function_0_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2AC")
    Jump("loc_2C8")

    label("loc_2AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2BB")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_2C8")

    label("loc_2BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8")
    ClearChrFlags(0x10, 0x80)

    label("loc_2C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E3")
    SetChrFlags(0x8, 0x80)

    label("loc_2E3")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_2F3"),
        (100, "loc_32A"),
        (SWITCH_DEFAULT, "loc_346"),
    )


    label("loc_2F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_314")
    OP_28(0x23, 0x1, 0x1)
    Event(1, 0)

    label("loc_314")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_327")
    OP_A2(0x503)
    Event(0, 10)

    label("loc_327")

    Jump("loc_346")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_340")
    OP_A2(0x501)
    Event(0, 9)
    Jump("loc_343")

    label("loc_340")

    OP_A2(0x53C)

    label("loc_343")

    Jump("loc_346")

    label("loc_346")

    OP_51(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_0_2A2 end

    def Function_1_358(): pass

    label("Function_1_358")

    OP_16(0x2, 0xFA0, 0xFFFDC5B0, 0xFFFE0C00, 0x3004F)
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_382")
    OP_72(0x2, 0x10)
    OP_65(0x0, 0x1)
    Jump("loc_395")

    label("loc_382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_END)), "loc_395")
    OP_72(0x2, 0x10)
    OP_6F(0x2, 160)

    label("loc_395")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A9")
    OP_28(0x2A, 0x1, 0x2000)

    label("loc_3A9")

    OP_1C(0x1, 0x0, 0xE)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3C6"),
        (101, "loc_3C6"),
        (102, "loc_3CE"),
        (103, "loc_3CE"),
        (SWITCH_DEFAULT, "loc_3D6"),
    )


    label("loc_3C6")

    OP_22(0x1CE, 0x1, 0x64)
    Jump("loc_3D6")

    label("loc_3CE")

    OP_22(0x1CA, 0x1, 0x64)
    Jump("loc_3D6")

    label("loc_3D6")

    Return()

    # Function_1_358 end

    def Function_2_3D7(): pass

    label("Function_2_3D7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3D7")

    label("loc_3EC")

    Return()

    # Function_2_3D7 end

    def Function_3_3ED(): pass

    label("Function_3_3ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_410")
    OP_8D(0xFE, 13000, 2500, 1500, 0, 1500)
    Jump("Function_3_3ED")

    label("loc_410")

    Return()

    # Function_3_3ED end

    def Function_4_411(): pass

    label("Function_4_411")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_681")

    ChrTalk(    #0
        0xFE,
        "So, do you have a moment?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "If you don't mind, I could use\x01",
            "your help.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Why not?]\x01",           # 0
            "[No, thanks...]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4D9"),
        (1, "loc_571"),
        (SWITCH_DEFAULT, "loc_681"),
    )


    label("loc_4D9")

    OP_28(0x23, 0x4, 0x8)

    ChrTalk(    #2
        0x101,
        "#000FSure, why not?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "Thank you. You're doing me\x01",
            "a massive favor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "Now, let me give you a\x01",
            "full explanation...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    NewScene("ED6_DT01/T2710   ._SN", 101, 0, 0)
    IdleLoop()
    Jump("loc_681")

    label("loc_571")

    OP_28(0x23, 0x1, 0x4000)

    ChrTalk(    #5
        0x101,
        (
            "#003FNo, thanks...we're a little busy\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        "That's no good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "We'll try to handle it on our\x01",
            "own for a little bit longer,\x01",
            "but I'm not optimistic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "When you're available please\x01",
            "come back here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        "#010FWe will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        "I appreciate it.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 0)
    Jump("loc_681")

    label("loc_681")

    TalkEnd(0x8)
    Return()

    # Function_4_411 end

    def Function_5_685(): pass

    label("Function_5_685")

    TalkBegin(0xD)

    ChrTalk(    #11
        0xFE,
        "Whew...finally finished.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I'd been hoping to cool off here,\x01",
            "but it's just too hot.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xD)
    Return()

    # Function_5_685 end

    def Function_6_6E8(): pass

    label("Function_6_6E8")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_8A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_79C")
    OP_A2(0x0)

    ChrTalk(    #13
        0xFE,
        (
            "Hey, I don't see many travelers\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "When everyone goes to Grancel,\x01",
            "do you want to go take in the sights?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "Yeah, that should be good.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A2")

    label("loc_79C")


    ChrTalk(    #16
        0xFE,
        (
            "If you think about it, going when\x01",
            "everyone else isn't around is perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "The hotspots won't be crowded,\x01",
            "and I'll bet the hotels aren't\x01",
            "too pricey...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "But now's the only time to check\x01",
            "out the birthday festivities...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "Hmm...don't worry about it.\x02",
    )

    CloseMessageWindow()

    label("loc_8A2")

    Jump("loc_1017")

    label("loc_8A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_98D")

    ChrTalk(    #20
        0xFE,
        (
            "Wow, I wasn't expecting the\x01",
            "inspections to be called off\x01",
            "so quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "We're already back to standard\x01",
            "security procedures.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I haven't been briefed, but I'd\x01",
            "guess this means that the\x01",
            "criminals have been caught.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1017")

    label("loc_98D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_A20")

    ChrTalk(    #23
        0xFE,
        (
            "The checkpoint's currently in a\x01",
            "state of high alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Sorry, but you need to keep\x01",
            "your voices down when it\x01",
            "comes to any rumors.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1017")

    label("loc_A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_BB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1C")
    OP_A2(0x0)

    ChrTalk(    #25
        0xFE,
        (
            "For right now, the checkpoint is\x01",
            "just maintaining contact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Yesterday, all of the orbments\x01",
            "in Zeiss just shut off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "If the same thing happened\x01",
            "to Ruan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "The Langland Bridge would be stuck\x01",
            "in the raised position.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB5")

    label("loc_B1C")


    ChrTalk(    #29
        0xFE,
        (
            "I hear that the central lab makes\x01",
            "a lot of strange stuff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "How could anyone manage to\x01",
            "create something that would\x01",
            "just shut orbal power down?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB5")

    Jump("loc_1017")

    label("loc_BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C7C")

    ChrTalk(    #31
        0xFE,
        "That gate leads to Zeiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Kaldia Tunnel up here isn't quite\x01",
            "the same as it used to be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Anyone who travels through it is\x01",
            "going to find a new experience,\x01",
            "newcomer or not.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1017")

    label("loc_C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_D40")

    ChrTalk(    #34
        0xFE,
        "That gate leads to Zeiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Kaldia Tunnel up here isn't quite\x01",
            "the same as it used to be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Anyone who travels through it is\x01",
            "going to find a new experience,\x01",
            "newcomer or not.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1017")

    label("loc_D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_F9D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4E")
    OP_A2(0x0)

    ChrTalk(    #37
        0xFE,
        (
            "Both of the higher ups\x01",
            "were writing up reports like crazy\x01",
            "a little while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "If there's any truth to the rumors I've\x01",
            "heard, that duke is one incredibly\x01",
            "frustrating man to deal with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I'm glad I'm on inspection\x01",
            "detail today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EEA")

    label("loc_E4E")


    ChrTalk(    #40
        0xFE,
        (
            "If there's any truth to the rumors I've\x01",
            "heard, that duke is one incredibly\x01",
            "frustrating man to deal with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I'm glad I'm on inspection\x01",
            "detail today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EEA")

    Jump("loc_F9A")

    label("loc_EED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_F4A")

    ChrTalk(    #42
        0xFE,
        (
            "The really obnoxious ones always seem \x01",
            "to want to come to the checkpoints.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F9A")

    label("loc_F4A")


    ChrTalk(    #43
        0xFE,
        (
            "The really obnoxious ones always seem \x01",
            "to want to come to the checkpoints.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9A")

    Jump("loc_1017")

    label("loc_F9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1017")

    ChrTalk(    #44
        0xFE,
        (
            "I'll say one thing for guard duty here...\x01",
            "the view is great.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "It can get tough when winter\x01",
            "comes, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1017")

    TalkEnd(0xE)
    Return()

    # Function_6_6E8 end

    def Function_7_101B(): pass

    label("Function_7_101B")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_10A2")

    ChrTalk(    #46
        0xFE,
        (
            "Hey. Welcome to the Air-Letten\x01",
            "checkpoint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "If you want to get set up to go\x01",
            "through, head to the counter\x01",
            "inside.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1250")

    label("loc_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_11DE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1132")

    ChrTalk(    #48
        0xFE,
        (
            "We had some rich guy come through\x01",
            "with a regular laundry list of\x01",
            "complaints...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "I don't know what his problem was.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11DB")

    label("loc_1132")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x23, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_118D")

    ChrTalk(    #50
        0xFE,
        (
            "It's been noisy in there for a\x01",
            "while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "I wonder what's going on.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11DB")

    label("loc_118D")


    ChrTalk(    #52
        0xFE,
        (
            "It's been noisy in there for a\x01",
            "while now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "I wonder what's going on.\x02",
    )

    CloseMessageWindow()

    label("loc_11DB")

    Jump("loc_1250")

    label("loc_11DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 3)), scpexpr(EXPR_END)), "loc_1250")

    ChrTalk(    #54
        0xFE,
        (
            "I heard we had a messenger from\x01",
            "Leiston Fortress a while back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "No telling what that was about...\x02",
    )

    CloseMessageWindow()

    label("loc_1250")

    TalkEnd(0xF)
    Return()

    # Function_7_101B end

    def Function_8_1254(): pass

    label("Function_8_1254")

    TalkBegin(0x10)

    ChrTalk(    #56
        0xFE,
        (
            "It's pretty bizarre that the ruins\x01",
            "themselves became the waterfall.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    Return()

    # Function_8_1254 end

    def Function_9_12A4(): pass

    label("Function_9_12A4")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(5900, 12000, 13400, 0)
    OP_6C(85000, 0)
    OP_6B(8000, 0)
    StopSound(0x7D00, 0x3D090, 0x0)
    SetChrPos(0x101, -51400, 0, -1100, 90)
    SetChrPos(0x102, -52500, 0, -300, 90)
    SetChrPos(0x105, -52500, 0, -2100, 90)
    FadeToBright(2000, 0)
    StopSound(0x7D00, 0x1FBD0, 0x2EE0)

    def lambda_132A():
        OP_6B(2800, 11000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_132A)

    def lambda_133A():
        OP_6C(45000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_133A)
    Sleep(3000)

    def lambda_134F():
        OP_6D(-50000, 0, -1500, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_134F)
    Sleep(9000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FC")

    ChrTalk(    #57
        0x101,
        (
            "#501F#2PWow... This is a nice little spot.\x02\x03",

            "The view here is breathtaking.\x01",
            "Certainly doesn't feel like a\x01",
            "checkpoint, that's for sure!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_149C")

    label("loc_13FC")


    ChrTalk(    #58
        0x101,
        (
            "#501F#2PI've been here before...but\x01",
            "this is a nice little spot.\x02\x03",

            "The view here is breathtaking.\x01",
            "Certainly doesn't feel like a\x01",
            "checkpoint, that's for sure!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_149C")

    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #59
        0x105,
        (
            "#040FActually, I hear that a lot of\x01",
            "visitors come here to see the\x01",
            "waterfall.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14FB():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14FB)
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #60
        0x101,
        (
            "#006F#2PReally?\x02\x03",

            "Ruan sure has a lot of nice places, huh?\x02\x03",

            "I can understand why the duke would want to\x01",
            "live here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x105,
        (
            "#041FAgreed.\x02\x03",

            "#048FBut I think Rolent is also a\x01",
            "nice, relaxing place to live.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#004F#2POh, you've been to Rolent?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x105,
        (
            "#041FYes, I've been to all five of the\x01",
            "great cities.\x02\x03",

            "#040FOh, that's right... Zeiss is\x01",
            "up ahead...\x02\x03",

            "You'll be surprised how charming\x01",
            "it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#000F#2PHmm... Really?\x02\x03",

            "#001FSounds like we're in for some fun.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #65
        0x102,
        (
            "#010F#1PAll right. Why don't we get\x01",
            "the paperwork started, then?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #66
        0x101,
        "#006F#2POkay.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_9_12A4 end

    def Function_10_173D(): pass

    label("Function_10_173D")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xE, 0x80)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-5200, 5000, 7200, 0)
    SetChrPos(0x101, -5000, 5000, 6600, 90)
    SetChrPos(0x105, -6300, 5000, 7100, 90)
    SetChrPos(0x102, -6300, 5000, 5800, 90)
    OP_72(0x2, 0x10)
    OP_6F(0x2, 160)
    FadeToBright(1000, 0)

    def lambda_17AD():
        OP_6B(5000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_17AD)

    def lambda_17BD():
        OP_6D(10900, 9200, 14500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17BD)

    def lambda_17D5():
        OP_6C(24000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17D5)
    Sleep(5000)
    SetChrPos(0xB, 10300, 6400, 3150, 0)
    SetChrPos(0xA, 900, 5000, 800, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x101, 8300, 5000, 2500, 0)
    SetChrPos(0x105, 6800, 5000, 2500, 0)
    SetChrPos(0x102, 7700, 5000, 1000, 0)

    ChrTalk(    #67
        0x101,
        "#001F#1PWow... This is amazing!\x02",
    )

    CloseMessageWindow()

    def lambda_1869():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1869)

    def lambda_1879():
        OP_6D(7800, 5000, 2500, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1879)
    Sleep(5000)

    ChrTalk(    #68
        0x101,
        (
            "#501F#4PHuh... So the waterfall comes\x01",
            "from a man-made river.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x102,
        (
            "#010F#4PI think it's called the Lhotse Waterway.\x02\x03",

            "It was made a very long time ago.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(    #70
        0x105,
        (
            "#040F#3PYes, and it's linked directly to\x01",
            "the Valleria Lakeshore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#007F#4PPretty impressive, given that they\x01",
            "did it without any orbments to help.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #72
        0x101,
        "#006F#3PSo, what's that over there...?\x02",
    )

    CloseMessageWindow()

    def lambda_1A0D():
        OP_6C(90000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A0D)

    def lambda_1A1D():
        OP_6D(17680, 5000, -70, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A1D)

    def lambda_1A35():
        OP_6B(4250, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1A35)

    def lambda_1A45():
        OP_67(0, 3980, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1A45)

    def lambda_1A5D():
        OP_6E(345, 4000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_1A5D)

    def lambda_1A6D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A6D)

    def lambda_1A7B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1A7B)
    OP_8C(0x105, 90, 400)

    def lambda_1A90():
        OP_8E(0xFE, 0x2C88, 0x1388, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1A90)
    Sleep(800)

    def lambda_1AB0():
        OP_8E(0xFE, 0x2A94, 0x1388, 0xFFFFFC7C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1AB0)
    Sleep(300)

    def lambda_1AD0():
        OP_8E(0xFE, 0x2648, 0x1388, 0x2BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1AD0)
    WaitChrThread(0x101, 0x2)
    OP_8C(0x101, 90, 0)
    WaitChrThread(0x102, 0x2)
    OP_8C(0x102, 90, 0)
    WaitChrThread(0x105, 0x2)
    OP_8C(0x105, 90, 0)
    Sleep(500)

    ChrTalk(    #73
        0x102,
        (
            "#010FThat's the entrance to the tunnel,\x01",
            "I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#501FYeah...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_20(0x5DC)
    Fade(1000)
    TurnDirection(0x102, 0x105, 0)
    TurnDirection(0x101, 0x105, 0)
    TurnDirection(0x105, 0x101, 0)
    OP_8C(0xB, 180, 0)
    OP_6D(11300, 5000, 540, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(60000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_21()
    OP_1D(0x58)

    ChrTalk(    #75
        0x101,
        "#505FSo, I guess this is goodbye...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x105,
        (
            "#047FYes...\x02\x03",

            "#040FSo, you're going to be traveling\x01",
            "around the kingdom, right?\x02\x03",

            "We might be able to meet again\x01",
            "in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#004FReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x105,
        (
            "#045FI'll be going back there when the\x01",
            "queen's birthday celebration\x01",
            "starts.\x02\x03",

            "Some of my relatives will be\x01",
            "there, so I have to join them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        (
            "#010FThat's just a month away,\x01",
            "isn't it?\x02\x03",

            "I think we may actually be in\x01",
            "Grancel around that time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#006FSo, then...\x02\x03",

            "Once you're done with your family\x01",
            "stuff, contact the Grancel guild\x01",
            "branch.\x02\x03",

            "If you do, we can try to meet up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x105,
        (
            "#041FI certainly will.\x02\x03",

            "#048FEstelle and Joshua...\x02\x03",

            "I can't thank you enough.\x02\x03",

            "I won't ever forget everything\x01",
            "that you've done for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#008FC-Come on...\x01",
            "Don't be so formal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        (
            "#019FWe're in your debt as well,\x01",
            "for many reasons.\x02\x03",

            "I'd say we're pretty even.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x105,
        (
            "#542FWhat a thing to say...\x02\x03",

            "...\x02\x03",

            "#049FWhen... When we confronted the\x01",
            "mayor...\x02\x03",

            "...I said some terrible things.\x02\x03",

            "'You care for no one but yourself...'\x02\x03",

            "But...I was no different.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#004FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x105,
        (
            "#047FI've been running away from the\x01",
            "reality of my own situation for\x01",
            "a while now.\x02\x03",

            "To the orphanage...and to the\x01",
            "academy...\x02\x03",

            "#040FBut the two of you taught me\x01",
            "something.\x02\x03",

            "You helped me find the courage\x01",
            "to hold my head high...\x02\x03",

            "...and find the strength to\x01",
            "protect what matters.\x02\x03",

            "#041FBecause of you, I know how\x01",
            "to be brave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#506FI...I don't really get it...\x02\x03",

            "...but if we were able to help\x01",
            "you, I'm happy.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2170():

        label("loc_2170")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2170")

    QueueWorkItem2(0x105, 3, lambda_2170)
    OP_92(0x101, 0x105, 0x258, 0x7D0, 0x0)
    Fade(500)
    SetChrPos(0x105, 10000, 5000, 640, 90)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x2)
    ClearChrFlags(0x105, 0x1)
    SetChrChipByIndex(0x105, 7)
    SetChrSubChip(0x105, 1)
    OP_0D()

    ChrTalk(    #88
        0x105,
        "#540FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#008F#2PHa ha...\x01",
            "Cheer up, okay?\x02\x03",

            "#508FWe'll see each other again\x01",
            "in Grancel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x105,
        "#048FYes... Absolutely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xB,
        "#310FScree!\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0x105, 9800, 5000, 700, 90)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x105, 0x2)
    SetChrFlags(0x105, 0x1)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    OP_0D()
    OP_94(0x1, 0x101, 0xB4, 0x1F4, 0x7D0, 0x0)
    TurnDirection(0x101, 0xB, 400)
    OP_44(0x105, 0xFF)
    TurnDirection(0x105, 0xB, 400)

    ChrTalk(    #92
        0x101,
        (
            "#001F#4PHa, and maybe we'll get to\x01",
            "see Sieg there, too, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xB,
        "#311FScree! ☆\x02",
    )

    CloseMessageWindow()
    OP_44(0x105, 0xFF)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #94
        0x101,
        (
            "#004F#4PThat was a joke. I mean, Grancel's\x01",
            "pretty far away! I don't think\x01",
            "those wings would hold...\x02\x03",

            "Besides...your home is here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xB,
        "#310FScreeee?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x105,
        (
            "#041FHa ha... Sieg isn't just any bird,\x01",
            "you know.\x02\x03",

            "I think he'll be there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#506F#4PI'm sure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x102,
        (
            "#019FHa ha ha. Sieg's just full of\x01",
            "surprises, isn't he?\x02\x03",

            "#010FWell, then...\x01",
            "Shall we be off?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #99
        0x101,
        "#006F#6PYeah...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)
    OP_8C(0x105, 90, 400)

    ChrTalk(    #100
        0x105,
        (
            "#040FHey...\x02\x03",

            "Good luck to both of you on\x01",
            "your journey.\x02\x03",

            "And I'll be praying for you to\x01",
            "find your father.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xB,
        "#311FScreeeee... ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#006F#4PThank you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x102,
        "#010FYou two take care!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 0)

    def lambda_256B():
        OP_6D(14900, 5000, 0, 3000)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_256B)

    def lambda_2583():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2583)

    def lambda_2591():
        OP_8F(0xFE, 0x5EEC, 0x1388, 0xFFFFFED4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2591)
    Sleep(200)

    def lambda_25B1():
        OP_8F(0xFE, 0x4F4C, 0x1388, 0x12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25B1)
    Sleep(500)

    def lambda_25D1():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_25D1)

    def lambda_25DF():
        OP_8F(0xFE, 0x5EEC, 0x1388, 0x12C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25DF)
    Sleep(3500)
    OP_72(0x2, 0x800)
    OP_22(0xDF, 0x0, 0x64)
    OP_70(0x2, 0x0)
    OP_73(0x2)
    OP_71(0x2, 0x800)
    OP_6D(11300, 5000, 540, 1500)

    ChrTalk(    #104
        0x105,
        "#049F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xB,
        "#310FScree.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xB, 400)

    ChrTalk(    #106
        0x105,
        (
            "#542F#2PYes, I think so, too.\x02\x03",

            "We'll see them again.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    OP_20(0x5DC)

    NpcTalk(    #107
        0xA,
        "Woman's Voice",
        "#2PSorry to keep you waiting, Kloe.\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_44(0xB, 0xFF)

    def lambda_26E8():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_26E8)

    def lambda_26F6():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_26F6)

    def lambda_2704():
        OP_8E(0xFE, 0x19C8, 0x1388, 0x320, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2704)
    OP_6D(8800, 5000, 680, 2000)
    WaitChrThread(0xA, 0x1)

    ChrTalk(    #108
        0x105,
        (
            "#040F...Miss Julia.\x02\x03",

            "You're done with your duties\x01",
            "at Leiston Fortress?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        (
            "#170FYes. It took longer than I had\x01",
            "anticipated.\x02\x03",

            "#170FPardon my rudeness, but I've\x01",
            "come to get your report on\x01",
            "the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x105,
        "#048FThank you for your service.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xB,
        "#311FScreee. ♪\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x40)
    SetChrSubChip(0xB, 4)
    Sleep(100)
    SetChrSubChip(0xB, 3)
    Sleep(100)
    SetChrChipByIndex(0xB, 3)
    SetChrSubChip(0xB, 0)
    TurnDirection(0xA, 0xB, 0)
    OP_22(0x8C, 0x0, 0x64)

    def lambda_286D():
        OP_8E(0xFE, 0x17E8, 0x157C, 0x596, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_286D)
    Sleep(300)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0xA, 0x17E8, 0x1388, 0x1D6, 0x7D0, 0x0)
    WaitChrThread(0xB, 0x1)
    OP_43(0xB, 0x1, 0x0, 0xB)
    OP_A2(0x2)
    Sleep(500)
    OP_8C(0xA, 315, 300)

    def lambda_28CE():
        OP_8C(0xFE, 225, 300)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_28CE)

    ChrTalk(    #112
        0xA,
        (
            "#174F#2PHey, now...\x01",
            "Settle down, Sieg.\x02\x03",

            "Have you been fulfilling your\x01",
            "duty as escort?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A5(0x2)
    OP_97(0xB, 0x17E8, 0x1D6, 0xFFFD40E0, 0x1770, 0x1)
    OP_97(0xB, 0x17E8, 0x1D6, 0xFFFD40E0, 0xFA0, 0x1)
    OP_97(0xB, 0x17E8, 0x1D6, 0xFFFF5038, 0x7D0, 0x1)
    SetChrFlags(0xB, 0x20)

    def lambda_2981():

        label("loc_2981")

        OP_99(0xFE, 0x0, 0x7, 0x1388)
        OP_48()
        Jump("loc_2981")

    QueueWorkItem2(0xB, 2, lambda_2981)

    def lambda_2994():
        OP_8F(0xFE, 0x16DA, 0x1450, 0x334, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2994)
    OP_8C(0xB, 180, 200)
    WaitChrThread(0xB, 0x1)
    OP_44(0xB, 0x2)
    Fade(500)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x20)
    SetChrChipByIndex(0xA, 8)
    SetChrSubChip(0xA, 0)
    OP_0D()

    ChrTalk(    #113
        0xB,
        "#310FScreee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x105,
        (
            "#041FHa ha... He's always been\x01",
            "very helpful.\x02\x03",

            "Isn't that right, Sieg?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xB,
        "#311FScree! ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xA,
        "#176F#2PHe's certainly chipper.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x105, 400)
    Sleep(400)

    ChrTalk(    #117
        0xA,
        (
            "#170F...The Arseille is stopped at\x01",
            "the end of the highway.\x02\x03",

            "You're to report in there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x105,
        (
            "#047FUnderstood.\x02\x03",

            "#049F...I'll be leaving school for\x01",
            "a while.\x02\x03",

            "I need to say goodbye to my\x01",
            "teachers before returning to\x01",
            "Grancel.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B5D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B5D)
    OP_6D(14900, 5000, 0, 1800)

    ChrTalk(    #119
        0x105,
        (
            "#040F(Estelle... Joshua...)\x02\x03",

            "(I'll take what you taught me and show you that\x01",
            "I can be strong...stronger than even you two.\x01",
            "I'll do everything in my power to see to that.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(2000, 0)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/R3400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_173D end

    def Function_11_2C3C(): pass

    label("Function_11_2C3C")

    OP_A6(0x2)

    label("loc_2C3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C60")
    OP_97(0xFE, 0x17E8, 0x1D6, 0xFFFA81C0, 0x1F40, 0x1)
    OP_48()
    Jump("loc_2C3F")

    label("loc_2C60")

    OP_A3(0x2)
    Return()

    # Function_11_2C3C end

    def Function_12_2C64(): pass

    label("Function_12_2C64")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #120
        "\x07\x05The gate is firmly shut.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_2C64 end

    def Function_13_2CB8(): pass

    label("Function_13_2CB8")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #121
        (
            "\x07\x05West: Ruan - 175 selge\x01",
            "East: Zeiss - 448 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_2CB8 end

    def Function_14_2D19(): pass

    label("Function_14_2D19")

    TalkBegin(0xFF)
    Sleep(200)
    TalkEnd(0xFF)
    Return()

    # Function_14_2D19 end

    SaveToFile()

Try(main)
