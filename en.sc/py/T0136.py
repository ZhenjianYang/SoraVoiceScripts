from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0136   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0136.x',
        MapIndex            = 8,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0136_1 ._SN',
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
        'Verne',                                # 9
        'Passenger',                            # 10
        'Passenger',                            # 11
        'Ida',                                  # 12
        'Aryll',                                # 13
        'Kitten',                               # 14
        'Kitten',                               # 15
        'Kitten',                               # 16
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
        'ED6_DT07/CH01560 ._CH',             # 00
        'ED6_DT07/CH01140 ._CH',             # 01
        'ED6_DT07/CH01150 ._CH',             # 02
        'ED6_DT07/CH01460 ._CH',             # 03
        'ED6_DT07/CH01470 ._CH',             # 04
        'ED6_DT07/CH01030 ._CH',             # 05
        'ED6_DT07/CH01700 ._CH',             # 06
        'ED6_DT27/CH03880 ._CH',             # 07
        'ED6_DT27/CH03881 ._CH',             # 08
        'ED6_DT27/CH03882 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01560P._CP',             # 00
        'ED6_DT07/CH01140P._CP',             # 01
        'ED6_DT07/CH01150P._CP',             # 02
        'ED6_DT07/CH01460P._CP',             # 03
        'ED6_DT07/CH01470P._CP',             # 04
        'ED6_DT07/CH01030P._CP',             # 05
        'ED6_DT07/CH01700P._CP',             # 06
        'ED6_DT27/CH03880P._CP',             # 07
        'ED6_DT27/CH03881P._CP',             # 08
        'ED6_DT27/CH03882P._CP',             # 09
    )

    DeclNpc(
        X                   = 4500,
        Z                   = 0,
        Y                   = 190662,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -46140,
        Z                   = 0,
        Y                   = 152120,
        Direction           = 80,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -48490,
        Z                   = 0,
        Y                   = 155900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -86540,
        Z                   = 0,
        Y                   = 119250,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -85700,
        Z                   = 0,
        Y                   = 120430,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x195,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 6598,
        TriggerZ            = 0,
        TriggerY            = 190158,
        TriggerRange        = 1000,
        ActorX              = 4500,
        ActorZ              = 1500,
        ActorY              = 190662,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3130,
        TriggerZ            = 0,
        TriggerY            = 192000,
        TriggerRange        = 800,
        ActorX              = 3130,
        ActorZ              = 1000,
        ActorY              = 192000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_242",          # 00, 0
        "Function_1_387",          # 01, 1
        "Function_2_391",          # 02, 2
        "Function_3_3B5",          # 03, 3
        "Function_4_3D9",          # 04, 4
        "Function_5_439",          # 05, 5
        "Function_6_43E",          # 06, 6
        "Function_7_83A",          # 07, 7
        "Function_8_981",          # 08, 8
        "Function_9_9F2",          # 09, 9
        "Function_10_C3C",         # 0A, 10
        "Function_11_C58",         # 0B, 11
    )


    def Function_0_242(): pass

    label("Function_0_242")

    OP_51(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x29, (scpexpr(EXPR_PUSH_LONG, 0x258), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_300")
    OP_A3(0x10F0)
    Event(1, 3)

    label("loc_300")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_386")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrPos(0xB, -85600, 0, 119540, 0)
    SetChrPos(0xF, -84190, 0, 123070, 330)
    SetChrPos(0xE, -83500, 580, 117300, 270)
    SetChrPos(0xD, -83030, 580, 116830, 315)
    OP_43(0xF, 0x1, 0x0, 0x2)
    OP_43(0xE, 0x1, 0x0, 0x3)
    OP_43(0xD, 0x1, 0x0, 0x3)

    label("loc_386")

    Return()

    # Function_0_242 end

    def Function_1_387(): pass

    label("Function_1_387")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    Return()

    # Function_1_387 end

    def Function_2_391(): pass

    label("Function_2_391")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B4")
    OP_8D(0xFE, -85500, 124240, -83590, 123040, 1000)
    Jump("Function_2_391")

    label("loc_3B4")

    Return()

    # Function_2_391 end

    def Function_3_3B5(): pass

    label("Function_3_3B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D8")
    OP_8D(0xFE, -83870, 117760, -83140, 116930, 1000)
    Jump("Function_3_3B5")

    label("loc_3D8")

    Return()

    # Function_3_3B5 end

    def Function_4_3D9(): pass

    label("Function_4_3D9")

    ClearChrFlags(0xFE, 0x1)

    label("loc_3DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_438")
    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xFFFEB754, 0xFB3, 0x1DDB2, 0x3E8, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)
    OP_8E(0xFE, 0xFFFEC1D6, 0xFB3, 0x1DDB2, 0x3E8, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    Jump("loc_3DE")

    label("loc_438")

    Return()

    # Function_4_3D9 end

    def Function_5_439(): pass

    label("Function_5_439")

    Call(0, 6)
    Return()

    # Function_5_439 end

    def Function_6_43E(): pass

    label("Function_6_43E")

    TalkBegin(0x8)
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45E")
    OP_0D()
    OP_A9(0x5)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_45E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46F")
    TalkEnd(0x8)
    Return()

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_836")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 7)), scpexpr(EXPR_END)), "loc_647")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_559")

    ChrTalk(    #0
        0x8,
        (
            "What a bothersome fog! Even nightfall\x01",
            "won't clear it away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "I'd best tell the guests to keep their\x01",
            "windows and doors shut tight tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "Otherwise, the rooms will be damp\x01",
            "and moldy come morning!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_644")

    label("loc_559")


    ChrTalk(    #3
        0x8,
        (
            "If there's anything else, I'll be sure\x01",
            "to contact the guild right away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "Still, though, this fog...\x01",
            "I expected it to drift away with the\x01",
            "night air, but it's just staying put.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        "Where is this fog even coming from, I wonder?\x02",
    )

    CloseMessageWindow()

    label("loc_644")

    Jump("loc_836")

    label("loc_647")

    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x101, 0)
    Sleep(400)

    ChrTalk(    #6
        0x8,
        "Oh, Estelle and Scherazard...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "Busy with bracer work, I see.\x01",
            "Your service is most appreciated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1002FHello, Verne. Anything out of\x01",
            "the ordinary over here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "No, the hotel is quiet as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "...Ah, has there been some manner\x01",
            "of incident?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x103,
        (
            "#020FWe're just taking precautionary measures.\x01",
            "Nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 400)

    ChrTalk(    #12
        0x8,
        "I see. Very good, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "Should anything occur, I will be\x01",
            "sure to contact the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1000FPlease do.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1897)
    OP_A2(0x0)

    label("loc_836")

    TalkEnd(0x8)
    Return()

    # Function_6_43E end

    def Function_7_83A(): pass

    label("Function_7_83A")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_97D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_8C2")

    ChrTalk(    #15
        0xFE,
        (
            "It's been a while since I've spent\x01",
            "the night away from home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Guess I'll just try and make\x01",
            "the best of it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97D")

    label("loc_8C2")


    ChrTalk(    #17
        0xFE,
        (
            "I've contacted my wife,\x01",
            "so I'm not worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Though really, it's been a long\x01",
            "time since I've spent the night\x01",
            "away from home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Guess I'll just try and make\x01",
            "the best of it!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_97D")

    TalkEnd(0x9)
    Return()

    # Function_7_83A end

    def Function_8_981(): pass

    label("Function_8_981")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_9EE")

    ChrTalk(    #20
        0xFE,
        "Ahh, I can see the passenger ships from here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "I wonder if they'll be setting off soon...\x02",
    )

    CloseMessageWindow()

    label("loc_9EE")

    TalkEnd(0xA)
    Return()

    # Function_8_981 end

    def Function_9_9F2(): pass

    label("Function_9_9F2")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_BB5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A63")

    ChrTalk(    #22
        0xFE,
        (
            "Hmmmmm, I wonder what kind of\x01",
            "names would be good...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "Mmm, I'm just not sure.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BB2")

    label("loc_A63")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_B9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_AC8")

    ChrTalk(    #24
        0xFE,
        "I'll be waiting riiight here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "I'm counting on you. For my sweet Aryll!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B99")

    label("loc_AC8")


    ChrTalk(    #26
        0xFE,
        (
            "Oooooh, my dearest bracers.\x01",
            "Did you find my little Aryll?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1000FWe're investigating right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x103,
        (
            "#020FWe'll come to report once we've\x01",
            "found her, so just keep calm and\x01",
            "stay put.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "Thank you!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_B99")

    Jump("loc_BB2")

    label("loc_B9C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_BAE")
    Call(1, 1)
    Jump("loc_BB2")

    label("loc_BAE")

    Call(1, 0)

    label("loc_BB2")

    Jump("loc_C38")

    label("loc_BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_C38")

    ChrTalk(    #30
        0xFE,
        (
            "Oooh, my... I really just CANNOT\x01",
            "see anything in all this fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "*siiigh* At this rate, I may\x01",
            "just get lost myself!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C38")

    TalkEnd(0xB)
    Return()

    # Function_9_9F2 end

    def Function_10_C3C(): pass

    label("Function_10_C3C")

    TalkBegin(0xC)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #32
        0xFE,
        "Nya～～go.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_10_C3C end

    def Function_11_C58(): pass

    label("Function_11_C58")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #33
        (
            "\x07\x05Linen Room\x01",
            "※Employees Only\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_C58 end

    SaveToFile()

Try(main)
