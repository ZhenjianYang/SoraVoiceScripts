from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2321   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2321.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
        'Creda',                                # 9
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
        'ED6_DT07/CH01010 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01010P._CP',             # 00
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 500,
        Y                   = 8800,
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


    DeclActor(
        TriggerX            = -4040,
        TriggerZ            = 500,
        TriggerY            = 7530,
        TriggerRange        = 400,
        ActorX              = -4000,
        ActorZ              = 2000,
        ActorY              = 8800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F6",           # 00, 0
        "Function_1_14E",          # 01, 1
        "Function_2_14F",          # 02, 2
        "Function_3_165",          # 03, 3
        "Function_4_16A",          # 04, 4
    )


    def Function_0_F6(): pass

    label("Function_0_F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_100")
    Jump("loc_14D")

    label("loc_100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_10A")
    Jump("loc_14D")

    label("loc_10A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_114")
    Jump("loc_14D")

    label("loc_114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_11E")
    Jump("loc_14D")

    label("loc_11E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_128")
    Jump("loc_14D")

    label("loc_128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_132")
    Jump("loc_14D")

    label("loc_132")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_13C")
    Jump("loc_14D")

    label("loc_13C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_146")
    Jump("loc_14D")

    label("loc_146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_14D")

    label("loc_14D")

    Return()

    # Function_0_F6 end

    def Function_1_14E(): pass

    label("Function_1_14E")

    Return()

    # Function_1_14E end

    def Function_2_14F(): pass

    label("Function_2_14F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_164")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_14F")

    label("loc_164")

    Return()

    # Function_2_14F end

    def Function_3_165(): pass

    label("Function_3_165")

    Call(0, 4)
    Return()

    # Function_3_165 end

    def Function_4_16A(): pass

    label("Function_4_16A")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA")
    OP_0D()
    OP_A9(0x28)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_1CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DB")
    TalkEnd(0x8)
    Return()

    label("loc_1DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_26B")

    ChrTalk(    #0
        0x8,
        (
            "The suspect is at the\x01",
            "Windmill Lodge?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "I'd like a chance to throw some\x01",
            "rocks at him before you hand\x01",
            "him over to the guild...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_927")

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_304")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CE")
    OP_A2(0x0)

    ChrTalk(    #2
        0x8,
        "The store's closed...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "Perhaps I could bring the\x01",
            "children a treat...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_301")

    label("loc_2CE")


    ChrTalk(    #4
        0x8,
        (
            "Perhaps I could bring the\x01",
            "children a treat...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_301")

    Jump("loc_927")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_476")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EB")
    OP_A2(0x0)

    ChrTalk(    #5
        0x8,
        (
            "It's so good of you to come play\x01",
            "with the kids at the orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "It's as if they've suddenly become\x01",
            "everyone's grandchildren.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "I tend to prefer the quiet,\x01",
            "but I don't mind hearing\x01",
            "their laughter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_473")

    label("loc_3EB")


    ChrTalk(    #8
        0x8,
        (
            "It's so good of you to come play\x01",
            "with the kids at the orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "It's as if they've suddenly become\x01",
            "everyone's grandchildren.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_473")

    Jump("loc_927")

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_517")

    ChrTalk(    #10
        0x8,
        (
            "It must have taken a truly\x01",
            "heartless individual to set\x01",
            "fire to an orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "It's just not the kind of thing any\x01",
            "human should be capable of.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_927")

    label("loc_517")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_574")

    ChrTalk(    #12
        0x8,
        "Maybe I'm just imagining things...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "But the village certainly\x01",
            "seems busy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_927")

    label("loc_574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_67D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61F")
    OP_A2(0x0)

    ChrTalk(    #14
        0x8,
        (
            "Aren't the flowers overlooking\x01",
            "the village beautiful?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "It's very convenient, having a city\x01",
            "like Ruan so close by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        "I quite like it here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_67A")

    label("loc_61F")


    ChrTalk(    #17
        0x8,
        (
            "It's very convenient, having a city\x01",
            "like Ruan so close by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "I quite like it here.\x02",
    )

    CloseMessageWindow()

    label("loc_67A")

    Jump("loc_927")

    label("loc_67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_7C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_774")
    OP_A2(0x0)

    ChrTalk(    #19
        0x8,
        (
            "Some people say the airships are the\x01",
            "reason no one comes here anymore, and\x01",
            "why all the young people leave.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "I, for one, enjoy the peace\x01",
            "and quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "I just want a nice, quiet place\x01",
            "where I can grow old gracefully.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C1")

    label("loc_774")


    ChrTalk(    #22
        0x8,
        (
            "People say Manoria is turning\x01",
            "into a ghost town, but I enjoy\x01",
            "the quiet.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C1")

    Jump("loc_927")

    label("loc_7C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_834")

    ChrTalk(    #23
        0x8,
        "A boy in a cap, you say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "He hasn't come into the store.\x01",
            "Perhaps Sadie's seen him pass by?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_927")

    label("loc_834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_927")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D3")
    OP_A2(0x0)

    ChrTalk(    #25
        0x8,
        (
            "My granddaughter, Sadie, really\x01",
            "is the sweetest girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        "Her parents left to find work...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "But Sadie stays here to be\x01",
            "with me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_927")

    label("loc_8D3")


    ChrTalk(    #28
        0x8,
        (
            "My granddaughter, Sadie, really\x01",
            "is the sweetest girl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        "I'm truly grateful.\x02",
    )

    CloseMessageWindow()

    label("loc_927")

    TalkEnd(0x8)
    Return()

    # Function_4_16A end

    SaveToFile()

Try(main)
