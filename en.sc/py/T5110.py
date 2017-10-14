from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T5110   ._SN',
        MapName             = 'Other',
        Location            = 'T5110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60025",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T5110   ._SN',
            'ED6_DT21/T5110_1 ._SN',
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
        'Anelace',                              # 9
        'Kurt',                                 # 10
        'Robert',                               # 11
        'Phyllis',                              # 12
        'Target Camera',                        # 13
        'Dish',                                 # 14
        'Dish',                                 # 15
        'Dish',                                 # 16
        'Coffee',                               # 17
        'Coffee',                               # 18
        "Estelle's Bag",                        # 19
        'Orbment',                              # 20
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
        'ED6_DT27/CH03090 ._CH',             # 00
        'ED6_DT27/CH03003 ._CH',             # 01
        'ED6_DT27/CH03093 ._CH',             # 02
        'ED6_DT07/CH01620 ._CH',             # 03
        'ED6_DT07/CH01450 ._CH',             # 04
        'ED6_DT27/CH03900 ._CH',             # 05
        'ED6_DT07/CH01623 ._CH',             # 06
        'ED6_DT06/CH20020 ._CH',             # 07
        'ED6_DT26/CH20269 ._CH',             # 08
        'ED6_DT26/CH20235 ._CH',             # 09
        'ED6_DT27/CH03133 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT27/CH03090P._CP',             # 00
        'ED6_DT27/CH03003P._CP',             # 01
        'ED6_DT27/CH03093P._CP',             # 02
        'ED6_DT07/CH01620P._CP',             # 03
        'ED6_DT07/CH01450P._CP',             # 04
        'ED6_DT27/CH03900P._CP',             # 05
        'ED6_DT07/CH01623P._CP',             # 06
        'ED6_DT06/CH20020P._CP',             # 07
        'ED6_DT26/CH20269P._CP',             # 08
        'ED6_DT26/CH20235P._CP',             # 09
        'ED6_DT27/CH03133P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 26690,
        Z                   = 0,
        Y                   = 5140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 24500,
        Z                   = 0,
        Y                   = 12470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
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
        Unknown3            = 65543,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65543,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65543,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1572871,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638407,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1245192,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 917512,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 120250,
        Y                   = 0,
        Z                   = 1000,
        Range               = 123170,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7D0,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = 25470,
        TriggerZ            = -300,
        TriggerY            = 4940,
        TriggerRange        = 800,
        ActorX              = 26690,
        ActorZ              = 1500,
        ActorY              = 5140,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22500,
        TriggerZ            = 0,
        TriggerY            = 12360,
        TriggerRange        = 800,
        ActorX              = 24500,
        ActorZ              = 1500,
        ActorY              = 12470,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15050,
        TriggerZ            = 0,
        TriggerY            = 12130,
        TriggerRange        = 800,
        ActorX              = 15050,
        ActorZ              = 1000,
        ActorY              = 12130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 85780,
        TriggerZ            = 0,
        TriggerY            = 41480,
        TriggerRange        = 700,
        ActorX              = 85180,
        ActorZ              = 500,
        ActorY              = 41480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 113640,
        TriggerZ            = 0,
        TriggerY            = 41480,
        TriggerRange        = 700,
        ActorX              = 113040,
        ActorZ              = 500,
        ActorY              = 41480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_356",          # 00, 0
        "Function_1_4E2",          # 01, 1
        "Function_2_523",          # 02, 2
        "Function_3_5CA",          # 03, 3
        "Function_4_5CF",          # 04, 4
        "Function_5_5D4",          # 05, 5
        "Function_6_C9A",          # 06, 6
        "Function_7_182F",         # 07, 7
        "Function_8_1C57",         # 08, 8
        "Function_9_3CB1",         # 09, 9
        "Function_10_3D14",        # 0A, 10
    )


    def Function_0_356(): pass

    label("Function_0_356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_360")
    Jump("loc_445")

    label("loc_360")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_END)), "loc_36A")
    Jump("loc_445")

    label("loc_36A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_END)), "loc_374")
    Jump("loc_445")

    label("loc_374")

    SetChrPos(0x8, 115980, 0, 37820, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 84690, 0, -30350, 0)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x0, 0x0, 0x2)
    SetChrPos(0xB, 25910, 0, 16520, 0)
    SetChrPos(0xA, 27980, 0, 6920, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_END)), "loc_3D7")
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_3D7")

    SetChrPos(0xD, 18160, 800, 11990, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x10, 17670, 800, 12040, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xE, 17600, 800, 11180, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, 18270, 800, 10980, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, 18190, 800, 11550, 0)
    ClearChrFlags(0xF, 0x80)

    label("loc_445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A9")
    OP_44(0x9, 0xFF)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x9, 15080, 200, 14890, 180)
    SetChrPos(0x8, 13670, 200, 12380, 0)
    SetChrSubChip(0x9, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x9, 10)
    SetChrChipByIndex(0x8, 2)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)

    label("loc_4A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_4B7")
    OP_A3(0x10F0)
    Event(0, 5)

    label("loc_4B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_4C5")
    OP_A3(0x10F1)
    Event(0, 6)

    label("loc_4C5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E1")
    Event(0, 7)

    label("loc_4E1")

    Return()

    # Function_0_356 end

    def Function_1_4E2(): pass

    label("Function_1_4E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F2")
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 6)), scpexpr(EXPR_END)), "loc_500")
    OP_64(0x2, 0x1)
    Jump("loc_522")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 5)), scpexpr(EXPR_END)), "loc_516")
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    Jump("loc_522")

    label("loc_516")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)

    label("loc_522")

    Return()

    # Function_1_4E2 end

    def Function_2_523(): pass

    label("Function_2_523")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_554"),
        (1, "loc_560"),
        (2, "loc_56C"),
        (3, "loc_578"),
        (4, "loc_584"),
        (5, "loc_590"),
        (6, "loc_59C"),
        (SWITCH_DEFAULT, "loc_5A8"),
    )


    label("loc_554")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_5B4")

    label("loc_560")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_5B4")

    label("loc_56C")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_5B4")

    label("loc_578")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_5B4")

    label("loc_584")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5B4")

    label("loc_590")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_5B4")

    label("loc_59C")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B4")

    label("loc_5A8")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B4")

    label("loc_5B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B4")

    label("loc_5C9")

    Return()

    # Function_2_523 end

    def Function_3_5CA(): pass

    label("Function_3_5CA")

    Call(1, 4)
    Return()

    # Function_3_5CA end

    def Function_4_5CF(): pass

    label("Function_4_5CF")

    Call(1, 5)
    Return()

    # Function_4_5CF end

    def Function_5_5D4(): pass

    label("Function_5_5D4")

    EventBegin(0x0)
    OP_6D(27560, 0, 11600, 0)
    OP_67(0, 5860, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 18080, 200, 12890, 180)
    SetChrPos(0x101, 18120, 200, 10470, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x8, 2)
    SetChrPos(0xD, 18160, 800, 11990, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x10, 17670, 800, 12040, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xE, 17600, 800, 11180, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, 18270, 800, 10980, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0xF, 18190, 800, 11550, 0)
    ClearChrFlags(0xF, 0x80)
    FadeToBright(1000, 0)

    def lambda_6D5():
        OP_6D(18760, 200, 12150, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6D5)

    def lambda_6ED():
        OP_67(0, 7000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6ED)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #0
        0x101,
        (
            "#4P#1016FPhew! Didn't realize how hungry I was!\x02\x03",

            "I hope it isn't a bad idea to eat this\x01",
            "much just before practice, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "#811F#3PYeah, Phyllis' cooking is extra-super yummy!\x02\x03",

            "#816FPlus, Kurt's got something big planned,\x01",
            "so I doubt we'll get a lunch break, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#4P#1006FYeah, good point. We need to keep\x01",
            "our strength up to train, after all.\x02\x03",

            "#1015FMan, though... It's already been\x01",
            "three weeks since I came here.\x02\x03",

            "It feels like it's passed by in the\x01",
            "blink of an eye.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#810F#3PHeehee! Well, you really threw\x01",
            "yourself into it, Estelle.\x02\x03",

            "Training with you has done me\x01",
            "a lot of good, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#4P#1008FAww, thanks, Anelace.\x01",
            "That means a lot.\x02\x03",

            "#1006FI gotta admit, though...while I'm\x01",
            "glad Kurt agreed to train us...\x02\x03",

            "I really didn't expect for you\x01",
            "to be here training with me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#818F#3PWellll...I've only been a 'senior' bracer for,\x01",
            "like, half a year. I'm really still a newbie\x01",
            "myself, to be honest.\x02\x03",

            "#810FSo when Schera told me the whole deal\x01",
            "with you and the training and stuff, I thought,\x01",
            "hey! Perfect!\x02\x03",

            "Kurt and the others had mentioned this place\x01",
            "before, and I'd wanted to come anyway,\x01",
            "so when I heard you were coming, well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#4P#1011FOh, that makes sense.\x02\x03",

            "#1015FY'know, thinking about it, the guild\x01",
            "owning something like this makes me\x01",
            "realize just how big the guild is.\x02\x03",

            "When Dad first told me about it,\x01",
            "I didn't realize how big a thing it'd be.\x02",
        )
    )

    CloseMessageWindow()
    OP_1F(0x46, 0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 65535)
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_5D4 end

    def Function_6_C9A(): pass

    label("Function_6_C9A")

    ClearMapFlags(0x2000000)
    OP_BB(0x0, 0x0, 0x200032)
    OP_BB(0x0, 0x1, 0x0)
    OP_BD()
    EventBegin(0x0)
    OP_6D(18760, 200, 12150, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 18080, 200, 12890, 180)
    SetChrPos(0x101, 18120, 200, 10470, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x8, 2)
    FadeToBright(1000, 0)
    OP_1F(0x64, 0x3E8)
    OP_0D()
    Sleep(500)

    ChrTalk(    #7
        0x8,
        (
            "#810F#3PYeah, it kind of surprised me, too.\x02\x03",

            "Speaking of your folks, those clothes\x01",
            "were a present from Schera, right?\x02\x03",

            "#811FYou're so lucky! I wish Schera would\x01",
            "buy ME clothes! Especially cute stuff\x01",
            "like that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#4P#1013FY-Yeah, they were...\x02\x03",

            "I mean, they're tough and all,\x01",
            "and they're nice and light and\x01",
            "easy to move around in, but...\x02\x03",

            "I don't know if colors this...\x01",
            "girly...are really my thing...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#816F#3PWhat, are you kidding? You look\x01",
            "great! Way better than that old red\x01",
            "outfit of yours.\x02\x03",

            "Remember: we may be bracers, but\x01",
            "we're girls, too. Fashion is important!\x02\x03",

            "#815FNo, BECAUSE we're bracers, we HAVE\x01",
            "to look great! It's our duty!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#4P#1004FUhhhh... Anelace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "#1310F#3PAH! I've got it! Estelle, a hair ribbon!\x02\x03",

            "#811FYou'd look great with one! How about it?\x01",
            "I should have a spare somewhere!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#4P#1008FI-I'll pass, thanks.\x02\x03",

            "#1016FIn fact, I, uh, couldn't help but notice...\x02\x03",

            "You're kind of a...fan of cute things,\x01",
            "aren't you, Anelace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#811F#3PWell, YEAH! Cuteness is justice!\x01",
            "It's the law!\x02\x03",

            "#1310FI mean, okay, I totally get the appeal\x01",
            "of cool, older women like Schera...\x02\x03",

            "But there's nothing--NOT A THING!--\x01",
            "that can beat a young girl who's dressed\x01",
            "up all cute!\x02\x03",

            "#1311FAnd whenever I see a teddy bear or\x01",
            "a stuffed animal, I just wanna hug it\x01",
            "to death and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#4P#1016FAh...hahaha...\x02\x03",

            "(If she ever met Tita, she'd probably faint...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#1314F#3PHmmm, but, y'know...\x02\x03",

            "You've changed a lot since I first met you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#4P#1004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#817F#3PWell, when we first met way back when,\x01",
            "you had this real 'I'm a naive innocent\x01",
            "newbie' air about you.\x02\x03",

            "And you still have that air of newbieness\x01",
            "around you, but now it seems like you've\x01",
            "got some...steel in your soul, I guess.\x02\x03",

            "#816FIt's pretty incredible, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#4P#1008FAwww, A-Anelace, cut it out with the flattery!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#811F#3PHaha! Don't get so embarrassed. I meant it.\x02\x03",

            "#816FBesides, you make me want to work harder.\x01",
            "Can't let a young upstart like you take\x01",
            "my 'cutest and best bracer ever' title!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#4P#1013FR-Really...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #21
        0x101,
        (
            "#4P#1004FAnyway, shouldn't we be\x01",
            "getting to practice soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#814F#3PYeah, it's about time, I guess, huh?\x01",
            "Let's go back to our rooms and get\x01",
            "ready.\x02\x03",

            "#811FSee you in a bit!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0x8, 0)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, 19230, 0, 12970, 98)
    OP_0D()
    SetChrSubChip(0x101, 2)
    OP_8E(0x8, 0x5154, 0x0, 0x2472, 0xBB8, 0x0)

    def lambda_164C():
        OP_8E(0x8, 0x6CAC, 0x7D0, 0x2346, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_164C)

    def lambda_1667():
        OP_6D(20870, 200, 10700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1667)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x1)

    def lambda_1689():
        OP_8E(0x8, 0x6C84, 0x7D0, 0x2ABC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1689)
    WaitChrThread(0x8, 0x1)

    def lambda_16A9():
        OP_8E(0x8, 0x63D8, 0xDAC, 0x2C1A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_16A9)

    def lambda_16C4():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_16C4)
    WaitChrThread(0x8, 0x1)

    def lambda_16DB():
        OP_6D(18770, 200, 11170, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16DB)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x8, 0x80)

    ChrTalk(    #23
        0x101,
        (
            "#6P#1017FGeez, she's like a ball of energy.\x02\x03",

            "...I'm so glad to have her with me, though.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(500)

    ChrTalk(    #24
        0x101,
        (
            "#6P#1006FAll right. Gotta stop by my room\x01",
            "and get my stuff together!\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x363, 1)
    OP_3E(0x35D, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(19120, 0, 10210, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x4)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 19120, 0, 10210, 103)
    OP_A2(0x1004)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_6_C9A end

    def Function_7_182F(): pass

    label("Function_7_182F")

    EventBegin(0x0)
    OP_6D(87090, 0, 40680, 0)
    OP_67(0, 6050, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 86470, 0, 35830, 0)
    SetChrFlags(0x101, 0x80)
    SetChrPos(0x12, 84860, 100, 41540, 0)
    SetChrChipByIndex(0x12, 8)
    SetChrSubChip(0x12, 0)
    ClearChrFlags(0x12, 0x80)
    FadeToBright(1000, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x80)

    def lambda_18C3():
        OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_18C3)
    OP_8E(0x101, 0x151EE, 0x0, 0x922C, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #25
        0x101,
        (
            "#1015F#5POkay, this is 'Kurt Practice' we're talking\x01",
            "about, so let's assume I'll need everything.\x01",
            "Kitchen sink included.\x02\x03",

            "It'll be just like real combat, so I'll have no\x01",
            "idea what to expect...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_19B9():
        OP_6D(87290, 0, 42930, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_19B9)

    def lambda_19D1():
        OP_67(0, 6050, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19D1)

    def lambda_19E9():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19E9)
    OP_8E(0x101, 0x150B8, 0x0, 0xA2EE, 0x7D0, 0x0)
    OP_8C(0x101, 261, 500)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #26
        "\x07\x05Estelle took the harmonica out of her bag.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Fade(500)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 7)
    OP_0D()

    ChrTalk(    #27
        0x101,
        (
            "#6P#1025F...\x02\x03",

            "#1012FOkay... I'll do my best today, too.\x01",
            "I promise.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x101, 0x2)
    OP_0D()
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    SetChrFlags(0x12, 0x80)
    OP_D6(0x1)
    OP_3E(0x35F, 1)
    OP_3E(0x363, 1)
    OP_3E(0x35D, 1)
    OP_3E(0x411, 1)
    AddMira(1000)
    OP_41(0x0, 0x9, 0xFF)
    OP_41(0x0, 0x104, 0xFF)
    OP_41(0x0, 0x125, 0xFF)
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #28
        "\x07\x00Packed away #1041i.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #29
        "\x07\x00Equipped #009i.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #30
        "\x07\x00Equipped #260i.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #31
        "\x07\x00Equipped #293i.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x456, 3)), scpexpr(EXPR_END)), "loc_1BD7")
    OP_3E(0x417, 1)
    OP_A3(0x22B3)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #32
        "\x07\x00Packed away #1047i.\x02",
    )

    CloseMessageWindow()

    label("loc_1BD7")

    OP_22(0x14, 0x0, 0x64)

    AnonymousTalk(    #33
        "#0CPacked away #4C1000#0C mira.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #34
        0x101,
        (
            "#6P#1006FAll right, that's everything.\x02\x03",

            "Next stop, the entrance!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1005)
    EventEnd(0x0)
    Return()

    # Function_7_182F end

    def Function_8_1C57(): pass

    label("Function_8_1C57")

    EventBegin(0x0)
    OP_44(0x9, 0x0)
    OP_44(0x8, 0x0)
    Fade(1000)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 15080, 200, 12380, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 1)
    OP_6D(15150, 0, 14940, 0)
    OP_67(0, 6200, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DA0")

    ChrTalk(    #35
        0x9,
        (
            "#843FAh, there you are, Estelle.\x01",
            "Let's begin today's practice, then.\x02\x03",

            "#842FToday, I want you and Anelace to cover\x01",
            "ruins exploration.\x02\x03",

            "We'll be heading to the Balstar Channel, \x01",
            "which is west of the lodge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E2B")

    label("loc_1DA0")


    ChrTalk(    #36
        0x9,
        (
            "#842FToday, I want you and Anelace to cover\x01",
            "ruins exploration.\x02\x03",

            "We'll be heading to the Balstar Channel, \x01",
            "which is west of the lodge.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E2B")


    ChrTalk(    #37
        0x101,
        (
            "#1002FThe Balstar Channel...\x02\x03",

            "Kind of a strange name, but it's\x01",
            "another training facility, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "#840FYes, that's exactly it. It's an old\x01",
            "aqueduct from the Middle Ages\x01",
            "that the guild repurposed.\x02\x03",

            "Several of its defense mechanisms\x01",
            "are still operable, plus quite a few\x01",
            "monsters have made it their nest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#816F#6PTraps and monsters, huh? Yep, that\x01",
            "sounds like practice, 'Kurt-style' to me.\x02\x03",

            "So let's head off to this aqua thingy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "#843FHold a moment. Before we leave...\x02\x03",

            "#842FI want you two to take a look at these.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #41
        "\x07\x05Kurt produced a pair of strangely configured orbments.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrFlags(0x13, 0x4)
    OP_22(0x82, 0x0, 0x64)
    SetChrPos(0x13, 14500, 150, 13630, 180)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x13, 8)
    SetChrSubChip(0x13, 1)
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_AD(0x24008F, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #42
        "\x07\x00#1004FWhat...? This is...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("Anelace")

    AnonymousTalk(    #43
        (
            "\x07\x00#814F#6PIt looks like a combat orbment,\x01",
            "but it's all weird.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 0, -1, -1)
    SetChrName("Kurt")

    AnonymousTalk(    #44
        (
            "\x07\x00#840FCorrect. This is a new model combat orbment.\x02\x03",

            "You know, of course, of the Epstein Foundation \x01",
            "which develops combat orbments, among\x01",
            "many other orbal technologies.\x02\x03",

            "This is a new kind of combat orbment\x01",
            "developed by the foundation and supplied\x01",
            "to the guild mere weeks ago.\x02\x03",

            "As you can see, they have an additional slot\x01",
            "compared to previous orbments, for a total of\x01",
            "seven.\x02\x03",

            "As a result, this should allow for the utilization\x01",
            "of new, more powerful combat arts.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #45
        "\x07\x00#1006FWhoa... That's incredible!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 300, -1, -1)
    SetChrName("Anelace")

    AnonymousTalk(    #46
        (
            "\x07\x00#811F#6PHeck yeah, it is!\x01",
            "These'll make us awesome!\x02\x03",

            "#810FSo don't be stingy, Kurt,\x01",
            "make with the goodies!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(180, 0, -1, -1)
    SetChrName("Kurt")

    AnonymousTalk(    #47
        (
            "\x07\x00#840FIf you wish, the guild\x01",
            "will provide you each with one for free.\x02\x03",

            "#843FHowever...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #48
        0x9,
        (
            "#842FThere is, as you may expect, a catch.\x02\x03",

            "The circuit architecture within these\x01",
            "orbments is radically different from\x01",
            "your current combat orbments.\x02\x03",

            "As a result, your old quartz crystals\x01",
            "are not compatible with these new\x01",
            "orbments whatsoever.\x02\x03",

            "You will need to obtain new, revised\x01",
            "quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1004FWhat?!\x02\x03",

            "But that'd mean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#814F#6PThat all the quartz we've made\x01",
            "up till now are worthless?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x9,
        (
            "#840FI'm afraid so, yes.\x02\x03",

            "It will be a hassle, but you'll need\x01",
            "to rebuild your quartz collection\x01",
            "from scratch if you use these.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1007FOh, no waaaay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#1316F#6PSheesh... This IS a hard choice.\x02\x03",

            "#810FCould we keep using our current orbments?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "#843FYou could, but I don't recommend it.\x02\x03",

            "#842FThese new orbments are superior\x01",
            "models in every way.\x02\x03",

            "Their maximum 'EP' potential is higher,\x01",
            "and the high-end new quartz they can\x01",
            "accept have impressive capabilities.\x02\x03",

            "In the long term, they will grant you\x01",
            "increased physical abilities...\x02\x03",

            "#843FAnd most importantly, the arts they\x01",
            "can construct are far beyond what\x01",
            "your current orbments are capable of.\x02\x03",

            "#842FEstelle. You recall our...'good friend,'\x01",
            "Lieutenant Lorence, I assume?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1020FWhat?!\x02",
    )

    CloseMessageWindow()
    OP_AD(0x2400BF, 0x0, 0x0, 0xC8)
    Sleep(2000)
    OP_AE(0xC8)
    Sleep(1000)

    ChrTalk(    #56
        0x101,
        (
            "#1026FL-Lorence? Yeah...\x02\x03",

            "Don't think I could forget him\x01",
            "even if I wanted to...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        (
            "#842FSchera told me about a certain\x01",
            "bizarre art he used against you.\x02\x03",

            "A terrifying attack that lashed out\x01",
            "at your entire team and clouded\x01",
            "your minds...\x02\x03",

            "As it happens, this orbment can\x01",
            "manifest an art exactly like that\x01",
            "with the correct quartz combination.\x02\x03",

            "It's been dubbed 'Silver Thorn.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#1002F 'Silver Thorn'...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #59
        0x8,
        (
            "#812F#6PW-Wait, hang on a sec here...\x02\x03",

            "Wouldn't that mean that red uniform bozo\x01",
            "had one of these new model orbments?!\x01",
            "TWO MONTHS ago?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        (
            "#843FA scary thought, but it's very possible.\x01",
            "The implications of which are...\x02\x03",

            "#842F...Well. For now, I must know.\x01",
            "Will you accept the new orbments?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "#813F#6PHmmmmm... Man, this is so tough.\x02\x03",

            "With a bit of work, it'd make us awesome,\x01",
            "but right now it'd be a nasty drop in power...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1010F...\x02\x03",

            "#1011FI... I'd like the new model, Kurt.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 2)
    Sleep(400)

    ChrTalk(    #63
        0x8,
        "#814F#6PBwuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1003FLorence...or whatever his name is...\x01",
            "beat us away like a...a tiger swatting\x01",
            "at a playful cub.\x02\x03",

            "I know a new orbment won't make\x01",
            "me innately stronger, but...\x02\x03",

            "#1002FIf this could give me even the tiniest\x01",
            "edge...I'd like to master it.\x02\x03",

            "So, please...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#814F#6PEstelle...\x02\x03",

            "#816FYeah... You're right!\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    Sleep(400)

    ChrTalk(    #66
        0x8,
        (
            "#1310F#6PLike I said, Kurt!\x01",
            "Fork over the goodies!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "#841FVery well.\x02\x03",

            "Go ahead and take them.\x02",
        )
    )

    CloseMessageWindow()
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    ClearChrFlags(0x13, 0x80)
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #68
        "\x07\x05Estelle and Anelace received new model combat orbments.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3E(0x20A, 1)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #69
        0x9,
        "#840FAlso, take these.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #70
        "\x07\x05Estelle and Anelace received various kinds of sepith.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddSepith(0x0, 0x14)
    AddSepith(0x1, 0x14)
    AddSepith(0x2, 0x32)
    AddSepith(0x3, 0x14)
    AddSepith(0x4, 0x64)
    AddSepith(0x6, 0x14)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #71
        0x9,
        (
            "#840FThat should be enough to synthesize\x01",
            "a basic selection of quartz.\x02\x03",

            "Robert's stationed at the workshop\x01",
            "there in the corner, so he'll be\x01",
            "able to help you prepare some quartz.\x02\x03",

            "Incidentally, your Bracer Notebook\x01",
            "should also cover all of the new quartz\x01",
            "and arts available.\x02\x03",

            "It might not be a bad idea to skim\x01",
            "through it before talking to him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1006FSure, we'll do that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "#840FIn addition, today's practice is likely\x01",
            "to be, ah, long duration, shall we say.\x02\x03",

            "I would recommend bringing some\x01",
            "food, just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "#818F#6PAh, right, food!\x02\x03",

            "#816FWe just talk to Phyllis about that,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x9,
        (
            "#843FCorrect.\x02\x03",

            "Talk to Robert and Phyllis for\x01",
            "anything you might need before\x01",
            "we begin practice.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x35), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x34), scpexpr(EXPR_PUSH_LONG, 0x170), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_32A4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32AE")

    label("loc_32A4")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32AE")

    Jump("loc_32E0")

    label("loc_32B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x35), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32CA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32E0")

    label("loc_32CA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x35), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32E0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3919")
    Sleep(500)

    ChrTalk(    #76
        0x9,
        (
            "#840FAh, Estelle, before I forget.\x01",
            "These are for you.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (1, "loc_334F"),
        (2, "loc_351C"),
        (3, "loc_3692"),
        (4, "loc_37E7"),
        (SWITCH_DEFAULT, "loc_3910"),
    )


    label("loc_334F")

    OP_3E(0x14F, 1)
    OP_3E(0x1FD, 1)
    OP_3E(0x140, 1)
    OP_3E(0x2D9, 1)
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #77
        "\x07\x00Received #335i.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #78
        "\x07\x00Received #509i.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #79
        "\x07\x00Received #320i.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #80
        "\x07\x00Received #729i quartz.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #81
        0x101,
        "#1004FHey, these are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "#1310F#6POooh, shiny!\x02\x03",

            "#811FAnd it all looks really high quality, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        (
            "#841FYes, they're all quite valuable.\x02\x03",

            "The quartz, naturally, is for your new\x01",
            "orbment.\x02\x03",

            "Think of them as a reward from the\x01",
            "guild for your successes as a junior\x01",
            "bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        "#1008FHeehee, thanks!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3910")

    label("loc_351C")

    FadeToDark(300, 0, 100)
    OP_3E(0x14F, 1)
    OP_3E(0x1FD, 1)
    OP_3E(0x140, 1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #85
        "\x07\x00Received #335i.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #86
        "\x07\x00Received #509i.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #87
        "\x07\x00Received #320i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #88
        0x101,
        "#1004FHey, these are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "#1310F#6POooh, shiny!\x02\x03",

            "#811FAnd it all looks really high quality, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "#841FYes, they're all quite valuable.\x02\x03",

            "Think of them as a reward from the\x01",
            "guild for your successes as a junior\x01",
            "bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        "#1008FHeehee, thanks!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3910")

    label("loc_3692")

    FadeToDark(300, 0, 100)
    OP_3E(0x14F, 1)
    OP_3E(0x1FD, 1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #92
        "\x07\x00Received #335i.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #93
        "\x07\x00Received #509i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #94
        0x101,
        "#1004FHey, these are...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        (
            "#1310F#6POooh, shiny!\x02\x03",

            "#811FAnd they both look really high quality, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x9,
        (
            "#841FYes, they're quite valuable.\x02\x03",

            "Think of them as a reward from the\x01",
            "guild for your successes as a junior\x01",
            "bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#1008FHeehee, thanks!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3910")

    label("loc_37E7")

    FadeToDark(300, 0, 100)
    OP_3E(0x14F, 1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #98
        "\x07\x00Received #335i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #99
        0x101,
        "#1004FHey, this is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "#1310F#6POooh, shiny!\x02\x03",

            "#811FAnd it looks really high quality, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "#841FYes, it's quite valuable.\x02\x03",

            "Think of it as a reward from the\x01",
            "guild for your successes as a junior\x01",
            "bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1008FHeehee, thanks!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3910")

    label("loc_3910")

    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_3919")

    Sleep(500)

    ChrTalk(    #103
        0x9,
        (
            "#840FNow, then. I shall wait for you\x01",
            "outside the lodge.\x02\x03",

            "Come see me once you're ready.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    SetChrPos(0x9, 16210, 0, 14960, 93)
    ClearChrFlags(0x9, 0x4)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 3)
    OP_0D()

    def lambda_39AC():
        OP_6D(18450, 0, 12380, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_39AC)
    SetChrSubChip(0x8, 2)

    def lambda_39C9():
        OP_8E(0x9, 0x48DA, 0x0, 0x38A4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_39C9)
    Sleep(500)
    SetChrSubChip(0x101, 2)
    WaitChrThread(0x9, 0x0)

    def lambda_39F3():
        OP_8E(0x9, 0x5294, 0x0, 0x2E86, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_39F3)
    WaitChrThread(0x9, 0x1)

    def lambda_3A13():
        OP_8E(0x9, 0x53E8, 0xFFFFFED4, 0x1B58, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3A13)
    WaitChrThread(0x9, 0x2)
    SetChrFlags(0x9, 0x80)
    Sleep(1000)

    def lambda_3A3D():
        OP_6D(14220, 600, 12150, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A3D)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #104
        0x8,
        "#816F#6POkay, Estelle! Let's go get ready!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0)
    Sleep(75)
    SetChrSubChip(0x101, 1)
    Sleep(400)

    ChrTalk(    #105
        0x101,
        "#1006F#4PRight! Let's talk to Phyllis and Robert.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x101, 0)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x80)
    AddParty(0x9, 0xF7, 0xFF)
    SetChrPos(0x101, 16020, 0, 11870, 160)
    SetChrPos(0x10A, 16020, 0, 11870, 160)
    OP_6D(16020, 0, 11870, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_41(0x9, 0xCF, 0xFF)
    OP_41(0x9, 0x104, 0xFF)
    OP_41(0x9, 0x125, 0xFF)
    OP_BB(0x9, 0x6, 0x110)
    OP_31(0x9, 0x0, 0x28)
    OP_31(0x9, 0xFE, 0x0)
    OP_35(0x9, 0x0)
    Sleep(500)
    OP_64(0x2, 0x1)
    OP_A2(0x1006)
    OP_28(0xC5, 0x4, 0x2)
    OP_28(0xC5, 0x4, 0x8)
    OP_28(0xC5, 0x1, 0x1)
    OP_28(0xC5, 0x1, 0x2)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #106
        (
            "\x07\x05You may now access your Senior Bracer Notebook. This notebook\x01",
            "contains information about your jobs, related events, orbment info,\x01",
            "etc.\x02\x03",

            "To read your Bracer Notebook, open the Items tab from the Camp\x01",
            "menu, and under the 'Book' category, select 'Bracer Notebook.' \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_8_1C57 end

    def Function_9_3CB1(): pass

    label("Function_9_3CB1")

    EventBegin(0x1)
    OP_8C(0x0, 174, 500)
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #107
        "\x07\x05The door is locked tight.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_9_3CB1 end

    def Function_10_3D14(): pass

    label("Function_10_3D14")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Rest\x01",      # 0
            "Stop\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D9B")
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x9, 0xFE, 0x0)
    OP_8C(0x0, 270, 0)
    OP_30(0x0)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_3D9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DB5")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_3DB5")

    Return()

    # Function_10_3D14 end

    SaveToFile()

Try(main)
