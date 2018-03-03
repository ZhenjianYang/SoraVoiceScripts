from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3131   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Ben',                                  # 9
        'Ursus',                                # 10
        'Randall',                              # 11
        'Muriel',                               # 12
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
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01003 ._CH',             # 02
        'ED6_DT07/CH01050 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01003P._CP',             # 02
        'ED6_DT07/CH01050P._CP',             # 03
    )

    DeclNpc(
        X                   = -2470,
        Z                   = -1000,
        Y                   = 4710,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 5480,
        Z                   = -1000,
        Y                   = 5320,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -450,
        Z                   = -650,
        Y                   = 3980,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1B5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 50,
        Z                   = -1000,
        Y                   = 8500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    DeclActor(
        TriggerX            = -530,
        TriggerZ            = -1000,
        TriggerY            = 4660,
        TriggerRange        = 400,
        ActorX              = -2470,
        ActorZ              = 500,
        ActorY              = 4710,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 660,
        TriggerZ            = -1000,
        TriggerY            = 6600,
        TriggerRange        = 400,
        ActorX              = 50,
        ActorZ              = 500,
        ActorY              = 8500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_192",          # 00, 0
        "Function_1_1B3",          # 01, 1
        "Function_2_1B4",          # 02, 2
        "Function_3_1D8",          # 03, 3
        "Function_4_1DD",          # 04, 4
        "Function_5_312",          # 05, 5
        "Function_6_4AE",          # 06, 6
        "Function_7_4B3",          # 07, 7
        "Function_8_699",          # 08, 8
    )


    def Function_0_192(): pass

    label("Function_0_192")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B2")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)

    label("loc_1B2")

    Return()

    # Function_0_192 end

    def Function_1_1B3(): pass

    label("Function_1_1B3")

    Return()

    # Function_1_1B3 end

    def Function_2_1B4(): pass

    label("Function_2_1B4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D7")
    OP_8D(0xFE, 400, 5540, 5960, 4780, 2000)
    Jump("Function_2_1B4")

    label("loc_1D7")

    Return()

    # Function_2_1B4 end

    def Function_3_1D8(): pass

    label("Function_3_1D8")

    Call(0, 4)
    Return()

    # Function_3_1D8 end

    def Function_4_1DD(): pass

    label("Function_4_1DD")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_30E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_279")
    OP_8C(0x10, 90, 0)

    ChrTalk(    #0
        0x10,
        "Don't freak out so much, Randall.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "She might not look or act like it, but she's not\x01",
            "stupid. She knows what she's doing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30E")

    label("loc_279")


    ChrTalk(    #2
        0x10,
        "H-Hey... You need something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "If you want to order something, go and speak\x01",
            "to the new girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        "I've left her in charge of the counter.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_30E")

    TalkEnd(0x10)
    Return()

    # Function_4_1DD end

    def Function_5_312(): pass

    label("Function_5_312")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_4AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3A9")

    ChrTalk(    #5
        0xFE,
        "...Oops. I forgot to go and wake Louise up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Still, Yuriel is there... I'm sure she woke her\x01",
            "up in my place. ...Probably.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AA")

    label("loc_3A9")


    ChrTalk(    #7
        0xFE,
        (
            "The newbie working here is Randall's \x01",
            "granddaughter, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Her cooking's not half bad, and she's got a\x01",
            "knack for dealing with customers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "...but thanks to her being around, the owner's\x01",
            "gonna have an even better excuse to slack off.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_4AA")

    TalkEnd(0xFE)
    Return()

    # Function_5_312 end

    def Function_6_4AE(): pass

    label("Function_6_4AE")

    Call(0, 7)
    Return()

    # Function_6_4AE end

    def Function_7_4B3(): pass

    label("Function_7_4B3")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_695")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_610")

    ChrTalk(    #10
        0x13,
        "I only work here at this time of day, actually.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x13,
        (
            "Why? I'd much rather be here at lunchtime\x01",
            "than over at ZCF. All there is to do there is\x01",
            "boring crap. The menial stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x13,
        (
            "And I'd say I'm MUCH more suited to being chirpy \x01",
            "and cheery and luring all the boys in here than\x01",
            "being a receptionist in a gloomy factory, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_695")

    label("loc_610")


    ChrTalk(    #13
        0x13,
        "Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x13,
        "We're currently running a lunchtime special offer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x13,
        "Come on in and try out our delicious grub. ㈱\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_695")

    TalkEnd(0x13)
    Return()

    # Function_7_4B3 end

    def Function_8_699(): pass

    label("Function_8_699")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_855")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_77B")

    ChrTalk(    #16
        0xFE,
        (
            "As long as Dan's with them, they shouldn't be able\x01",
            "to cause TOO much trouble, but to say I'm worried\x01",
            "is...an understatement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Those two working on the same project can only\x01",
            "spell trouble... *sigh*\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_855")

    label("loc_77B")


    ChrTalk(    #18
        0xFE,
        (
            "It sounds like old Russell's stirrin' up trouble\x01",
            "again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "And if that's not scary enough, this time he's\x01",
            "got Erika with him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "*sigh* I've never heard two bigger ingredients\x01",
            "for a disaster than that...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_855")

    TalkEnd(0xFE)
    Return()

    # Function_8_699 end

    SaveToFile()

Try(main)
